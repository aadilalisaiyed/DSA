class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        #vertical, horizontal (2>0 then overlap)
        #top, bottom (3>1 then overlap)
        if rec2[0] < rec1[2] and rec1[0]<rec2[2] and rec1[3] > rec2[1] and rec2[3] > rec1[1] :
            return True
        return False