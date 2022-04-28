class A:
    def fun1(self):
        print('feature_1 of class A')
    def fun2(self):
        print('feature_2 of class A')

class B(A):
    #modified function that is already exist in class A
    def fun1(self):
        print('Modified feature_1 of class A by class B')
    def fun2(self):
        print('feature_3 of class B')

#create instance
obj = B()

#call the override function
obj.fun1()