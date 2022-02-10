class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linked_list:
    def __init__(self):
        self.head=None

    def insert_at_last(self,val):
        n=node(val)
        if self.head is None:
            self.head=n
            return
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=n


    def insert_values(self,datalist):
        self.head=None
        for i in datalist:
            self.insert_at_last(i)

    def print_ls(self):
        temp=self.head
        tm=""
        while temp:
            tm+=str(temp.data)+"-->"
            temp=temp.next
        tm+="None"
        print(tm)

    # main method for reverse linked list in k group
    def revers_in_k_group(self,B):
        A=self.head
        dummy=tail=node(0)
        dummy.next=A
        cur=A
        
        while cur:
            prev=None
            next_ele=None
            tail2=cur
            k=B
            while cur and k:
                k-=1
                next_ele=cur.next
                cur.next=prev
                prev=cur
                cur=next_ele
            tail.next=prev
            tail=tail2
        self.head=dummy.next


if __name__=="__main__":
    root=linked_list()
    l=[1,2,3,4,5]
    root.insert_values(l)
    root.revers_in_k_group(3)
    root.print_ls()