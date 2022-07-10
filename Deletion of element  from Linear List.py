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

marks = eval(input("Enter list : "))
ans = "y"

while ans=="y":
    item = int(input("Enter item to delete: "))
    pos = Bsearch(marks,item)
    if pos != -1:
        del marks[pos]
        print("\nList after deletion: ")
        print(marks)
    else:
        print("Sorry Item not found")
    ans = input("Delete more? --> ")