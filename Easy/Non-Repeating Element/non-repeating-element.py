#User function Template for python3

class Solution:
    def firstNonRepeating(self, arr, n): 
        # Complete the function
        hs ={}
        for i in arr:
            if i not in hs:
                hs[i]=1
            else:
                hs[i]+=1
        for i in arr:
            if hs[i]==1:
                return i
        return 0


#{ 
 # Driver Code Starts
#Initial Template for Python 3

from collections import defaultdict 

for _ in range(0,int(input())):
    n = int(input())
    arr = list(map(int,input().strip().split()))
    ob = Solution()
    print(ob.firstNonRepeating(arr, n))
    
# } Driver Code Ends