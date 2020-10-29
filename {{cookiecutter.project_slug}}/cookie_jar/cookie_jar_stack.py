from aws_cdk import aws_s3 as s3, aws_s3_deployment as s3deploy, core


class CookieJarStack(core.Stack):
    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)
        # The Bucket itself
        cookie_jar = s3.Bucket(
            self,
            "{{cookiecutter.project_name}}-cookie-jar",
            # bucket_name="{{cookiecutter.project_slug}}",
            website_index_document="index.html",
            website_error_document="404.html",
            public_read_access=True,
        )

        # The deployment for the Bucket
        s3deploy.BucketDeployment(
            self,
            "{{cookiecutter.project_name}}",
            sources=[s3deploy.Source.asset("../dough/dist")],
            destination_bucket=cookie_jar,
            retain_on_delete=False,
            prune=false,
        )

        core.CfnOutput(self, "S3Website", value=cookie_jar.bucket_website_url)