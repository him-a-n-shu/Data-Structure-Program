def Bsearch(mlist,item):
    low = 0
    high = len(mlist)-1
    while (low<=high):
        mid = (low+high)//2
        if mlist[mid]==item:
            return mid
        elif mlist[mid]>item:
            high = mid-1
        else:
            low = mid+1
    return - 1

arr = []

n = int(input("Enter how many items in List : "))

for i in range(n):
    d= int(input("Enter value : "))
    arr.append(d)

k = int(input("Enter value to search : "))

pos = Bsearch(arr,k)

if pos == -1:
    print("Not FOUND")
else:
    print("Found at position", pos+1)