#User function Template for python3

class Solution:
	def countOddEven(self, arr, n):
		#Code here
		ec,oc=0,0
		for i in range(n):
		    if arr[i]%2==0:
		        ec+=1
		    else:
		        oc+=1
		print(oc,ec)
# 		print(ec)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        n = int(input())
        arr = list(map(int, input().strip().split()))
    	obj = Solution()
    	obj.countOddEven(arr, n);
# } Driver Code Ends