#User function Template for python3

class Solution:
    #Complete this function
    # Function to find the maximum index difference.
    def maxIndexDiff(self,a,n): 
        stack=[]
        for i in range(n-1,-1,-1):
            if not stack or a[stack[-1]]<=a[i]:
                stack.append(i)
        i = 0
        ans = 0
        while stack:
            if not stack or a[i] <= a[stack[-1]]:
                ans = max(ans, stack[-1] - i)
                stack.pop()
            else:
                i += 1

        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            ob=Solution()
            print(ob.maxIndexDiff(arr,n))
            
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends