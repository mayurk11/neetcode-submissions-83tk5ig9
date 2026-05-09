class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
            
        result = []
        
        def solve(index,subset):

            phone_map = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }   
            if index >= len(digits):
                result.append("".join(subset))
                return

            for ch in phone_map[digits[index]]:
                subset.append(ch)
                solve(index + 1 , subset)
                subset.pop()

        solve(0,[])

        return result

        
        
        
        
        
        
        
        
        # if not digits:
        #     return []

        # phone_map = {
        #     "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
        #     "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        # }

        # result = [""]

        # for digit in digits:
        #     temp = []
            
        #     for letter in phone_map[digit]:
        #         for combitation in result:
        #             temp.append(combitation + letter)

        #     result = temp

        # return result