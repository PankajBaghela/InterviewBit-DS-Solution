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
    
    def del_dup_in_list(self):
        dumy=slow=node(0)
        cur=self.head
        dumy.next=cur
        while cur:
            if cur.next and cur.data==cur.next.data:
                while cur.next and cur.data==cur.next.data:
                    cur=cur.next
                slow.next=cur.next
            else:
                slow=slow.next
            cur=cur.next
        r=linked_list()
        r.head=dumy.next
        r.print()

        

if __name__=="__main__":
    r1=linked_list()
    test=[[1,2,2,3,4,4,5],[2,2,2,2,2,2,3],[2,3,4,5,6,6,7,8,8]]
    for i in test:
        r1.insert_values(i)
        r2=linked_list()
        r1.del_dup_in_list()
        #r1.print()