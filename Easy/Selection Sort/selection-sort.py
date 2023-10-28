#User function Template for python3

class Solution: 
    def select(self, arr, i):
        # code here 
        return selectionSort(arr,n)
    
    def selectionSort(self, arr,n):
        #code here
        for i in range(0,len(arr)-1):
            min = i
            for j in range(i+1,len(arr)):
                if (arr[j] < arr[min]):
                    min = j
            if (min != i):
                arr[i],arr[min] = arr[min],arr[i]
        return arr


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends