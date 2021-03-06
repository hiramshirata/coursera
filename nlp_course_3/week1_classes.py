

class My_class: #definicao
    def __init__(self, y, z):
        self.x_1 = y
        self.x_2 = z

    def __call__(self):
        result = self.x_1 - 2*self.x_2 
        return result

    def my_method(self, w):
        result =  self.x_1*self.x_2 + w
        return result

    def new_method(self, v):
        result = self.my_method(v)
        return result

# subclasses inherit all methods and parameters from it's parent class, including the __init__ and __call__ methods.
# but it can override those inherited methods... 
class sub_c(My_class):
    def additional_method(self):
        print(self.x_1)

instance_e = My_class(1,10)
instance_sub = sub_c(1,2)

print(instance_e.my_method(16))
print(instance_e())
print(instance_e.new_method(2))
instance_sub.additional_method()

