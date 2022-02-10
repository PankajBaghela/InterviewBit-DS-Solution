class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class linked_list:
    def __init__(self):
        self.head=None
    
    def insert_at_beg(self,val):
        n=node(val)
        n.next=self.head
        self.head=n

    def insert_values(self,datal):
        self.head=None
        for i in datal:
            self.insert_at_last(i)
    
    
    def insert_at_last(self,val):
        n=node(val)
        if self.head is None:
            self.head=n
            return
        
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=n

    #here is the code for the reversing the list
    def reverse_list(self):
        cur=self.head
        prev=None

        while cur:
            tmp=cur.next
            cur.next=prev
            prev=cur
            cur=tmp
        self.head=prev



    def printl(self):
        temp=self.head
        tm=""
        while temp:
            tm+=(str(temp.data)+"-->")
            temp=temp.next
        tm+="None"
        print(tm)

if __name__=="__main__":
    root=linked_list()
    l=[1,2,3,4]
    root.insert_values(l)
    print("before reversing the list")
    root.printl()
    print("after reversing the list")
    root.reverse_list()
    root.printl()