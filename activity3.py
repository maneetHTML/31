class computer:
    def __init__(self):
        self.__price=900
    def sell (self):
        print("computer price : ", self.__price)
    def newprice (self):
        self.__price=1000

obj=computer()
obj.sell()
# obj.__price=1500
# obj.sell() : print 900
obj.newprice()
obj.sell()