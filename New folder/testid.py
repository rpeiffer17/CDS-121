x = 42
print (f"{x} {id(x)}")
y = x
print(f"{x} {id(x)}")
print(f"{y} {id(y)}")