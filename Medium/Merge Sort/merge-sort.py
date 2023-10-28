#User function Template for python3

class Solution:
    def merge(self,arr, l, m, r): 
        # code here
        return mergeSort(arr,l,r)
    def mergeSort(self,arr, l, r):
        #code here
        return arr.sort()



#{ 
 # Driver Code Starts
#Initial Template for Python 3


import sys
input = sys.stdin.readline
if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int,input().split()))
        Solution().mergeSort(arr, 0, n-1)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends