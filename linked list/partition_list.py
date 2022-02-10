class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class linked_list:
    def __init__(self):
        self.head=None

    
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

    # partition_linked_list
    def partt_list(self,B):
        head=self.head
        small=s1=node(0)
        high=h1=node(0)
        while head:
            if head.data<B:
                s1.next=head
                s1=s1.next
            else:
                h1.next=head
                h1=h1.next
            head=head.next

        h1.next=None
        s1.next=high.next
         
        return small.next
    
           


if __name__=="__main__":
    r1=linked_list()
    d=[1,4,3,2,5,2]
    r1.insert_values(d)
    r1.partt_list(3)

    
    r1.print()