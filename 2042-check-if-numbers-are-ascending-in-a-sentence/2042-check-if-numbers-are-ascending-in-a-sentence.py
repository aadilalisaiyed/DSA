class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        s=s.split()
        arr=[]
        print(s)
        for i in s:
            if i.isdigit():
                arr.append(int(i))
        print(arr)
        for i in range(len(arr)-1):
            if arr[i]>=arr[i+1]:
                return False
        return True
    