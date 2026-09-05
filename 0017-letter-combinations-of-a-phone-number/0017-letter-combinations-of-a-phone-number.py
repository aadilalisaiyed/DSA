class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        codes={2:"abc",3:"def",4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz"}
        res=[]
        def helper(idx,substr):
            if idx == len(digits):
                res.append(substr)
                return
            for i in codes[int(digits[idx])]:
                helper(idx+1,substr+i)
        helper(0,"")
        return res
