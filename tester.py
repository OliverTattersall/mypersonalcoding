
class Dog:

    def __init__(self, name, age):
        self.name=name
        self.age=age

lst=[]
joe=Dog("joe", 15)
lst.append(Dog("martha", 12))
print(lst[0].name)

