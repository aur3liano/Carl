# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 10:48:39 2020

Practicing linked lists

@author: jpaul
"""

#Define the linked list class
class LinkedList():
    #Write the linked class initialization function
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next

    #Write the linked list representation function
    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        return(nodes)

    #Write the linked list insert function
    def add_first(self, node):
        node.next = self.head
        self.head = node
    
    #Write the linked list append function
    def add_last(self, node):
        if not self.head:
            self.head = node
            return
        for current_node in self:
            pass
        current_node.next = node

    #Write the linked list iteration function
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

#Define the node class
class Node:
    #Write the node initialization function
    def __init__(self, data):
        self.data = data
        self.next = None

    #Write the node representation function
    def __repr__(self):
        return self.data

def main():
    #Create the list of nodes
    num_of_reps = 3
    nodes = [[1,2,3]]*num_of_reps
    print('nodes')
    print(nodes)
    #Initialize (and build) the list
    llist = LinkedList([nodes[0]])
    for nds in range(num_of_reps):
        llist.add_last(Node(nodes[nds]))
    ll_nodes = llist.__repr__()
    print('ll_nodes')
    print(ll_nodes)
    b = nodes[0]
    print('b')
    print(b)
    b.remove(b[0])
    print('b element removed')
    print(b)
    print('nodes')
    print(nodes)
    '''
    #Create the list nodes
    first_node = Node(1)
    second_node = Node(2)
    third_node = Node(3)
    #Build the linked list
    llist.head = first_node
    first_node.next = second_node
    second_node.next = third_node
    '''
    #Show the linked list
    ll_nodes = llist.__repr__()
    #Print the object addresses for each item in the linked list
    print('ll_nodes')
    print(ll_nodes)
    for nids in range(len(ll_nodes)):
        print('each ll_node')
        print(ll_nodes[nids])
        print('each ll_node object')
        print(str(id(ll_nodes[nids])))
    print('b object')
    print(str(id(b)))
    return(llist)

def list_obj_comprehension():
    explicit_list = [[1,2,3],[1,2,3],[1,2,3]]
    print('explicit list')
    print(explicit_list)
    print('explicit list object ids')
    for el in range(len(explicit_list)):
        print(str(id(explicit_list[el])))
    a = explicit_list[0]
    print('explicit list element 1: a')
    print(a)
    print('explicit list element 1: a id')
    print(str(id(a)))
    a.remove(a[0])
    print('explicit list with a[0] removed')
    print(explicit_list)
    print('explicit list element 1 with a[0] removed')
    print(a)
    print()
    num_of_reps = 3
    auto_gen_list = [[1,2,3]]*num_of_reps
    print('auto_gen list')
    print(auto_gen_list)
    print('auto_gen list object ids')
    for agl in range(len(auto_gen_list)):
        print(str(id(auto_gen_list[agl])))
    b = auto_gen_list[0]
    print('auto_gen list element 1: b')
    print(b)
    print('auto_gen list element 1: b id')
    print(str(id(b)))
    b.remove(b[0])
    print('auto_gen list with b[0] removed')
    print(auto_gen_list)
    print('auto_gen list element 1 with b[0] removed')
    print(b)
    return(1)

list_obj_comprehension()