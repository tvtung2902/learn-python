x = "tran"
def myfunc():
    x = "van"
    print("x =", x)
myfunc()
print("x =", x)

def myfunc1():
    global x1 
    x1 = "tung"
myfunc1()
print("global x1 =", x1)


x2 = "awesome"

def myfunc():
  global x2
  x2 = "fantastic"

myfunc()

print("Python is " + x2)
