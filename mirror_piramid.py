num = int(input("Enter the number of rows : "))
for i in range(0, num):
    for j in range(0, num - i - 1):
        print(end=" ")
    for j in range(0, i + 1):
        print("*", end=" ")
    print()

for i in range(num,0,-1):
    for j in range(0,num-i+1):
        print(end=" ")
    for j in range(0, i-1):
        print("*", end=" ")

    print()

