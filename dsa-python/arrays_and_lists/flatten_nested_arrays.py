from typing import Any, List

class Solution:

    def flatten(self, nestedLists: List[Any], resultList: List[int]) -> None:
        for element in nestedLists:
            if isinstance(element, int):
                resultList.append(element)
            elif isinstance(element, List):
                self.flatten(element, resultList)


s = Solution()
list = list()
s.flatten([1, [2,3], 4, [5, [6,7]]], list)
print(list)
    

 