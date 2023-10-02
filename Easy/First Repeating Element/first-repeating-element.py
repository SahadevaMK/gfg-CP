#User function Template for python3

# class Solution:
#     #Function to return the position of the first repeating element.
#     def firstRepeated(self,arr, n):
#         hs ={}
#         a=0
#         for i in arr:
#             if i not in hs:
#                 hs[i]=1
#             else:
#                 hs[i]+=1
#         for key,val in hs.items():
#             if val==2:
#                 a=arr.index(key)
#                 return a+1
#         return -1

class Solution:
    #Function to return the position of the first repeating element.
    def firstRepeated(self,arr, n):
        
        #arr : given array
        #n : size of the array
        dict1 = {}
        for num in arr:
            if num in dict1:
                dict1[num] += 1
            else:
                dict1[num] = 1
        for i in range(n):
            if dict1[arr[i]] > 1:
                return i+1
        return -1
        #arr : given array
        #n : size of the array


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        
        arr=[int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.firstRepeated(arr, n))
# } Driver Code Ends