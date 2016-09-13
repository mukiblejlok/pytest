#for calculation 
import numpy as np
#for CSV handling
import matplotlib.cbook as cbook
#for ploting
import matplotlib.pyplot as plt
#for PDF generation
from matplotlib.backends.backend_pdf import PdfPages
#for datetime handling
import datetime
import matplotlib.dates as mdates
#for handling files in folder
import os


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
	
	fig, ax = plt.subplots(figsize=(11.7,8.27))
	
	#add plots to figure
	for p in range(nr_val-1):
		ax.plot(date, values[p],colors[p])
	
	#X - label
	#plt.xlabel('Date')
	minutesFmt = mdates.DateFormatter("%b-%d %H:%M")
	ax.xaxis.set_major_formatter(minutesFmt)
	fig.autofmt_xdate()
	#Y - label
	#plt.ylabel('Values')
	
	#title
	plt.title(str(filename.split('\\')[-1]))
	
	#legend
	plt.legend(names)
	
	#return figure object
	print('Printing ' + filename)	
	
	return fig




########################################################3
#Create a Report
ReportName = 'HVACTrends'
try: 
	pdf=PdfPages(ReportName+'.pdf')
except:
	print('Unable to create: ' + ReportName)
	print('Trying to make: ' + ReportName + "_1")
	pdf=PdfPages(ReportName+'_1.pdf')




print('Generating Report: ' + ReportName)

#print a first Page
pdf.savefig(FirstPage())


folder = os.getcwd() + '\data'
#go through files in 'data folder'
toc_list =[]
file_list = os.listdir(folder)
for file in file_list:
	if file.endswith('.csv'):
		#plot figure
		fig=PlotFile(folder + '\\' + str(file))
		#save it to file
		pdf.savefig(fig)
		toc_list.append(str(file))


#print last page
fig=PrintTOC(toc_list)
pdf.savefig(fig)

#close the PDF file
pdf.close()

