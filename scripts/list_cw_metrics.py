import boto3


session = boto3.Session(
    region_name='ap-northeast-1'
)
client = session.client("cloudwatch")


response = client.list_metrics(
    Namespace='CWAgent',
    MetricName='disk_used_percent',
)
results = response["Metrics"]
while "NextToken" in response:
    response = client.list_metrics(NextToken=response["NextToken"])
    results.extend(response["Metrics"])


for r in results:
    if r['MetricName'] == 'disk_used_percent':
        print()
        for k, v in r.items():
            print(k, v)
            