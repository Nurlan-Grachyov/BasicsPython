class Descriptor:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        return instance.__dict__[self.name] == value

    def __delete__(self, instance):
        del instance.__dict__[self.name]


des = Descriptor("Nurlan")
print(des.name)
del des.name
print(des.name)
