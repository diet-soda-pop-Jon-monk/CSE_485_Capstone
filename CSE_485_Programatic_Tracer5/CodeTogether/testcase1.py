#!/usr/bin/env python3
import hoare_logic
#import tracer
import myscript5_r
import os
from pathlib import Path

'''
Test case 1
steps into myscript5.py and then shows cactus stack
'''

def checkfile(directory, filename, conditions):
    #print("directory being checked is: ", directory)
    #print("filename being checked is: ", filename)
    #print("conditions file is ", conditions)
    fname = os.path.join(directory, filename)
    #print("fname is ", fname)
    cname = os.path.join(directory, conditions)
    #print("cname is", cname)

    tracer = myscript5_r.Python_tracer()
    print("myscript filename is ", tracer.filepath)
    #tracer.setFilePath("/target.py")
    #print("testcase1 returned from tracer init")
    print(tracer.filepath)
    tracer.setFilePath(os.path.join(directory, filename))
    #print("tracer file path is ", tracer.filepath)
    tracer.start()

    for i in range(18):
        tracer.step()

    tracer.continueRun()
#print("line is " + str(tracer.curFrame.f_lineno))
#print("tracer step ", tracer.CactusStack.print_frame())
#print("tracer step vars ", tracer.CactusStack.current_frame.vars)
#tracer.step()
#tracer.stepover()
    tracer.quit()
    saveStack = tracer.CactusStack
    print("\nCactusStack is ")
    print(tracer.CactusStack.print_tree())
    print("saved CactusStack is ")
    print(saveStack.print_tree())
    return

print("Test case 1")
pythonfilesChecked = 0
conditionsFile = input("Enter the conditions text file: ")
print("Conditions files is: ", conditionsFile)
directory = input("Enter path to directory to process: ")
print("directory is", directory)
for f_name in os.listdir(directory):
    if f_name.endswith('.py'):
        pythonfilesChecked += 1
        filetocheck = os.path.join(directory, f_name)
        #print("file to check is: ", f_name)
        #print("file name is: ", filetocheck)
        checkfile(directory, f_name, conditionsFile)

print("Checked ", pythonfilesChecked, "python files")
print("Test case 1 end")