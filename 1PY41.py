class student:
    def __init__(self,rollno,name,course,mark1,mark2):
        self.rollno_41=rollno
        self.name_41=name
        self.course_41=course
        self.mark1_41=mark1
        self.mark2_41=mark2
    def sum(self):
        tmark_41=0
        self.tmark_41=self.mark1_41+self.mark2_41
    def display(self):
        print("Roll No=",self.rollno_41,"\nName=",self.name_41,"\nCourse=",self.course_41)
        print("Mark1=",self.mark1_41,"\nMark2=",self.mark2_41,"\nTotal marks=",self.tmark_41)
print("\nStudent 1:")
ob=student(11,'Manu','MCA',19,18)
ob.sum()
ob.display()
print("\nStudent 2:")
ob1=student(12,'Anu','MCA',15,17)
ob1.sum()
ob1.display()
print("\nStudent 3:")
ob2=student(15,'Sonu','MCA',20,16)
ob2.sum()
ob2.display()
