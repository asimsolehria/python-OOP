class Animal:
    def __init__(self,x):
        self.radius=x


    def area(self):
        return self.radius**3.14
    
 


userInputRadius=int(input("Enter Radius"))
areaObject=Animal(userInputRadius)

print(areaObject.area())