print(bool(111))
#false
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

class myclass():
  def __len__(self):
    return False

myobj = myclass()
print(bool(myobj))

def myFunc() :
  return 1
if myFunc():
    print("ok")
else: print("ko ok")

x = 200
print(isinstance(x, int))