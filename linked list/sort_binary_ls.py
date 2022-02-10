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
        

    def print(self):
        temp=self.head
        tm=""
        while temp:
            tm+=str(temp.data)+"-->"

            temp=temp.next

        print(tm)
    def binary_sort_LL(self):
        temp=self.head
        zeros=0
        ones=0
        while temp:
            if temp.data==0:
                zeros+=1
            else:
                ones+=1
            temp=temp.next
        temp=self.head
        for i in range(zeros):
            temp.data=0
            temp=temp.next
        for i in range(ones):
            temp.data=1
            temp=temp.next
           


if __name__=="__main__":
    r1=linked_list()
    d=[1,0,1,0,1,0]
    r1.insert_values(d)
    r1.binary_sort_LL()
    r1.print()