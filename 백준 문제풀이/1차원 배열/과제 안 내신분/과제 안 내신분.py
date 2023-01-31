arr = []
arr_miss = list(range(1,31))

for i in range(28):
    a = int(input())
    arr.append(a)
for i in range(1, 31):
    for j in range(28):
        if i == arr[j]:
            arr_miss.remove(i)
arr_miss.sort()
for i in range(len(arr_miss)):
    print(arr_miss[i])


