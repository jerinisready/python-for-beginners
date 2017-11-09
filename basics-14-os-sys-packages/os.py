#!/usr/bin/python

import os, sys, stat, subprocess

#Create a folder in the current directory
os.mkdir('example')

#Create a python file in the newly created folder
fp = open("example/sum.py","w+")

#Writing a list of lines into the file
lines_of_text = ["a=5","\n", "b=10","\n", "sum=a+b","\n", "print(sum)"]
fp.writelines(lines_of_text)

fp.close()  #close the file

#Change permission
st = os.stat('example/sum.py')
os.chmod('example/sum.py', st.st_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)

print("=========================================")
print("Contents in the file sum.py\n")
fp = open("example/sum.py","r+")
print fp.read()
fp.close()
print("=========================================")

#Executing display.py 
print("\nResult :")
os.system('python example/sum.py')
print("\nSuccess!!\n")


