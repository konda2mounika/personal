# Import all the modules and Libraries
import boto3
# Open Management Console
aws_management_console = boto3.session.Session(profile_name="default")
# Open IAM Console
iam_console = aws_managament_console.client(service_name="iam")
# Use Boto3 Documentation to get more information (https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
result =iam_console.list_users()
print(result)