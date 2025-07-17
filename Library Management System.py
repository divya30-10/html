import time
counter = 100
Books = {}
def add():
    global counter
    counter+=1
    Books[counter]={}
    Books[counter]["name"]=input("Enter Name of Book : ")
    Books[counter]["author"]=input("Enter the author name : ")
    Books[counter]["num"]=input("Enter the no. of book : ")
    print("Books with Name {} added successfully..".format(Books[counter]["name"]))

def view():
    print("Displaying Books:")

    if(len(Books))==0:
        print("No Books Found")
        return
    for i in Books:
        print("ID :",i)
        print("Name: ",Books[i]["name"])
        print("Marks : ",Books[i]["no."])

def update():
    id=int(input("Enter Id of Student : "))
    uc = int(input("1)Update Book Name\n2)Update Book No.\n3)Enter Return Date\n4)Cancle\nEnter Your Choice :")) 
    time.sleep(1)
    if(uc==1):
        Books[counter]["name"]=input("Enter Name of Book : ")
    elif uc==2:
        Books[counter]["marks"]=input("Enter the No. of Book : ")
    elif uc == 3:
        print("Operation Cancelled...")
    else:   
        print("Invalid Choice")
    print("Books with Name {} Updated successfully..".format(Books[counter]["name"]))
    
def delete():
    id=int(input("Enter ID of book : "))
    uc = int(input("Are You Sure ?\n1)Yes \n2)No\nEnter Your Choice :")) 
    time.sleep(1)
    if(uc==1):
       Books.pop(id)
    elif uc==2:
       print("Operation Cancelled...")
    else:
        print("Invalid Choice")
    print("Books  Deleted successfully..")
    



print("************Library Management System************")
time.sleep(1)
print("--------------------------------------------------")

while True:
    uc = int(input("1)Add Book Name\n2)Add Book Name\n3)Update Book\n4)View Book\n5)Exit\nEnter Your Choice :"))
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

