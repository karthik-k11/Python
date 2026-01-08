##Find two numbers in an array that add up to a target.
##Trick:- Use a hashmap to store the numbers and their indices.

def twoSum(nums, target):
    seen={}

    for i, num in enumerate(nums):
        needed= target - num 

        if needed in seen:
            return [seen[needed], i]
        
        seen[num]=i

if __name__ == "__main__":
    
    nums1 = [2, 7, 11, 15]
    target1 = 9
    print(f"Test 1: {twoSum(nums1, target1)}") 

    nums2 = [3, 2, 4]
    target2 = 6
    print(f"Test 2: {twoSum(nums2, target2)}")

    nums3 = [3, 3]
    target3 = 6
    print(f"Test 3: {twoSum(nums3, target3)}") 