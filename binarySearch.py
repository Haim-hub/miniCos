
array = [1,2,3,4,5,6,7,8,9,10]
find = 5;

lowerBound = 1
upperBound = len(array)

while True:
	if upperBound < lowerBound:
		print('The sucker does not exsist')
		break

	midpoint = lowerBound + ( upperBound - lowerBound ) / 2

	if array[midpoint] < find:
		lowerBound = midpoint + 1

	if array[midpoint] > find:
		upperBound = midpoint - 1

	if array[midpoint] is find:
		print(midpoint)
		break



