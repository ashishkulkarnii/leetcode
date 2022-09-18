class Solution:
    def trap(self, height: List[int]) -> int:
        water, leftmax, rightmax = [0 for i in height], [0 for i in height], [0 for i in height]
        
        leftmax[0] = height[0]
        for i in range(1, len(height)):
            if leftmax[i-1] < height[i]:
                leftmax[i] = height[i]
            else:
                leftmax[i] = leftmax[i-1]
        
        rightmax[-1] = height[-1]
        for i in range(len(height)-2, -1, -1):
            if rightmax[i+1] < height[i]:
                rightmax[i] = height[i]
            else:
                rightmax[i] = rightmax[i+1]
                
        for i in range(1, len(height) - 1):
            temp = min([leftmax[i], rightmax[i]]) - height[i]
            water[i] = temp if temp > 0 else 0
        
        return sum(water)