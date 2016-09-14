#for calculation 
import numpy as np
#for CSV handling
import matplotlib.cbook as cbook
#for ploting
import matplotlib.pyplot as plt
#for datetime handling
import datetime
import matplotlib.dates as mdates

###################################
#  Report generation
#  functions
#
#####################################

#======================
def FirstPage():
	#Create a figure
	fig = plt.figure(figsize=(11.7,8.27))
	#with no axes
	plt.axis('off')
	
	#add some text
	text = 'HVAC Trends Report'
	plt.text(0.4,0.5,text,fontsize=20)
	text = 'from 2016-09-12'
	plt.text(0.4,0.45,text,fontsize=15)
	text = 'by Valmet Automation Report'
	plt.text(0.4,0.40,text,fontsize=15)
	
	print("Priniting first page")
	return fig

##########################################################
def PrintTOC(list,nelem=20):
	
	fig=plt.figure(figsize=(11.7,8.27))
	nr_tof = len(list)
	plt.text(0, 1,"Table of contents: ",fontsize=20)

	for i in range(nr_tof):
		xpos = 0.5 * int((i+1)/nelem)
		ypos = 0.9 - 0.05 * ((i) % (nelem-1))
		text = str(i+1) + ". " + list[i] 
		plt.text(xpos,ypos,text,fontsize=10)
	plt.axis('off')
	
	print("Priniting TOC")
	return fig

#########################################################
def PlotFile(filename):
	#define data table
	date = []
	#define values
	values = []
	#colors
	colors = ['r-', 'g-', 'b-', 'k-', 'y-']


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
		#strip row
		val = line.strip().split(';')
		#first column is a datetime
		#so read it like it is
		date.append(datetime.datetime.strptime(val[0], "%Y-%m-%d %H:%M:%S.%f"))
		#read following elements in row
		for i in range(nr_val-1):
			values[i].append(float(val[i+1]))

	##############
	#make a plot
	
	fig, ax = plt.subplots(3, sharex=True, figsize=(11.7,8.27))

	#title
	
	#add plots to figure
	#for p in range(nr_val-1):
	#	ax.plot(date, values[p],colors[p])
	ax[0].plot(date, values[0], colors[0])
	ax[0].plot(date, values[1], colors[1])
	ax[0].set_title(str(filename.split('\\')[-1]))
	ax[0].set_ylabel('Meas. and SP')
	ax[0].set_ylim([15, 30])
	ax[0].legend(['Temp.', 'SP'])

	#ax[0].set_legend(names[:2])
	
	ax[1].plot(date, values[2], colors[2])
	ax[1].set_ylabel('Control')
	
	ax[2].fill_between(date, 0, values[3], hatch='x', edgecolor='k')
	ax[2].set_ylabel('Auto Mode')
	
	


	#X - label
	#plt.xlabel('Date')
	minutesFmt = mdates.DateFormatter("%b-%d %H:%M")
	ax[0].xaxis.set_major_formatter(minutesFmt)
	fig.autofmt_xdate()
	#Y - label
	#plt.ylabel('Values')
	
	
	
	
	
	#return figure object
	print('Printing ' + filename)	
	
	return fig


