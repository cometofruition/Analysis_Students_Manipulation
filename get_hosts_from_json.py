import json
f = open("deploy/deploy1_chall2.json")
d = json.loads(f.read())
for i in d['message']:
    for j in i['deployment']['instances']:
    	print(str(j['floatingip']) + " ansible_connection=ssh ansible_ssh_user=ubuntu ansible_ssh_pass=1") 
 
# Closing file
f.close()
