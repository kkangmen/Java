num = int(input())
cnt = 0

arr = list(map(int, input().split()))
found_num = int(input())
for i in range(num):
    if found_num == arr[i]:
        cnt += 1
print(cnt)