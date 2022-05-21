nums1 = [1, 2, 3]
nums2 = [4, 5, 6]
nums3 = [7, 8, 9] 
print("Original list: ")
print(nums1)
print(nums2)
print(nums3)
result = map(lambda x, y, z: x + y + z, nums1, nums2, nums3)
print("\nNew list after adding above three lists:")
print(list(result))