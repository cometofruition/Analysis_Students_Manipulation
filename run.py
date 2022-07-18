import os
import re
import threading
import json
import csv
from datetime import datetime
from subprocess import Popen, PIPE

# Folder Path
path = "/home/r3ckl3ss/Desktop/Analysis_Students_Manipulation/output"

if not os.path.exists(path):
	os.mkdir(path)

	
print('Choose: 1: Clean history cache and set \n\t DateTime 2: Get Log')
choose = input()

if choose == '1':
	args = ["ansible-playbook", "-b", "-v", "Setup.yml", "--extra-var", "\"crunchify-group\"", "-i", "crunchify-hosts"]
	Setup = Popen(args, stdin=PIPE, stdout=PIPE, stderr=PIPE)
	output = Setup.communicate()
	print(output)

if choose == '2':
	args = ["ansible-playbook", "-b", "-v", "Check_History.yml", "--extra-var", "\"crunchify-group\"", "-i", "crunchify-hosts"]         
	Check_History = Popen(args, stdin=PIPE, stdout=PIPE, stderr=PIPE)
	output = Check_History.communicate()
	print(output)
	
	# Change the directory
	#os.chdir(path)

	# data rows of csv file
	time = ""
	rows = []
	user = ""
	
	# field name
	fields = ['User', 'Time', 'Working Directory', 'Command', 'Duration']
	Sum = []
	file_path = os.getcwd()

	# iterate through all file
	for file in os.listdir(path):
	# Check whether file is in text format or not
		if file.endswith(".txt"):
			file_path = f"{path}/{file}"
			user = file.split('.txt')[0]

			# call read text file function
			f = open(file_path, 'r')
			data = json.loads(f.read())
			
			dt_object = datetime.fromtimestamp(int(data[0].split(" - ")[0]))
			sumDuration = dt_object - dt_object # sum of duration
			countDict = {}
			
			for item in data:
				line = item.split(" - ")
				try:
					countDict[line[2].split(" ")[0]] += 1
				except:
					countDict[line[2].split(" ")[0]] = 1
				time = line[0]
				timestamp = int(time)
				new_dt_object = datetime.fromtimestamp(timestamp)
				duration = new_dt_object - dt_object
				sumDuration += duration
				dt_object = new_dt_object
				line[0] = dt_object
				line.append(duration)
			
				line.insert(0, user)
				rows.append(line)
			
			with open(f'{path}/Statistical_Table.csv', 'w') as f:

				# using csv.writer method from CSV package
				write = csv.writer(f)

				write.writerow(fields)
				write.writerows(rows)
					
	"""Sum.append(['Sum %s' % user, sumDuration])
				
			with open(f'{path}/Statistical_Table.csv', 'a') as f:

				# using csv.writer method from CSV package
				write = csv.writer(f)
				write.writerows(Sum)"""
