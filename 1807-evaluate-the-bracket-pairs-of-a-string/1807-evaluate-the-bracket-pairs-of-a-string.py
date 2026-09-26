class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        n=len(s)
        m=len(knowledge)
        answer=""
        mp = {key:val for key,val in knowledge}
        
        i=0
        while i<n:
            if s[i]=='(':
                key=''
                j=i+1
                while s[j]!=')':
                    key+=s[j]
                    j+=1
                i=j
                answer +=mp.get(key,'?')
            else:
                answer+=s[i]
            i+=1
        return answer