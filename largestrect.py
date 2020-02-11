arr = [int(item)for item in input().split(" ")]
largest = 0
for i in range(len(arr)):
    idx = i
    sum = 0
    while arr[i] < arr[idx]:
        sum += arr[i]
        idx += 1
    if largest < sum:
        largest = sum

print(largest)