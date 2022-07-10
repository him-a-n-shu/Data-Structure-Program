import bisect

marks = eval(input("Current list is: "))

item = int(input("Enter item to insert: "))

pos = bisect.bisect(marks,item)
bisect.insort(marks,item)

print("\nItem inserted at index : ", pos)
print("Updated list: ", marks)