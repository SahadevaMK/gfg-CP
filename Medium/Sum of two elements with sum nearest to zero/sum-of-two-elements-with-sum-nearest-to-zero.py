#User function Template for python3
import sys
class Solution:
    def closestToZero (self,arr, n):
        # your code here
        arr.sort()
        ans=sys.maxsize
        l=0
        r=n-1
        while l < r:
            sumi=arr[l]+arr[r]
            if sumi == 0:
                return 0
            if abs(sumi) < abs(ans):
                ans=sumi
            elif abs(sumi) == abs(ans):
                ans=max(ans,sumi)
            if sumi < 0:
                l+=1
            else:
                r-=1
        return ans




#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int (input ())
for tc in range(t):
    n = int (input ())
    arr = list(map(int, input().split()))
    ob = Solution()
    print (ob.closestToZero (arr, n))
# } Driver Code Ends