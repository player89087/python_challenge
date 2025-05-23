
fib_list = [1,2]
for i in range(33):
    fib_list.append(fib_list[i] + fib_list[i+1])


x = str(fib_list[30])
x = b"2178309"
print(type(x))
print(fib_list[30])

y = [1,0,0,0,0,1,0,0,1,1,1,1,0,1,0,0,0,0,0,1,0,1]
final = ""
for i in range(len(y)):
    z = y[i]+1
    final += str(z)
print(len(final))


