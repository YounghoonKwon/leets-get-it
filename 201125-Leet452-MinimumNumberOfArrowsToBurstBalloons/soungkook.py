from functools import cmp_to_key

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        #we have to sort by right edge(diameter's right point)
        #since you can start with shortest range for minimum arrows
        points = sorted(points, key=cmp_to_key(lambda a,b:a[1]-b[1]))

        size=len(points)
        #move next iteration manually
        i = 0
        arrows=0
        while i < size:
            #you will compare with target
            target = points[i]
            
            #look next 
            j= i+1
            while j < size and points[j][0] <= target[1]:
                # shot in line and move next
                j+=1
            
            arrows+=1
            #skip balloons in line
            i=j
            
        return arrows
