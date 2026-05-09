class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        bracket = [""]*(n*2)

        def solve(ind,total,result,bracket):

            if ind >= len(bracket):
                if total == 0:
                    result.append("".join(bracket))
                return

            if total > len(bracket)//2:
                return

            elif total < 0 or total > n:
                return 

            bracket[ind] = "("
            sum = total + 1
            solve(ind + 1, sum,result,bracket)
            bracket[ind] = ")"
            sum = total - 1
            solve(ind + 1, sum , result,bracket)
        solve(0,0,result,bracket)
        return result