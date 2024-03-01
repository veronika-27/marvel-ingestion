import boto3
import json


class AWSRolesAndPolicies:
    """
    Class to represent AWSRolesAndPolicies obj. for managing the aws roles and policies
    -----
    Methods:
        create_bucket_policy (policy_name: str): creates s3 bucket full access policy
        create_s3_role (role_name: str, account: str): creates role for the s3 bucket
        list_policies (policy_name): returns the arn for provided policy
        attach_policy_to_role (policy_name: str, policy_arn: str): attaches policy to role
        create_sf_read_only_policy (resource: str, policy_name: str): creates read only policy to be used for SF ingration
        create_sf_role (aws: str, external_id: str, role_name: str): creates aws role for snowflake integration
    """

    def __init__(self):
        self.iam = boto3.client("iam")

    def create_bucket_policy(self, policy_name: str):
        """
        Creates s3 bucket full access  policy
        :param:
            policy_name (str): the name wanted to be used for the policy
        """
        self.iam = boto3.client("iam")
        policyDocument = {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Effect": "Allow",
                    "Action": ["s3:*", "s3-object-lambda:*"],
                    "Resource": "*",
                }
            ],
        }
        response = self.iam.create_policy(
            PolicyName=policy_name,
            PolicyDocument=json.dumps(policyDocument),
            Description="Full access s3 bucket",
        )
        print(response)

    def create_s3_role(self, role_name: str, account: str):
        """
        Creates needed aws role (trusted entity) to manage s3
        :param:
            role_name (str): the way the role could be named
            account (str): account id
        :return:
            "RoleName"(str): name of the role created
        """
        trusted_entities = json.dumps(
            {
                "Version": "2012-10-17",
                "Statement": [
                    {
                        "Effect": "Allow",
                        "Action": "sts:AssumeRole",
                        "Principal": {"AWS": account},
                        "Condition": {},
                    }
                ],
            }
        )
        response = self.iam.create_role(
            RoleName=role_name, AssumeRolePolicyDocument=trusted_entities
        )
        return response["Role"]["RoleName"]

    def list_policies(self, policy_name: str):
        """
        Lists aws policy arn for specific policy
        :param:
            policy_name (str): name of the policy which arn is needed
        :return:
            policy_arn (str): the aws arn for specific policy
        """
        paginator = self.iam.get_paginator("list_policies")
        for response in paginator.paginate(Scope="Local"):
            for policy in response["Policies"]:
                if policy_name == policy["PolicyName"]:
                    policy_arn = policy["Arn"]
                    return policy_arn

    def attach_policy_to_role(self, role_name: str, policy_arn: str):
        """
        Attaches specific iam policy to specific iam role
        :param:
            role_name (str): name of the role to be attached to
            policy_arn (str): name of the policy to be attached to specific role
        """
        response = self.iam.attach_role_policy(RoleName=role_name, PolicyArn=policy_arn)
        print(response)

    # SF related part

    def create_sf_read_only_policy(
        self, resource: str, policy_name: str, bucket_name: str
    ):
        """
        Creates read only policy to be used from SF
        :param:
            resource (str): the arn for the s3 bucket + object(folder)
            policy_name (str): name of the policy to be created
        """
        self.iam = boto3.client("iam")
        policyDocumet = {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Effect": "Allow",
                    "Action": ["s3:GetObject", "s3:GetObjectVersion"],
                    "Resource": resource,
                },
                {
                    "Effect": "Allow",
                    "Action": ["s3:ListBucket", "s3:GetBucketLocation"],
                    "Resource": "arn:aws:s3:::" + bucket_name,
                    "Condition": {"StringLike": {"s3:prefix": ["ingest_data/*"]}},
                },
            ],
        }
        response = self.iam.create_policy(
            PolicyName=policy_name,
            PolicyDocument=json.dumps(policyDocumet),
            Description="Read only policy",
        )
        # print(response)

    def create_sf_role(
        self,
        aws: str,  # sf_iam_id
        external_id: str,  # sf_role_id
        role_name: str,  # bucket_name+-SF
    ):
        """
        Creates needed aws role (trusted entity) for snowflake integration
        :param:
            aws (str): aws iam user arn (equivalent in SF: STORAGE_AWS_IAM_USER_ARN)
            external_id (str): snowflake id for snowflake role (equivalent in SF: STORAGE_AWS_EXTERNAL_ID)
            role_name (str): name of the role to be created
        :return:
            role_name (str): name of the role created
        """
        trusted_policy = json.dumps(
            {
                "Version": "2012-10-17",
                "Statement": [
                    {
                        "Effect": "Allow",
                        "Principal": {"AWS": aws},
                        "Action": "sts:AssumeRole",
                        "Condition": {"StringEquals": {"sts:ExternalId": external_id}},
                    }
                ],
            }
        )

        response = self.iam.create_role(
            RoleName=role_name, AssumeRolePolicyDocument=trusted_policy
        )
        role_name = response["Role"]["RoleName"]
        return role_name
