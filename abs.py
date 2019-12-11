class Employe:
    '所有员工的基类'
    emCount = 0
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary
        Employe.emCount += 1

    def displayCount(self):
        print ("total Employee %d" %Employe.emCount)

    def displayEmployee(self):
        print("Name:",self.name)

# em = Employe('lilei',23,1999)
# em2 = Employe('hanmeimei',22,2000)
# # em.displayEmployee()
# # em.displayCount()
# # print(getvattr(em,'age'))
# print ("EMPLOYEE._doc__:",Employe.__doc__)

class justConut:
    __privateCount = 0
    publicCount = 0

    def Count(self):
        self.__privateCount += 1
        self.publicCount +=1
        print(self.__privateCount)

count = justConut()
count.Count()
count.Count()
print(count.publicCount)
print(count.__privateCount)