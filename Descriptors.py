class descriptor(object):
    def __init__(self,name="") -> None:
     self.name=name
    def __get__(self,obj,objtype):
        return "{}".format(self.name)
    def __set__(self,obj,name):
        if isinstance(name,str):
            self.name=name
        else:
            raise TypeError("Name should be String")
class ABC(object):
    name=descriptor()
obj=ABC()
obj.name="Sampath Kumar"
print(obj.name)