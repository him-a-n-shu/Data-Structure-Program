from http.client import FOUND
from turtle import position


def linearSearch(mlist,item):
    n = len(mlist)
    for i in range(n):
        if item == mlist[i]:
            return i
    return None

arr = []
n = int(input("Enter how many items in List : "))
for i in range(n):
    d= int(input("Enter value : "))
    arr.append(d)
k = int(input("Enter value to search : "))

pos = linearSearch(arr,k)

if pos!= None:
    print("Found at position", pos+1)
else:
    print("Not FOUND")