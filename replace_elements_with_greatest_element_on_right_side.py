class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        max=arr[len(arr)-1];
        arr[len(arr)-1]=-1;
        for i in range(len(arr)-2,-1,-1):
            t=arr[i];
            arr[i]=max;
            if(t>max):
                max=t;

        return arr;
