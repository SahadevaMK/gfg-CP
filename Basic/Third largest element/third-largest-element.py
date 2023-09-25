
        # code here
class Solution:
    def thirdLargest(self,a, n):
        i,j,k=1,1,1
        for t in a:
            if(t>i):
                k=j
                j=i
                i=t
            elif(t>j):
                k=j
                j=t
            elif(t>k):
                k=t
        return k


#{ 
 # Driver Code Starts
# Your code goes here
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        print(Solution().thirdLargest(arr, n))
# } Driver Code Ends