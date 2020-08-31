class Node:
    def __init__(self,value):
        self.info=value
        self.link=None
class SingleLinkedList:
    def __init__(self):
        self.start=None

    def displayList(self):
        if self.start is None:
            print("Empty")
        else:
            print("List is :  ")
            p= self.start
            while p is not None:
                print(p.info,"",end="")
                p=p.link
            print()
    def count_nodes(self):
        count=0
        p=self.start
        while p is not None:
            count+=1
        print(count)
    def search(self,x):
        position=1
        p=self.start
        while p is not None:
            if p.info==x:
                print("found ar",position)
            position+=1
            p=p.link
    def insert_in_beg(self,data):
        temp=Node(data)        
        temp.link=self.start
        self.start=temp
    def insert_at_end(self,data):
        temp=Node(data)
        if self.start is None:
            self.start=temp
            return
        p=self.start
        while p.link is not None:
            p=p.link
        p.link=temp

    def createList(self):
        n=int(input("Input the number of nodes"))
        if n==0:
            return
        for i in range(n):
            data=int(input("Enter the number you want to enter"))
            self.insert_at_end(data)

list=SingleLinkedList()
list.createList()
while True:
    print("1.Display list")
    print("2.Count for the number of nodes")
    print("3.Search for an element")
    print("4.Insert a node at the beg")
    print("5.Insert a node at the end")
    # print("")
    # print("")
    # print("")
    # print("")
    # print("")
    # print("")
    # print("")
    option=int(input("ENter your choice"))
    if option==1:
        list.displayList()
    if option==2:
        list.count_nodes()
    if option==3:
        data=int(input("Enter the elments to be searched"))
        list.search(data)
    if option==4:
        data=int(input("Enter the elments to be inserted"))
        list.insert_in_beg(data)
    if option==5:
        data=int(input("Enter the elments to be searched"))
        list.insert_at_end(data)


             



    


        

        


                