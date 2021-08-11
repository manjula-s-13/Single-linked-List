class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class SingleLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    def Insert_Begin(self,data):
        new_node=Node(data)
        if self.head==None:
            self.head=new_node
            self.tail=new_node
        else:
            new_node.next=self.head
            self.head=new_node
    def Insert_End(self,data):
        new_node=Node(data)
        if self.head==None:
            self.head=new_node
        else:
            self.tail.next=new_node
            self.tail=new_node
    def Display(self):
        temp=self.head
        if (self.head==None):
            print("NO nodes")
        while(temp!=None):
            print(temp.data,"-->",end=" ")
            temp=temp.next
    def Insert_Mid(self,data,index):
        new_node=Node(data)
        temp=self.head
        count=1
        while(temp.next!=None and count<index):
            temp=temp.next
            count+=1
        new_node.next=temp.next
        temp.next=new_node
    def Delete_Begin(self):
        if self.head==None:
            print("NO nodes")
        else:
            self.head=self.head.next
    def Delete_End(self):
        if self.head==None:
            print("NO nodes")
        elif self.head.next==None:
            self.head=None
        else:
            temp=self.head
            while(temp.next.next!=None):
                temp=temp.next
            temp.next=None
    def Delete_Mid(self,index):
        if self.head==None:
            print("NO nodes")
        else:
            temp=self.head
            count=1
            while(temp.next!=None and count<index):
                temp=temp.next
                count+=1
            temp.next=temp.next.next
    def Search(self,data):
        if self.head==None:
            print("NO nodes")
        else:
            temp=self.head
            count=0
            while(temp!=None):
                count+=1
                if(temp.data==data):
                    print(data," found at Position-->",count)
                    return
                temp=temp.next
            print("Element not found")
        
         




