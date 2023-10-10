
import boto3

aws_management_console = boto3.session.Session(profile_name="default")

ec2_console = aws_management_console.client("ec2")

response = ec2_console.run_instances(
    ImageId = 'ami-065680f8cbec51c69',
    InstanceType= 't2.micro',
    MaxCount=1,
    MinCount=1
)