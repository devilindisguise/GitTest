#! /usr/bin/python
# -*- coding:utf-8 -*-

import csv 
import sys


#140624_172716_HP-PC_UE0000_CQIREPORTING_ALL_0001.csv
#140624_172716_HP-PC_UE0000_L1THROUGHPUT_NA_0001.csv
#140624_172716_HP-PC_UE0000_DLL1L2CONTROL_NA_0001

#fisrt numbers as input
logTimeStamp=sys.argv[1]
logL1Thp= logTimeStamp+'_HP-PC_UE0000_L1THROUGHPUT_NA_0001.csv'
LogCqi	= logTimeStamp+'_HP-PC_UE0000_CQIREPORTING_ALL_0001.csv'
LogDlL1L2=  logTimeStamp+'_HP-PC_UE0000_DLL1L2CONTROL_NA_0001.csv'


'''
calculate DCI information

for j in range(0,10):
		with open(arrLogL1[j]) as csvFile:
			reader = csv.reader(csvFile)
			for line in reader:
	 			continue
			print line
			print "The thp. of UE %d is: " %j
			dlBoth=line[4]
			print dlBoth
			dlBothSum =dlBothSum+float(dlBoth)
			
			dlPcc=line[5]
			print dlPcc
			dlPccSum=dlPccSum+float(dlPcc)
			dlScc=line[6]
			print dlScc
			dlSccSum=dlSccSum+float(dlScc)
			ulPcc=line[7]
			print ulPcc
			ulPccSum=ulPccSum+float(ulPcc)
'''

print LogDlL1L2

#with open (LogDlL1L2) as csvFile:
reader = csv.reader(open(LogDlL1L2,'rb'))
for line in reader:
	if (len(line) and line[0]=='0'):
#		if line[0]=='0'):
		print line[0]
	else:	
		continue




'''
arrLogL1=range(0,10)

i=0
arrLogL1[i]=logName
print arrLogL1[i]
i=i+1
arrLogL1[i]=logName.replace('UE0000','UE0001')
print arrLogL1[i]
i=i+1
arrLogL1[i]=logName.replace('UE0000','UE0002')
print arrLogL1[i]
i=i+1
arrLogL1[i]=logName.replace('UE0000','UE0003')
print arrLogL1[i]
i=i+1
arrLogL1[i]=logName.replace('UE0000','UE0004')
print arrLogL1[i]
i=i+1
arrLogL1[i]=logName.replace('UE0000','UE0005')
print arrLogL1[i]
i=i+1
arrLogL1[i]=logName.replace('UE0000','UE0006')
print arrLogL1[i]
i=i+1
arrLogL1[i]=logName.replace('UE0000','UE0007')
print arrLogL1[i]
i=i+1
arrLogL1[i]=logName.replace('UE0000','UE0008')
print arrLogL1[i]
i=i+1
arrLogL1[i]=logName.replace('UE0000','UE0009')
print arrLogL1[i]



dlBothSum=0.0
dlPccSum=0.0
dlSccSum=0.0
ulPccSum=0.0

for j in range(0,10):
		with open(arrLogL1[j]) as csvFile:
			reader = csv.reader(csvFile)
			for line in reader:
	 			continue
			print line
			print "The thp. of UE %d is: " %j
			dlBoth=line[4]
			print dlBoth
			dlBothSum =dlBothSum+float(dlBoth)
			
			dlPcc=line[5]
			print dlPcc
			dlPccSum=dlPccSum+float(dlPcc)
			dlScc=line[6]
			print dlScc
			dlSccSum=dlSccSum+float(dlScc)
			ulPcc=line[7]
			print ulPcc
			ulPccSum=ulPccSum+float(ulPcc)
			
			


print "32UE DL total L1 throughput is: %-10.3f" % dlBothSum
print "32UE DL total PCC L1 throughput is: %-10.3f" % dlPccSum
print "32UE DL total SCC L1 throughput is: %-10.3f" % dlSccSum
print "32UE UL total L1 throughput is: %-10.3f" % ulPccSum

dlAver=dlBothSum/32
print "32UE DL averaged L1 throughput is: %-10.3f" % dlAver

dlAverPcc=dlPccSum/32
print "32UE DL PCC averaged L1 throughput is: %-10.3f" % dlAverPcc

dlAverScc=dlSccSum/32
print "32UE DL SCC averaged L1 throughput is: %-10.3f" % dlAverScc

ulAverPcc=ulPccSum/32
print "32UE UL PCC averaged L1 throughput is: %-10.3f" % ulAverPcc
'''
