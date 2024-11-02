try:
    x = int(input("Enter a number: "))

    if x <= 0:
        print("INVALID:The number should be positive")

    for i in range (1, x + 1): #each row from 1 up to and including x

        for j in range (1, i + 1) : #j goes from 1 to the current row index i
            print(j, end = ' ')

        print()

except ValueError:
    print("INVALID:Enter only a number")
