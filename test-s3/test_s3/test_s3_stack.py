from aws_cdk import core as cdk, aws_s3 as s3


class TestS3Stack(cdk.Stack):
    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        bucket = s3.Bucket(
            self,
            "MyBucket",
            versioned=True,
            public_read_access=True,
            removal_policy= cdk.RemovalPolicy.DESTROY
        )
