class Student:
    def __init__ (self):
        self.name=name
        self.enroll=enroll
        
    def set_marks(self,mark1,mark2,mark3):
        self.mark1=mark1
        self.mark2=mark2
        self.mark3=mark3
        
    def get_marks(self,mark1,mark2,mark3):
        return self.mark1,self.mark2,self.mark3
    
    def result(self):
        self.total=self.mark1+self.mark2+self.mark3
        
    def show(self):
        print(self.total)
while True:
    name=input("enter name of student")
    enroll=int(input("enter student enrollment id"))
    att=int(input("enter students attendance"))
    if att>70:
        print("student has permission to sit in exam")
        mark1=int(input("enter mark in first subject"))
        mark2=int(input("enter mark in second subject"))
        mark3=int(input("enter mark in third subject"))
        total=mark1+mark2+mark3
        print("total marks obtained in three subject:",total)
        if total>=60:  
            print("secured A grade")
        elif total>=50:
            print("secured B grad")
        elif total>=35:
            print("secured C grade")
    else:
        print("student has no permission to sit in exam")
    quit = input("Do you want to continue (y/n) ?")
    if quit == 'n':
        break
    
t=Student()
p=t.set_marks(mark1,mark2,mark3)
t1=t.get_marks(mark1,mark2,mark3)
r=t.result()


    
        
        
        


