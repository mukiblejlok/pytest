#import xml parser
import xml.etree.ElementTree as ET
##classes to work with excel
#from openpyxl import Workbook
from openpyxl import load_workbook
import warnings 
import os


warnings.filterwarnings("ignore") 


######################################################3
#Read Data from XLS
def ReadXLS(filename):

	wb = load_workbook(filename, data_only=True)
	ws = wb.active

	data = dict()
	names = [col.value for col in ws.rows[0]]

	row_nr=0	
	for row in ws.rows[1:]:
		key1 = str(row[1].value)
		key2 = str(row[2].value)
		key3 = str(row[3].value)
		val = str(row[0].value)

		if not key1 in data: data[key1] = dict()
		if not key2 in data[key1]: data[key1][key2] = dict()
		if not key3 in data[key1][key2]: data[key1][key2][key3] = list()

		data[key1][key2][key3].append(str(val))
		row_nr += 1


	#close workbook
	
	print('Retrieved: ' + str(row_nr) + ' rows'
		 +' from: ' + filename)
	#print(data_dict['TAG'])
	return names, data		


#######
##Make XML
def MakeXML(file, tags, prints):
	#Header
	fheader = open(os.getcwd() + '\\templates\\header.xml').read()
	fh = open(os.getcwd() + '\\results\\' + file, 'w')
	
	for idx,elem in enumerate(prints):
		#print("writing")
		fh.write(str(elem) + "\n")
	
	fh.close()
	print("File: " + file + " created " + str(idx) + " lines.")




#################################################################################3
#############
#1. Read XLS
print('==Part 1 Read input XLSX')
names, data = ReadXLS('input_data.xlsx')

###########
#2. Prepare results folder
print('==Part 2 Prepare \'results\' folder')
folder = os.getcwd() + '\\results\\'
file_list = os.listdir(folder)
for file in file_list:
	if file.endswith('.xml'):
		#plot figure
		os.remove(folder + file) 
print('Done!')
#####################################
#2. Make Files
print('==Part 3 Create Files')
max_nelem = 20

for lev1 in data:
	for lev2 in data[lev1]:
		#Initialize counter of pages
		part = 1
		nelem = 0
		tag_list = []
		print_list = []
		for lev3 in data[lev1][lev2]:

			divider = ('---' + lev3)
			print_list.append(divider)
			
			for tag in data[lev1][lev2][lev3]:
				#do some stuff with tags
				tag_list.append(tag)
				print_list.append(tag)
				nelem += 1 
				#check if max reached
				
				if nelem>=max_nelem : 

					####Make an XML
					file_name = "gd_B1_" + str(lev1) + "_MFZ" + str(lev2) +  "_" + str(part) + ".xml"
					MakeXML(file_name, tag_list, print_list)
					nelem = 0
					part += 1
					tag_list = []
					print_list = []
					print_list.append(divider) 
		if nelem > 0 :
			file_name = "gd_B1_" + str(lev1) + "_MFZ" + str(lev2) +  "_" + str(part) + ".xml"
			MakeXML(file_name, tag_list, print_list)
			


		



