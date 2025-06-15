from typing import List

def twoSum(self, nums: List[int], target: int) -> List[int]:
        i=0
        while (i<len(nums)):
            j=i
            while (j<len(nums)):
                if i != j and nums[i] + nums[j] == target:
                    return [i,j]
                    break
                j=j+1
            i=i+1
        return [0,0]

nums = [2, 7, 11, 15]
target = 9