# Brutal concept performed during interview.
class Solution1:
    def fourSum(self, nums, target):
        ret = set()
        nums.sort()
        self.dfs(nums, target, [], ret)
        return [list(i) for i in ret]

    def dfs(self, nums, target, cur, ret):
        if len(cur) == 4:
            if sum(cur) == target:
                ret.add(tuple(cur))
            return
        for i in range(len(nums) - 3 + len(cur)):
            cur.append(nums[i])
            self.dfs(nums[i + 1:], target, cur, ret)
            cur.pop()


# Based on 3Sum
class Solution2:
    def fourSum(self, nums, target):
        ret = set()
        nums.sort()
        for i in range(len(nums) - 3):
            self.three_sum(nums[i + 1:], target - nums[i], [nums[i]], ret)
        return [list(i) for i in ret]

    def three_sum(self, nums, target, cur, ret):
        if len(nums) < 3:
            return []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j = i + 1
            k = len(nums) - 1
            t = target - nums[i]
            while j < k:
                if nums[j] + nums[k] == t:
                    c = cur.copy()
                    c.extend([nums[i], nums[j], nums[k]])
                    ret.add(tuple(c))
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1
                    j += 1
                    k -= 1
                elif nums[j] + nums[k] < t:
                    j += 1
                else:
                    k -= 1


# Based on two sum, and some improvement.
class Solution:
    def fourSum(self, nums, target):
        ret = []
        nums.sort()
        for i in range(len(nums) - 3):
            # Since nums is sorted, the first number must be the smallest in combination.
            if nums[i] * 4 > target:
                break
            # If current number is the same as previous one.
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums) - 2):
                if nums[i] + nums[j] * 3 > target:
                    break
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                self.two_sum(nums[j + 1:], target - nums[i] - nums[j], [nums[i], nums[j]], ret)
        return ret

    def two_sum(self, nums, target, cur, ret):
        d = {}
        for i in range(len(nums)):
            d[nums[i]] = i
        for idx, i in enumerate(nums):
            if (target - i) in d and d[target - i] != idx:
                d.pop(i, None)
                d.pop(target - i, None)
                ret.append([cur[0], cur[1], i, target - i])
