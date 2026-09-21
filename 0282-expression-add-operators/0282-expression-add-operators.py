class Solution:
    def addOperators(self, num: str, target: int) -> list[str]:
        res=[]
        n=len(num)
        def helper(idx,expr,val,prev):
            if idx == n:
                if val==target:
                    res.append(expr)
                return
            for j in range(idx,n):
                # Avoid numbers with leading zero
                if j > idx and num[idx] == '0':
                    break
                curr = int(num[idx:j+1])
                curr_str=num[idx:j+1]
                if idx==0:
                    helper(j+1,curr_str,curr,curr)
                else:
                    helper(j+1,expr + '+' + curr_str,val + curr,curr)
                    helper(j+1,expr + '-' + curr_str,val - curr,-curr)
                    helper(j+1,expr + '*' + curr_str,val - prev + prev * curr,prev*curr)
        helper(0,"",0,0)
        return res