class Node:

  

    def __init__(self, one, twe, three):

        self.ldata=[]

        self.ldata.insert(one)

        self.ldata.insert(twe)

        self.ldata.insert(three)

        self.data=ldata

        self.next = None 

        self.prev = None 

  

class List:

    def init(self):       

        self.head = Node(None,None,None)

        self.head.next = self.head

        self.head.prev = self.head

        self.n = 0

      

    def get(self,ind1):

        if ind1 >=  self.size() :

            raise Exception('Out of list')

        a = self.head.next

        for i in range(ind1) :

            a=a.next

        return a

  

    def insert_after(self, a, one, b, three):

        b = Node(one, twe,three)

        self.n += 1

        b.prev = a

        b.next = a.next

        a.next = b

        b.next.prev = b

        return b

      

    def delete(self, a):

        if self.size()==0:

            raise Exception('List is empty')

        self.n -= 1

        a.prev.next = a.next

        a.next.prev = a.prev

        return a

      

    def find(self, val):

        a = self.head.next

        for i in range(self.size()) :

            if a.data == val :

               return a

            a=a.next

        return None

  

    def size(self):

        return self.n

    

    def is_empty(self):

        return self.n==0

  

    def sum(self, a, b):

        return a+b

#Example

l=List()

l.insert_after(list.head,1,4,5)

l.insert_after(list.get(0),1,0,4)

print(l.sum(list.get(0),list.get(1)))
