# singly linked list
class Node:
    def __init__(self, item=None, next=None):
        self.item=item
        self.next=next
class SLL:
    def __init__(self,start):
        self.start=start
    def is_empty(self):
        return self.start==None
    def insert_at_start(self,data):  
        n=Node(data, self.start)
        self.start=n
    def insert_at_last(self,data):
        n=Node(data,None)
        if not self.is_empty():
            temp=self.start
mylist=SLL