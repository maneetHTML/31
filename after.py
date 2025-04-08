class Stringr:
    def __init__(self,string):
        self.string=string
    def String(self):
       return self.string[::-1]
obj = Stringr("Maneet is the best.")
obj2 = obj.String()
print(obj2)