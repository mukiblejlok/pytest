
import datetime
import random
import math
import os


#params 
#nr of files
fnr = 10
#length of file
flen = 500
#initial date
inidate = datetime.datetime.now()
sec_jump = 86400 / flen
#value names
names_temp = ['date', 'me', 'sp', 'pos', 'ma']



#clear folder
folder = os.getcwd() + '\data\\'
file_list = os.listdir(folder)
for file in file_list:
	if file.endswith('.csv'):
		#plot figure
		os.remove(folder + file)

#create new files
for i in range(fnr):
	if i < 9: numerator = '0'+str(i+1)
	else: numerator = str(i+1)
	filename = "data\data"+numerator+".csv"
	fhand = open(filename,'w')

	#nr of values
	#nrv = int(random.uniform(2,6))
	nrv = 5
	base_sp = random.uniform(20,24)
	base_pos = random.uniform(50,100)
	val_ma = 1

	#create a file
	for j in range(flen):
		#make a first row with names
		if j==0: 
			for x in range(nrv):
				fhand.write(names_temp[x] + ";")
			fhand.write("\n")

		#create data row
		date = inidate + datetime.timedelta(seconds=(j*sec_jump))
		string = str(date)

		val_me = random.uniform(1.0,1.1) * 0.3*math.sin(j) + base_sp
		val_sp = base_sp
		val_pos = random.uniform(1.0,1.1) * base_pos + 0.2*math.sin(0.4*j)
		val_ma_tmp = 0
		if random.uniform(0,10) >= 9.9:
			if val_ma == 1 and val_ma_tmp == 0: 
				val_ma = 0
				val_ma_tmp = 1
			elif val_ma == 0 and val_ma_tmp == 0: 
				val_ma = 1

		string = string + ";" + str(val_me) + ";" + str(val_sp) +";" + str(val_pos) +";" + str(val_ma)  
		
		fhand.write(string + '\n')





