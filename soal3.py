def sort_odd_even(num):
    for i in range(len(num)):
        for j in range(i+1, len(num)):
            if num[i] % 2 == 0 and num[j] % 2 == 0:
                if num[i] < num[j]:
                    num[i], num[j] = num[j], num[i]
            elif num[i] % 2 != 0 and num[j] % 2 != 0:
                if num[i] > num[j]:
                    num[i], num[j] = num[j], num[i]           
    return num
print(sort_odd_even([5,3,2,8,1,4]))
