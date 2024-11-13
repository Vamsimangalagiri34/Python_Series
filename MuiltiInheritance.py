class A:#not supported in java
    def __init__(self):
        print("status: initiated from A")
    
    def oneFun(self):
        return 3

class B:
    def __init__(self):
        print("status: initiated from B")
    
    def twoFun(self):
        return 4

class C(A, B):
    def __init__(self):
        # Initialize both base classes
        super().__init__()
    
    def calculate_sum(self):
        # Call the methods from both A and B
        return self.oneFun() + self.twoFun()

# Creating an instance of C
c_instance = C()
result = c_instance.calculate_sum()
print("Result:", result)
