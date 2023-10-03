#User function Template for python3

# class Solution:
#     def productExceptSelf(self, nums, n):
#         #code here
#         pro=1
#         res = []
#         a=0
#         for i in arr:
#             pro = pro*i
#         for i in arr:
#             a = int(pro/i)
#             res.append(a)
#         return res
            
class Solution:
    def productExceptSelf(self, nums, n):
        # Calculate the product of all elements in the array
        total_product = 1
        zero_count = 0
        
        for num in nums:
            if num == 0:
                zero_count += 1
                if zero_count > 1:
                    # If there are more than one zero, all other elements become 0
                    return [0] * n
            else:
                total_product *= num
        
        # If there is one zero, all elements except the zero become 0
        if zero_count == 1:
            return [0 if num != 0 else total_product for num in nums]
        
        # Calculate the result by dividing the total product by each element
        result = [total_product // num for num in nums]
        return result

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())

    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().split()]

        ans=Solution().productExceptSelf(arr,n)
        print(*ans)
# } Driver Code Ends