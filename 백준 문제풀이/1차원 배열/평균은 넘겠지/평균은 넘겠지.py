test_case = int(input())
cnt = 0
sum = 0
arr_ans = []
# 5 10 20 30 40 50 
for j in range(test_case):
    arr_num = list(map(int, input().split()))
    for i in range(arr_num[0]):
        sum += arr_num[i+1]
    avg = sum / (len(arr_num) - 1)
    for i in range(len(arr_num) - 1):
        if arr_num[i+1] > avg:
            cnt += 1
    percent = cnt / (len(arr_num) - 1) * 100
    arr_ans.append(percent)
    sum = 0
    arr_num.clear()
for i in range(len(arr_ans)):
    print("{:.3f}".format(arr_ans[i]))   
    

