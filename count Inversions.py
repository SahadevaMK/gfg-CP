class Solution:
    #User function Template for python3
    
    # arr[]: Input Array
    # N : Size of the Array arr[]
    #Function to count inversions in the array.
    def inversionCount(self, arr, n):
        count = 0
        
        for i in range(len(arr)):
            j=i+1
            while(j<len(arr)):
                if arr[i]>arr[j]:
                    count+=1
                j+=1
        return count
        # Your Code Here
