import time
counter = 100
Students = {}
def add():
    global counter
    counter+=1
    Students[counter]={}
    Students[counter]["name"]=input("Enter Name of Student : ")
    Students[counter]["marks"]=input("Enter the Marks of Student : ")
    print("Student with Name {} added successfully..".format(Students[counter]["name"]))

def view():
    print("Displaying Students:")

    if(len(Students)==0):
        print("No Students Found")
        return
    for i in Students:
        print("ID :",i)
        print("Name: ",Students[i]["name"])
        print("Marks : ",Students[i]["marks"])

def update():
    id=int(input("Enter Id of Student : "))
    uc = int(input("1)Update Name\n2)Update Marks\n3)Cancle\nEnter Your Choice :")) 
    time.sleep(1)
    if(uc==1):
        Students[counter]["name"]=input("Enter Name of Student : ")
    elif uc==2:
        Students[counter]["marks"]=input("Enter the Marks of Student : ")
    elif uc == 3:
        print("Operation Cancelled...")
    else:
        print("Invalid Choice")
    print("Student with Name {} Updated successfully..".format(Students[counter]["name"]))
    
def delete():
    id=int(input("Enter Id of Student : "))
    uc = int(input("Are You Sure ?\n1)Yes \n2)No\nEnter Your Choice :")) 
    time.sleep(1)
    name = Students[counter]["name"]
    if(uc==1):
       Students.pop(id)
    elif uc==2:
       print("Operation Cancelled...")
    else:
        print("Invalid Choice")
    print("Student with Name {} Deleted successfully..".format(name))
    



print("************Student Management System************")
time.sleep(1)
print("--------------------------------------------------")

while True:
    uc = int(input("1)Add New Student\n2)View Students\n3)Update Student\n4)Delete Student\n5)Exit\nEnter Your Choice :"))
    time.sleep(1)
    if(uc==1):
        add()
    elif uc==2:
        view()
    elif uc==3:
        update()
    elif uc==4:
        delete()
    elif uc==5:
        print("--------------------------------------------------")
        print("Thank You")
        print("--------------------------------------------------")

        break
    else:
        print("Invalid Choice")
    
    print("--------------------------------------------------")
