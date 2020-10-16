# iam-role-no-policies-check
Python script to get IAM roles, last used date and whether it has attached policies or not

It uses python 3.7.4

Make sure you have configured IAM credentials in your workstation with enough permissions to invoke the APIs in the code. 

Run it `python function.py' 

It will generate a csv with the following structure:
,Role name,Last used,Has policies
