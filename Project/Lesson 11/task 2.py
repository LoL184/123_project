def lst(nums: list[int]) -> list[tuple[int, int]]:
    nums.sort()
    ans = []
    for num in [nums[i] for i in range(len(nums)) if (i == 0 or nums[i] != nums[i-1])]:
        ans.append((num, sum([1 for j in nums if j == num])))
    return ans


print(lst([1, 2, 2, 1, 5, 1]))
