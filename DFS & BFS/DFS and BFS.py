#!/usr/bin/env python
# coding: utf-8

# In[19]:


#Lab 10
class stack:
    def __init__(self,size):
        self.data = [0 for i in range(size)]
        self.top = 0
        self.size = size
    
    def isEmpty(self):
        return self.top == 0
    
    def push(self,val):
        if self.top != self.size:
            self.data[self.top] = val
            self.top += 1
        else:
            return "stack overflow"
        
    def pop(self):
        if not self.isEmpty():
            x = self.data[self.top-1]
            self.top -= 1
            return x
        else:
            return "stack underflow"
        
    def peek(self):
        if not self.isEmpty():
            return self.data[self.top-1]
        
    def count(self):
        return self.top
        
class Queue:
    def __init__(self,size):
        self.size = size
        self.data = [0 for i in range(size)]
        self.rare = 0
        self.front = 0
        self.count = 0
        
    def isEmpty(self):
        if self.count == 0:
            return True
        return False
        
    def enqueue(self,val):
        if self.count != self.size:
            self.data[self.rare] = val
            self.rare = (self.rare + 1) % self.size
            self.count += 1
        else:
            return "Queue Overflow"
    
    def dequeue(self):
        if self.count != 0:
            x = self.data[self.front]
            self.front = (self.front + 1) % self.size
            self.count -= 1
            return x
        else:
            return "Queue Underflow"
        
    def peek(self):
        if not self.isEmpty():
            return self.data[self.rare]
        return "Queue is empty"
    
    def Count(self):
        return self.count
    
class Graph:
    def __init__(self,v):
        self.v = v
        self.adjmat = [[0 for i in range(v)]for j in range(v)]
        
    def addEdge(self,source,dest):
        if source == dest:
            return "source and destination can not be same"
        else:
            self.adjmat[source][dest] = 1
            self.adjmat[dest][source] = 1
            
    def getNeighbours(self,vertex):
        temp = []
        for i in range(len(self.adjmat[vertex])):
            if self.adjmat[vertex][i] == 1:
                temp.append(i)
        return temp
    
    def printMat(self):
        for i in self.adjmat:
            for j in i:
                print(j,end=" ")
            print()
            
    def BFS(self,source):
        visited_Q = []
        obj_Q = Queue(self.v)
        obj_Q.enqueue(source)
        visited_Q.append(source)
        while not obj_Q.isEmpty():
            x = obj_Q.dequeue()
            print("Visited :",x+1)
            neg = self.getNeighbours(x)
            for i in neg:
                if i not in visited_Q:
                    obj_Q.enqueue(i)
                    visited_Q.append(i)
                    
    def DFS(self,source):
        visited_stk = []
        obj_stk = stack(self.v)
        obj_stk.push(source)
        visited_stk.append(source)
        while not obj_stk.isEmpty():
            x = obj_stk.pop()
            print("Visited :",x+1)
            neg = self.getNeighbours(x)
            for i in neg:
                if i not in visited_stk:
                    obj_stk.push(i)
                    visited_stk.append(i)
            
g1 = Graph(10)
g1.addEdge(0,1)
g1.addEdge(0,3)
g1.addEdge(3,2)
g1.addEdge(1,2)
g1.addEdge(2,9)
g1.addEdge(2,8)
g1.addEdge(1,7)
g1.addEdge(1,6)
g1.addEdge(1,4)
g1.addEdge(4,5)
g1.addEdge(4,6)
g1.addEdge(7,6)
print("Adjacent Matrix: \n")
g1.printMat()
print("\nBFS: \n")
g1.BFS(0)
print("\nDFS: \n")
g1.DFS(0)


# In[ ]:




