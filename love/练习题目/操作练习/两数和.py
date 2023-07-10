nums = [2,7,11,15]
target = 9
count = -1
for i in nums:
        count += 1
        num = target - i
        if num in nums:
            index_num = nums.index(num)
            break
print(count, index_num)