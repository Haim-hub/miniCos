
def knuthSeq(a):
	b = [1]
	while b[0] < len(a):
		b.insert(0, 3 * b[0] + 1)
	return b

array = [6,4,7,1,1,2,8,10,3,5,123,63,24,62,1,1,42,235,45,7,23,0]
gaps = knuthSeq(array)

for gap in gaps:

	for offset in range(gap):

		i = offset
		while i < len(array):
			temp = array[i]

			j = i
			while j >= gap and array[j-gap] > temp:
				array[j] = array[j-gap]
				j -= gap

			array[j] = temp

			i+=gap

print(array)