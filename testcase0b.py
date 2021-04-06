#!/usr/bin/env python3
import hoare_logic
#import tracer
import myscript5_r as myscript5
import ast_code

'''
Test case 0 
15 steps into myscript2.py and then quit
'''
print("Test case 0")

tracer = myscript5.Python_tracer()
tracer.setFilePath("c:/..use full file path.../target.py")
tracer.start()

#Testing stepover

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
print("Test case 0 end")

ast_tree = ast_code.CustomVisitor(tracer.filepath)
ast_tree.print_tree(ast_tree.root)