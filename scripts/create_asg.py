
"""
* need to create LaunchTemplate first: https://docs.aws.amazon.com/autoscaling/ec2/userguide/create-launch-template.html

possible funcitons:
create_auto_scaling_group
create_

describe_auto_scaling_groups
describe_auto_scaling_instances

put_scaling_policy


"""

import boto3

session = boto3.Session(region_name='ap-northeast-1')
client = session.client('autoscaling')

print("\nStart creat auto scaling group: \n")
response = client.create_auto_scaling_group(
    AutoScalingGroupName='chord-asg-sdk-test',
    # LaunchConfigurationName='string',
    LaunchTemplate={
        'LaunchTemplateId': 'lt-036e6da40dea7e53c',
        # 'LaunchTemplateName': 'chord-ami-lauch-template',
        'Version': '$Latest'
    },
    # InstanceId='string',
    MinSize=1,
    MaxSize=3,
    DesiredCapacity=1,
    DefaultCooldown=30,
    AvailabilityZones=[
        'ap-northeast-1d',
    ],
    # LoadBalancerNames=[
    #     'string',
    # ],
    # TargetGroupARNs=[
    #     'string',
    # ],
    # HealthCheckType='string',
    # HealthCheckGracePeriod=123,
    # PlacementGroup='string',
    VPCZoneIdentifier='subnet-032777a8d3278e987',
    TerminationPolicies=[
        'Default',
    ],
    NewInstancesProtectedFromScaleIn= False,
    CapacityRebalance= False,
    # LifecycleHookSpecificationList=[
    #     {
    #         'LifecycleHookName': 'string',
    #         'LifecycleTransition': 'string',
    #         'NotificationMetadata': 'string',
    #         'HeartbeatTimeout': 123,
    #         'DefaultResult': 'string',
    #         'NotificationTargetARN': 'string',
    #         'RoleARN': 'string'
    #     },
    # ],
    Tags=[
        {
            'ResourceId': 'chord-asg-sdk-test',
            'ResourceType': 'auto-scaling-group',
            'Key': 'project',
            'Value': 'chord',
            'PropagateAtLaunch': True
        },
    ],
    # ServiceLinkedRoleARN='string',
    # MaxInstanceLifetime=123,
    # Context='string',
    DesiredCapacityType='units',
    DefaultInstanceWarmup=30,
    # TrafficSources=[
    #     {
    #         'Identifier': 'string'
    #     },
    # ]
)
print(response)