
import boto3

def get_running_instances(filters:[dict]=[]):
    session = boto3.Session(region_name='ap-northeast-1')
    ec2 = session.resource('ec2')
        
    # create filter for instances in running state
    running_filter = [
        {
            'Name': 'instance-state-name', 
            'Values': ['running']
        }
    ]
    filters += running_filter

    # filter the instances based on filters() above
    instances = ec2.instances.filter(Filters=filters)

    return instances

if __name__ == "__main__":
    print("\nPrint the EC2 names from my AWS account\n")
    instances = get_running_instances()

    # instantiate empty array
    RunningInstances = []

    for instance in instances:
        # for each instance, append to array and print instance id
        RunningInstances.append(instance.id)
        print(instance.id, instance.public_ip_address, instance.private_ip_address)
