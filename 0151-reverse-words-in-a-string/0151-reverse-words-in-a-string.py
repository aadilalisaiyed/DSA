class Solution:
    def reverseWords(self, s: str) -> str:
        s=s[::-1]+" "
        start=0
        ans=[]
        for i in range(len(s)):
            if s[i]==" ":
                if start!=i:
                    ans.append(s[start:i][::-1])
                start = i+1
            

        return " ".join(ans)
