#User function Template for python3

class Solution:
    def findTwoElement( self,arr, n): 
        # code here
    
        total = (n*(n+1))//2
        hs = {}
        s = sum(arr)
        missin = 0
        h = set(arr)
        v = sum(h)
        
        missin = total-v
        
        
        for i in arr:
            if i in hs:
                hs[i]+=1
            else:
                hs[i]=1
        rep = 0
        for i in hs:
            if hs[i]>1:
                rep = i
        # for i in range(1,len(arr)+1):
        #     if i not in hs:
        #         missin += i
        return [rep,missin]
        
        
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 

    tc=int(input())
    while tc > 0:
        n=int(input())
        arr=list(map(int, input().strip().split()))
        ob = Solution()
        ans=ob.findTwoElement(arr, n)
        print(str(ans[0])+" "+str(ans[1]))
        tc=tc-1
# } Driver Code Ends