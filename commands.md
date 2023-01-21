# chord
sudo yum install git -y
sudo yum install tmux
git clone https://github.com/BOBO-LU/chord.git
python3 utils.py 1 10 100 # generate dummy files
python3 Node.py # start chord node


# cloudwatch monitor disk usage
## https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/install-CloudWatch-Agent-on-EC2-Instance-fleet.html#start-CloudWatch-Agent-EC2-fleet
## https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/create-cloudwatch-agent-configuration-file-wizard.html
## https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Agent-Configuration-File-Details.html
sudo yum install amazon-cloudwatch-agent -y
sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-config-wizard
sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl -a fetch-config -m ec2 -s -c file:/opt/aws/amazon-cloudwatch-agent/bin/config.json

# cloudwatch verification
sudo yum install telnet -y
telnet monitoring.ap-northeast-1.amazonaws.com 443


# boto3
sudo yum install -y python3-pip python3 python3-setuptools -y
pip3 install boto3
aws sts get-caller-identity

# setup asg and as
## https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scaling-simple-step.html
## https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_PutMetricAlarm.html


# TODO:
- change sg ip to coresponding sg
- asg describe / ec2 describe script => to get ip
- cloudwatch agent install script
- lambda agg metrics ?
- run ssm in auto scaling group -> tag association # https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-state-manager-asg.html
! loading time difference 

# steps:
Finish：
- write chord
- test chord locally
- create sg
- create iam
- create 2 ec2
- test socket connection between two ec2
- test chord on ec2
- launch cw agent wizard
- modify agent config
- upload config to parameter store
- start cw agent
- test connection with cw
- use ssm to start cw agent on all instance
- check cw metrics
- test alarm

TODO:
- prepare ec2 start script & chord start script
- create ec2 AMI
- create launch template
- create asg
- create scaling policy
- create metric alarm and attach to policy
- finish !!