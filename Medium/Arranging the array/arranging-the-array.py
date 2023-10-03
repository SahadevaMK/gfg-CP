
# from typing import List


# class Solution:
#     def Rearrange(self, n : int, arr : List[int]) -> None:
#         # code here
#         l=0
#         r=len(arr)-1
#         while(l<r):
#             if arr[l]<0:
#                 l+=1
#             if arr[r]>0:
#                 r-=1
#             else:
#                 arr[l],arr[r]=arr[r],arr[l]
#                 l+=1
#                 r-=1
                
        
from typing import List

class Solution:
    def Rearrange(self, n: int, arr: List[int]) -> None:
        # Separate negative and positive numbers
        negatives = [x for x in arr if x < 0]
        positives = [x for x in arr if x >= 0]

        # Rearrange the original array
        index = 0
        for neg in negatives:
            arr[index] = neg
            index += 1
        for pos in positives:
            arr[index] = pos
            index += 1    



#{ 
 # Driver Code Starts

class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        
        arr=IntArray().Input(2)
        
        obj = Solution()
        obj.Rearrange(n, arr)
        
        print(*arr, end=' ')
        print()

# } Driver Code Ends