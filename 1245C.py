#m-> nn  w-> uu  
#yanlis calisiyor
#len(subst)^subs_count * digerleri
def fibo(n):
    i = 0
    First_Value = 0
    Second_Value = 1
    Next = 0
    while(i < n):
            if(i <= 1):
                        Next = i
            else:
                        Next = First_Value + Second_Value
                        First_Value = Second_Value
                        Second_Value = Next
            i = i + 1
    return Next

def strcmp(str,str1):
    count = 0
    for i in range(len(str) - 1):
        if (str[i] + str[i+1]) == str1:
            count += 1  
    return count

line = input()

if line.find("m") != -1 or line.find("w") != -1:
    print("0")
    exit()

elif line.find("nn") == -1 and line.find("uu") == -1:
    print("1")
    exit()

else:   
    x = strcmp(line,"uu")
    y = strcmp(line,"nn")

    count = x + y
    if x == 0 or y == 0:
        print(fibo(x+y+3) % (pow(10,9) + 7))
    else:
        print(count)
        print(pow(count,2) % (pow(10,9) + 7))