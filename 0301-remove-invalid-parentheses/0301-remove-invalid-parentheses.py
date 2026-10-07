class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        ans=[]
        maxi=0
        def valid(substr):
            depth=0
            for i in substr:
                if i=='(':
                    depth+=1
                elif i==')':
                    depth-=1
                    if depth<0:
                        return False
                    
            return depth==0
        level = {s}
        while True:
            valid_list = list(filter(valid, level))
            if valid_list:
                return valid_list
            
            # Generate next level by removing 1 parenthesis at a time
            next_level = set()
            for string in level:
                for i in range(len(string)):
                    if string[i] in '()':
                        next_level.add(string[:i] + string[i+1:])
            level = next_level