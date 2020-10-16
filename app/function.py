import boto3
import pandas as pd 

clientIam = boto3.client('iam')
roles = []
lastUses = []
policies = []

response = clientIam.list_roles()

while True:
    for i in response['Roles']:
        role = clientIam.get_role(RoleName=i['RoleName'])['Role']
        if role['RoleLastUsed']:
            roles.append(role['RoleName'])
            lastUses.append(str(role['RoleLastUsed']['LastUsedDate']))
        else:
            roles.append(role['RoleName'])
            lastUses.append('Never used')
        attachedPolicies=clientIam.list_attached_role_policies(RoleName=i['RoleName'], MaxItems=1)
        if attachedPolicies['AttachedPolicies']:
            policies.append('yes')
        else:
            policies.append('no')
    if "Marker" in response:
        response = clientIam.list_roles(Marker=response['Marker'])
        continue
    else:
        break

dict={'Role name': roles, 'Last used':lastUses, 'Has policies':policies}
df = pd.DataFrame(dict) 
df.to_csv('file1.csv') 