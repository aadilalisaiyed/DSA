class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapp={")":"(", "}":"{", "]":"["}
        for i in s:
            if i in mapp.values():
                stack.append(i)
            elif i in mapp.keys():
                if stack and stack[-1]==mapp[i]:
                    stack.pop()
                else:
                    return False
        
        if stack == []:
            return True
        return False

