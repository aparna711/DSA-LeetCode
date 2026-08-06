class Solution(object):
    def maxArea(self, height):
        #The below docstring tells about the input and return type of the code
        '''
        :type height: List[int]
        :rtype: int
        '''
        #code of maxArea()
       
        maxArea = 0
        #List index
        left = 0
        right = len(height) -1
        
        while left<right:
                Area = min(height[right],height[left])*(right-left)
                if(Area > maxArea):
                    maxArea = Area
                if height[left] < height[right]:
                    left += 1
                else:    
                    right -= 1
        return maxArea
        
'''
import array as arr

height = arr.array('i', [2,5,6,7,7,8])
height_1, height_2, max_area = 0, 0, 0
result = []

for i in range(0, len(height)-1):
  for j in range(1, len(height)):
    Area = min(height[i], height[j]) * (j - i)
    if Area > max_area:
      height_1, height_2 = i, j;
      max_area = Area;
  

result.append(height[height_1])
result.append(height[height_2])
result.append(max_area)

print('Height of first line: ',result[0])
print('Height of second line: ',result[1])
print('Maximum water contained : ',result[2])
'''


'''
# --- LeetCode's Hidden Driver Code for Python execution---

# 1. LeetCode instantiates your Solution class
solver = Solution()

# 2. LeetCode passes its test case array into your method as an argument
test_array = [1, 8, 6, 2, 5, 4, 8, 3, 7]
result = solver.maxArea(test_array)  # 'height' parameter receives 'test_array'

# 3. LeetCode checks your returned value against the expected answer
assert result == 49
'''