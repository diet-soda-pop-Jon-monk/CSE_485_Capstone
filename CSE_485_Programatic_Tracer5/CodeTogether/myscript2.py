a = 0
def fun():
    print("got here")
    a = 3.56235
    b = 2.5
    c = a + b
    d = thing1()
    print(a)
    return "GFG"

def thing1():
    a = 1+2
    checka()
    # global trace function is invoked here and
    return a
# global trace function is invoked here and
# local trace function is set for check()
def checka():
    a = 4

def check():
    e = 5
    for_loop()
    t = 12
    d = 123
    fun()
    y = 145
    checka()
    recursion()
    return fun()

def recursion(n=5):
    if(n > 1):
        return recursion(n-1)
    else:
        return n-1

def for_loop():
    for i in range(0, 5):
        print(i)
    return

for i in range(0, 3):
    print(i)
a=12
check()
fun()
a = 2
a = 3.2
a = 3.5