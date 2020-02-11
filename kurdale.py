def cut(arr,lenght,parca):
    if lenght == 0:
        return parca
    else:
        for i in range(len(array)):
            if(lenght >= arr[i]):
                return cut(arr, lenght - arr[i], parca + 1)
array = [int(item)for item in input().split(" ")]
lenght = array.pop(0)
array.sort()
print(cut(array, lenght, 0))
