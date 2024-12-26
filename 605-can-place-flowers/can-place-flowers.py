class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        count = 0  # Count of flowers planted
        length = len(flowerbed)
        
        for i in range(length):
            if flowerbed[i] == 0:  # Check if current spot is empty
                # Check left and right neighbors
                prev = (i == 0) or (flowerbed[i - 1] == 0)
                next = (i == length - 1) or (flowerbed[i + 1] == 0)
                
                if prev and next:  # Plant a flower if both neighbors are empty
                    flowerbed[i] = 1
                    count += 1
                
            # Stop checking early if we've planted enough flowers
            if count >= n:
                break
        
        # Return the result after the loop
        return count >= n
