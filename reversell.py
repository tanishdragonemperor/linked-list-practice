class Node(object):
    def __init__(self,value):
        self.info=value
        self.nextnode=None

class reverse(head):
    current=head
    previous=None
    nextnode=None
    while current:
        nextnode=current.nextnode
        current.nextnode=previous
        previous=current
        current=nextnode


a=Node(1)
b=Node(2)

c=Node(3)
d=Node(4)
a.nextnode=2
b.nextnode=3
c.nextnode=4


print(a.nextnode.value)

print(b.nextnode.value)

print(c.nextnode.value)




