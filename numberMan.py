numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, ]
for item in numbers:
    print (item)

## note this same code can be run differently as shown below
i = 1 
while i < len(numbers):
    print(numbers[i])
    i = i + 1

## Range functions
numbers = range (0, 9)
for number in numbers:
    print(number)