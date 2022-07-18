import pandas as pd

# Load the CSV into a DataFrame
df = pd.read_csv("output/Statistical_Table.csv")

# Commands from user
check = df.groupby('User')

user_ip = []
user_command = []

# Get user_ip and user_command
for User, group in check:
	user_ip.append(User)
	df = group['Command'].tolist()
	user_command.append(df)
	
# default solution	
model = ["binwalk -e dolls.jpg",
"binwalk -e 2_c.jpg",
"binwalk -e 3_c.jpg",
"binwalk -e 4_c.jpg",
"cat flag.txt"]

def Check_User_Command(command):

	indexCmd = 0
	flag = 0
	for modelCmd in model:
		for checkCmd in command:
			if (checkCmd == modelCmd and command.index(checkCmd) >= indexCmd):
				#print(check.index(checkCmd))
				indexCmd = command.index(checkCmd)
				flag = 1
				break
		if flag == 0:
			return False
		flag = 0
	return True

for i in range(len(user_ip)):
	if Check_User_Command(user_command[i]):
		print('%s Passed' % user_ip[i])
	else:
		print('%s Failed' % user_ip[i])
