class Solution:
    def maxArea(self, height: list[int]) -> int:
        # взять самый левый и правый, смотреть что меньше, если левый столбик меньше - левый итератор двигаем нраправо, если наоборот, правый итератор двигаем направо
        l = 0
        r = len(height)-1
        v = 0
        while r != l:
            curr = min(height[l], height[r]) * (r-l)
            #print(f"l: {l} r: {r} h: {min(height[l], height[r])} p: {min(height[l], height[r]) * (r-l)}")
            if curr > v:
                v = curr
            if height[r] > height[l]:
                l+=1
            else:
                r-=1
        return v
result = Solution().maxArea([8,7,2,1])
print(result)