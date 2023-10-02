#User function Template for python3

def find4Numbers( arr, n, X):
    # return true or false
    arr.sort()
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            k=j+1
            l=n-1
            while(k<l):
                sumi = arr[i]+arr[j]+arr[k]+arr[l]
                if sumi==X:
                    return True
                elif(sumi<X):
                    k+=1
                else:
                    l-=1
    return False
    




#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        A = [int(x) for x in input().strip().split()]
        X = int(input())
        
        if find4Numbers(A, n, X):
            print(1)
        else:
            print(0)

        T -= 1


if __name__ == "__main__":
    main()


# } Driver Code Ends