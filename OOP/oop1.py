# Object Orienter Programming

# Classess and Instances
class student:
    def __init__(self,first,last,rollno):
        self.first=first
        self.last=last
        self.rollno=rollno

    def fullname(self):
        print('{} {}'.format(self.first,self.last))

    def mail_id(self):
            roll=[]
            for i in self.rollno:
                roll.append(i)
            r = roll[8:12]
            r=''.join(r)
            mailid=self.first + r + '@gmail.com'
            print(mailid)


stu1=student(r'Erlich','Bachman','17094523011')
stu2=student('Jian','Yang','17094523007')

stu1.fullname()
stu1.mail_id()
print()
stu2.fullname()
stu2.mail_id()