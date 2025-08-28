# You are given two strings order and s. All the characters of order are unique and were sorted in some custom order previously.
#
# Permute the characters of s so that they match the order that order was sorted. More specifically, if a character x occurs before a character y in order, then x should occur before y in the permuted string.
#
# Return any permutation of s that satisfies this property.
#
# Example 1:
#
# Input: order = "xabfcg", s = "bdca"
#
# Output: "abcd"



class CustomSortString:
    def customeSort(self,order : str, s: str):

        frequencyCount = {}

        for ch in s:
            frequencyCount[ch] = frequencyCount.get(ch,0) + 1

        res = []
        for ch in order:

            while ch in frequencyCount and frequencyCount[ch]:
                res.append(ch)
                frequencyCount[ch] -= 1

        for ch,cnt in frequencyCount.items():
            for _ in range(cnt):
                res.append(ch)

        return res





customestring = CustomSortString()
print(customestring.customeSort("ABD","ANNCCFD"))