import math

inputvalues = input('Enter all elements values: ')
numbers1 = inputvalues.split() 
numbers2 = []
for i in range(len(numbers1)):
	numbers1[i] = int(numbers1[i]) 
for i in range(0,len(numbers1),2):
	numbers2.append(numbers1[i])
for i in range(int(math.floor(len(numbers1)+1)/2)):
	numbers1.pop(i)
print(numbers2)
print(numbers1)
