x = int(input("Enter x: "))

if x <= 0:
    print("The number must be positive")

for i in range (1, x + 1): #each row from 1 up to and including x

    for j in range (1, i + 1) : #j goes from 1 to the current row index i
        print(j, end = ' ')

    print()








   
  


