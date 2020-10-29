from aws_cdk import aws_lambda as _lambda, aws_apigateway as api_gw, core
import os


class ChocoStack(core.Stack):
    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)
        handler_name = ""
        lambda_dir = "../chocolate_chips"
        {% if cookiecutter.chocolate_chips == "Flask" %}
        lambda_dir = f"{lambda_dir}/flask"
        {% endif %}
        for api in os.listdir(lambda_dir):
            content_name = f"{lambda_dir}/{api}"
            if os.path.isfile(content_name):
                with open(content_name, "r") as choco:
                    if choco.read().find("handler") > 0:
                        handler_name = api.replace(".py", "")

        chocolate = _lambda.Function(
            self,
            "chocolateHandler",
            runtime=_lambda.Runtime.PYTHON_3_8,
            handler=f"{handler_name}.handler",
            code=_lambda.Code.from_asset(lambda_dir),
        )

        # defines an API Gateway REST API resource backed by our "lambda_lith" function.
        gw = api_gw.LambdaRestApi(self, "CookieApi", handler=chocolate)

        core.CfnOutput(self, "ApiUrl", value=gw.url)