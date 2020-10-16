# iam-role-no-policies-check
Python script to get IAM roles, last used date and whether it has attached policies or not

It uses python 3.7.4

Make sure you have configured IAM credentials with this permissions:
* iam:GetRole
* iam:ListAttachedRolePolicies
* iam:ListRoles

Run it `python function.py' 

It will generate a csv with the following structure:
,Role name,Last used,Has policies
