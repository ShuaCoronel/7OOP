
row = int(input("How Many Rows?: "))
col = int(input("How Many Columns?: "))

for i in range(1, row + 1):
    for j in range(1, col + 1):
        print(i*j, end=" ")
    print()
