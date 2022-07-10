def DoubleIt(arr):
    for i in range(len(arr)):
        arr[i] *= 2

arr = eval(input("Enter list; "))
print("Current List: ")
for i in arr:
    print(i)

DoubleIt(arr)
print("Afer update List: ")
for i in arr:
    print(i)