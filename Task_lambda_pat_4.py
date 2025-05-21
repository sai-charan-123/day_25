a=64
x=lambda n: [''.join([chr(a + i) + ' ' for j in range(i)]) for i in range(1,5)]
for line in x(a):
    print(line)

