#!/usr/bin/env python3

import myscript4
# Test case 3
# Testing break, breakpoint implementation, and continue_run
print("Test case 3")
myscript4.thing1.setFilePath("/myscript2.py")
myscript4.start()
#myscript4.step()

myscript4.addbreakpoint([22])
myscript4.continue_run()
print(myscript4.thing1.CactusStack.print_tree())
myscript4.quit()
print("should be at linenumber 22 --> e = 5")