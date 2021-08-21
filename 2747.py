a=0
b=1
x=1

for i in range(int(input())):
    if i > 1:
        a = b
        b = x
        x = a + b

print(x)