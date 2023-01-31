total_price = int(input())
cnt = int(input())
arr = []
sum = 0

for i in range(cnt):
    a , b = map(int, input().split())
    arr.append(a*b) 
for i in range(cnt):
    sum += arr[i]
if sum == total_price:
    print("Yes")
else:
    print("No")
