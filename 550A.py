str = input()
x = str.find("AB")
y = str.find("BA")
if x != -1 and y != -1:
    if abs(x - y) > 1:
        print("YES")
        exit()
print("NO")