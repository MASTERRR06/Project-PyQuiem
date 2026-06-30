class SecondTime:
    def __init__(self,Name:str,age:int):#initializes the class ,ie provides extra info which i WANT TO GIVE FOR THE MACHINE
        self.Name=Name
        self.age=age
        self.now:bool = True
    def now(self):
        if self.now:
            print("ehh nvm"+str(self.Name)+(self.age))
        else:
            self.now = False
            print("ehh nvm"+str(self.Name)+(self.age))

obj=SecondTime("Maira",16)
print(obj.Name)
print(obj.age)
print(obj.now)