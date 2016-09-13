import matplotlib.pyplot as plt
import datetime


def PlotFile(filename):
	#define data table
	date = []
	#define values
	values = []

	#open file
	fh = open(filename, 'r')
	#read first line and get the names
	names = fh.readline().rstrip().split(';')
	#remove last element because it is empty
	del names[-1]
	nr_val = len(names)

	#initialize an values list of list
	for i in range(nr_val):
		values.append([])

	#read file and fill the lists
	for line in fh:
		val = line.strip().split(';')
		date.append(datetime.datetime.strptime(val[0], "%Y-%m-%d %H:%M:%S.%f"))
		for i in range(nr_val-1):
			values[i].append(float(val[i+1]))

	#print(names)
	#print(date)
	#print(values)
	fig=plt.figure(figsize=(11.7,8.27))
	plt.plot(date,values[1])
	plt.xlabel('Date & Time')
	plt.ylabel('Values')
	plt.title('Interesting Graph\nCheck it out')
	plt.legend()
	
	return fig



