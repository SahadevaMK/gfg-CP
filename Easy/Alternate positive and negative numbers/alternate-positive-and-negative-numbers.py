#User function Template for python3

class Solution:
    def rearrange(self,arr, n):
        # code here
        pos = []
        neg = []
        
        for i in range(len(arr)):
            if (arr[i]>=0):
                pos.append(arr[i])
            else:
                neg.append(arr[i])
        
        i=j=k=0
        
        while(i<len(pos) and j<len(neg)):
            arr[k]=pos[i]
            i+=1
            k+=1
            arr[k]=neg[j]
            j+=1
            k+=1
        while i <len(pos):
            arr[k]=pos[i]
            i+=1
            k+=1
        while j <len(neg):
            arr[k]=neg[j]
            j+=1
            k+=1
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	tc = int(input())
	while tc > 0:
		n = int(input())
		arr = list(map(int, input().strip().split()))
		ob = Solution()
		ob.rearrange(arr, n)
		for x in arr:
			print(x, end=" ")
		print()
		tc -= 1

# } Driver Code Ends