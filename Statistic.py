import pandas as pd
from dateutil import parser
from datetime import date

# Load the CSV into a DataFrame
df = pd.read_csv("output/sandbox-123-useractions.csv")

# Commands from user
check = df.groupby('ip')

user_ip = []
user_command = []
time_stamp = []
countDict = {}

# Get user_ip and user_command
for User, group in check:
	user_ip.append(User)
	df = group['cmd'].tolist()
	user_command.append(df)
	time = group['timestamp_str'].tolist()
	time_stamp.append(time)
"""
# default solution	
keywords = ["file", "strings", "binwalk", "foremost", "cd", "cat"]

def Check_User_Valid_Cmd(command):

	valid_cmd = []
	for checkCmd in command:
		if list(set(keywords).intersection(checkCmd.split())):
			valid_cmd.append(checkCmd)
	return valid_cmd"""
	
def Sum_Completion_Time(time):

	Sum = date.today() - date.today()
	for i in range(len(time)-1):
		date1 = parser.parse(time[i])
		date2 = parser.parse(time[i+1])

		diff = date2 - date1
		Sum += diff
	return Sum

def Count_Dict(command):

	for line in command:
		try:
			countDict[line.split(" ")[0]] += 1
		except:
			countDict[line.split(" ")[0]] = 1
	return countDict
	
def Sum_User_Command(command):

	count = 0

	for i in command:
		count += 1
	return count
	
"""def changed_options(current, prev):
	return current.program == prev.program and current.options and current.options != prev.options
	
def count_option_changes(commands):
	option_changes = 0
	for i in range(0, len(commands) - 1):
		if changed_options(commands[i], commands[i+1]):
			option_changes += 1
	return option_changes"""

for i in range(len(user_ip)):
	print("- %s:" % user_ip[i])
	print("\t+ Sum of User Command: %d" % Sum_User_Command(user_command[i]))
	print("\t+ Total completion time: ", Sum_Completion_Time(time_stamp[i]))
	print("\t+ Average Delays: ", Sum_Completion_Time(time_stamp[i])/(len(time_stamp[i])-1))
	print("\t+ Count dictionary: ", Count_Dict(user_command[i]))
	#print("Valid Commands: %s" % Check_User_Valid_Cmd(user_command[i]))
	print()
