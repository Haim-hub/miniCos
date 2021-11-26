
def mergesort(a):
	if len(a) is 1:
		print(a)

	l1 = a[0: (len(a)/2)]
	l2 = a[(len(a)/2):len(a)]

	print(l1)
	print(l2)
		
	if(len(a) > 2):
		l1 = mergesort(l1)
		l2 = mergesort(l2)

	return merge(l1,l2)


def merge(a, b):
	c = []
	while a and b:
		if a[0] > b[0]:
			c.append(b[0])
			b.pop(0)
		else:
			c.append(a[0])
			a.pop(0)
	
	while a:
		c.append(a[0])
		a.pop(0)

	while b:
		c.append(b[0])
		b.pop(0)

	return c

array = [6,4,7,9,1,2,8,10,3,5]

print(mergesort(array))

