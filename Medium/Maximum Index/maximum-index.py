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
if __name__ == "__main__":
	t = int(input())
	while(t>0):
		num = int(input())
		arr = [int(x) for x in input().strip().split()]
		ob = Solution()
		print(ob.maxIndexDiff(arr,num))
		t-=1
# } Driver Code Ends