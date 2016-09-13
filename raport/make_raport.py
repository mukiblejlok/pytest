#for handling files in folder
import os
from matplotlib.backends.backend_pdf import PdfPages

from report_functions import *

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


#####
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


