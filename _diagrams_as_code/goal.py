from diagrams import Cluster, Diagram, Edge
from diagrams.k8s.compute import Pod, DaemonSet
from diagrams.aws.analytics import Kinesis
from diagrams.aws.compute import LambdaFunction
from diagrams.elastic.elasticsearch import Elasticsearch
from diagrams.aws.storage import S3
from diagrams.saas.chat import Slack

graph_attr = {"fontsize": "15"}
with Diagram(
    "logging", filename="goal.py", outformat="png", show=False):
    with Cluster("AWS Account - YOUR--ACCOUNT", graph_attr=graph_attr):
        s3_bucket = S3("logs")
        logs_lambda_eip = LambdaFunction("logs-processor")
        slack_channel = Slack("python_workshop")
        s3_bucket >> Edge(label="trigger") >> logs_lambda_eip  >> Edge(label="notify") >> slack_channel
