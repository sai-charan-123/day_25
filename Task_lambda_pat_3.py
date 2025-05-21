z=lambda x:[''.join([chr(65+j)+' ' for j in range(i+1)]) for i in range(x)]
x=4
for y in z(x):
	print(y)
