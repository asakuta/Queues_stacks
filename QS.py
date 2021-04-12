import math
import random

def enq(value, List):
    List.append(value)
    return List

def deq(List):
    newList=[]
    for x in range(0, len(List)-1):
        newList.insert(len(newList), List[x])
    result=[newList, List[len(List)-1]]
    print(result)
    return result

def reverse(List):
    newList=[]
    for x in range(0, len(List)):
        newList.insert(x, List[len(List)-1-x])
    return newList

def FIFO(List):
    list1=reverse(List)
    list2=deq(list1)
    list3=reverse(list2[0])
    print(list3)

List=[1,2,3]
enq(4, List)
FIFO(List)