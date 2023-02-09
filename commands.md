# chord
sudo yum install git -y  
sudo yum install tmux  
git clone https://github.com/BOBO-LU/chord.git  
cd chord
python3 utils.py 1 10 100 # generate dummy files  



# cloudwatch monitor disk usage
### https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/install-CloudWatch-Agent-on-EC2-Instance-fleet.html#start-CloudWatch-Agent-EC2-fleet
### https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/create-cloudwatch-agent-configuration-file-wizard.html
### https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Agent-Configuration-File-Details.html
sudo yum install amazon-cloudwatch-agent -y   
sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-config-wizard  
sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl -a fetch-config -m ec2 -s -c file:/opt/aws/amazon-cloudwatch-agent/bin/config.json  
sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl -a fetch-config -m ec2 -s -c file:/home/ec2-user/chord/config/config.json  
aws ssm put-parameter --region ap-northeast-1 --name AmazonCloudWatch-linux --type String --value file:~/chord/config/config.json --overwrite  

# cloudwatch verification
sudo yum install telnet -y   
telnet monitoring.ap-northeast-1.amazonaws.com 443  


# boto3
sudo yum install -y python3-pip python3 python3-setuptools -y  
pip3 install boto3 pytz pyyaml  
aws sts get-caller-identity  


# start chord
python3 Node.py 

# setup asg and as
## https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scaling-simple-step.html
## https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_PutMetricAlarm.html
python3 create_asg.py  
python3 create_scaling_policy.py  

# launch ec2
yum install cloud-init  
chmod 777 /home/ec2-user/chord/startup.sh  
## check userdata
cat /tmp/testfile.txt  
sudo cat /var/log/cloud-init-output.log  
## set user-template version
aws ec2 modify-launch-template --launch-template-id "lt-036e6da40dea7e53c" --default-version "9" --region "ap-northeast-1"  


# TODO:
- change sg ip to coresponding sg in asg
- asg describe / ec2 describe script => to get ip
- cloudwatch agent install script
- run ssm in auto scaling group -> tag association # https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-state-manager-asg.html
! loading time difference 

# steps:
Finish：
- write chord  (clone others)
- test chord locally
- create security group
- create IAM
- create 2 EC2
- test socket connection between two EC2
- test chord on EC2
- launch cloudwatch agent wizard
- modify agent config
- upload config to parameter store
- start cloudwatch agent
- test connection with cloudwatch
- use systems manager agent to start cloudwatch agent on all instance
- check cloudwatch metrics
- test alarm
- prepare ec2 start script (user_data) & chord start script
- create ec2 AMI
- create launch template
- create auto scaling group
- create scaling policy
- create cloud watch metric alarm and attach it to scaling policy


TODO:
- write a client to connect nodes in auto scaling group
- upload/download files
- test auto scaling
- finish chord deployment!! 
