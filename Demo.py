class Demo :
    def __init__(self):
        print("initiated")
    def oneFun(self):
        print('from onefun')

obj=Demo()
obj.oneFun()
Demo.oneFun(obj)