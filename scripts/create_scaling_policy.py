import boto3


session = boto3.Session(region_name='ap-northeast-1')
client = session.client('autoscaling')


print("\n Start put scaling policy (add 1 instance):\n")

add_policy_response = client.put_scaling_policy(
    AutoScalingGroupName='chord-asg-sdk-test',
    PolicyName='add_one_instance_scaling_policy',
    PolicyType='SimpleScaling',
    AdjustmentType='ChangeInCapacity',
    ScalingAdjustment=1,
    Cooldown=90,
    Enabled=True
)
print(add_policy_response)

print("\n Start put scaling policy (remove 1 instance):\n")
remove_policy_resposne = client.put_scaling_policy(
    AutoScalingGroupName='chord-asg-sdk-test',
    PolicyName='remove_one_instance_scaling_policy',
    PolicyType='SimpleScaling',
    AdjustmentType='ChangeInCapacity',
    ScalingAdjustment=-1,
    Cooldown=90,
    Enabled=True
)
print(remove_policy_resposne)





session = boto3.Session(region_name='ap-northeast-1')
client = session.client('cloudwatch')


client = session.client('cloudwatch')
print("\nStart put metric alarm (need more disk space): \n")
response = client.put_metric_alarm(
    AlarmName='need_more_disk_space',
    AlarmDescription='alarm if disk avg used percent is above the threshold',
    ActionsEnabled=True,
    AlarmActions=[
        add_policy_response['PolicyARN']
    ],
    EvaluationPeriods=5,
    DatapointsToAlarm=2,
    Threshold=37,
    ComparisonOperator='GreaterThanOrEqualToThreshold', # |'GreaterThanThreshold'|'LessThanThreshold'|'LessThanOrEqualToThreshold'|'LessThanLowerOrGreaterThanUpperThreshold'|'LessThanLowerThreshold'|'GreaterThanUpperThreshold',
    Metrics=[
        {
            'Id': 'disk_avg_query',
            'Expression': "SELECT AVG(disk_used_percent) FROM SCHEMA(CWAgent, AutoScalingGroupName,device,fstype,path) WHERE path = '/' AND AutoScalingGroupName = 'chord-asg-sdk-test'",
            'ReturnData': True,
            'Period': 60
        },
    ],
    Tags=[
        {
            'Key': 'project',
            'Value': 'chord'
        },
    ],
    # ThresholdMetricId='string'
)
print(response)


print("\nStart put metric alarm (need less disk space): \n")
response = client.put_metric_alarm(
    AlarmName='need_less_disk_space',
    AlarmDescription='alarm if disk avg used percent is below the threshold',
    ActionsEnabled=True,
    AlarmActions=[
        remove_policy_resposne['PolicyARN']
    ],
    EvaluationPeriods=5,
    DatapointsToAlarm=2,
    Threshold=30,
    ComparisonOperator='LessThanOrEqualToThreshold', # |'GreaterThanThreshold'|'LessThanThreshold'|'LessThanOrEqualToThreshold'|'LessThanLowerOrGreaterThanUpperThreshold'|'LessThanLowerThreshold'|'GreaterThanUpperThreshold',
    Metrics=[
        {
            'Id': 'disk_avg_query',
            'Expression': "SELECT AVG(disk_used_percent) FROM SCHEMA(CWAgent, AutoScalingGroupName,device,fstype,path) WHERE path = '/' AND AutoScalingGroupName = 'chord-asg-sdk-test'",
            'ReturnData': True,
            'Period': 60
        },
    ],
    Tags=[
        {
            'Key': 'project',
            'Value': 'chord'
        },
    ],
    # ThresholdMetricId='string'
)
print(response)