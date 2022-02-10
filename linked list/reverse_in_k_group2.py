class linked_node:
    def __init__(self,data):
        self.data=data
        self.next=None

class linked_list:
    def __init__(self):
        self.head=None

    def insert_at_last(self,val):
        n=linked_node(val)
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
    

    def printls(self):
        temp=self.head
        tm=""
        while temp:
            tm+=str(temp.data)+"-->"
            temp=temp.next
        tm+="None"
        print(tm)

    def revers_in_k_group(self,k):
        head=self.head
        if head is None:
            return
        dummy=tail=linked_node(0)
        dummy.next=head
        
        while head:
            cur=head
            count=0
            while head and count<k:
                head=head.next
                count=count+1
           
            if count==k:
                prev=None
                tail2=cur
                while count>0:
                    tmp=cur.next
                    cur.next=prev
                    prev=cur
                    cur=tmp
                    count-=1
                tail.next=prev
                tail=tail2
            else:
                tail.next=cur
        self.head=dummy.next


if __name__=="__main__":
    r1=linked_list()
    d1=[1,2,3,4,5,6,9]
    r1.insert_values(d1)
    r1.revers_in_k_group(4)
    r1.printls()