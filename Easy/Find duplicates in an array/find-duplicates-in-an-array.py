class Solution:
    def duplicates(self, arr, n): 
        # code here
        unique_set = set()
    
        duplicate_set = set()
    
        for item in arr:
            if item in unique_set:
                duplicate_set.add(item)
            else:
                unique_set.add(item)
    
    
        duplicates_list = sorted(list(duplicate_set))
    
        if not duplicates_list:
            return [-1]
        else:
            return duplicates_list



            





#{ 
 # Driver Code Starts
if(__name__=='__main__'):
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        res = Solution().duplicates(arr, n)
        for i in res:
            print(i,end=" ")
        print()



# } Driver Code Ends