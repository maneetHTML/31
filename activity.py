class student:
    __school="abc school" #school is a private variable
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display (self):
        print("The age and name are :",self.name,self.age)
    def schdi (self):
        print("the school name : ", self. __school)
    
obj=student("maneet",8)
obj.display ()
obj.schdi ()
# print ("school name",obj.school)