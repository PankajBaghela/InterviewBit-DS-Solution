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
        

    def print_ls(self):
        temp=self.head
        tm=""
        while temp:
            tm+=str(temp.data)+"-->"

            temp=temp.next

        print(tm)
    
    def merge_two_sort(self,A,B):
        curA,curB=A.head,B.head
        start=node(0)
        cur=start
        while curA or curB:
            if curA and curB:
                if curA.data<curB.data:
                    cur.next=curA
                    curA=curA.next
                else:
                    cur.next=curB
                    curB=curB.next
            elif curA:
                cur.next=curA
                curA=curA.next
            else:
                cur.next=curB
                cur=cur.next
            cur=cur.next
        A.print_ls()


if __name__=="__main__":
    r1=linked_list()
    r2=linked_list()
    a=[1,4,8]
    r1.insert_values(a)
    b=[5,9,11]
    r2.insert_values(b)
    r3=linked_list()
    r3.merge_two_sort(r1, r2)
    
    
    