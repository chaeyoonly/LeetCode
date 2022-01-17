class Solution:
    def reverseWords(self, s: str) -> str:
        word = s.split(" ")
        string = ""
        for i in word:
            string += i[::-1]
            string += " "
        return string[:-1]

      
### Two pointers
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip().split()                   #Converting s into a list to get rid of spaces
        out = []
        for word in s:                          #Reversing each word of the list using two-pointers
            i = 0
            j = (len(word) - 1)
            while (i < j):
                word = list(word)
                word[i], word[j] = word[j], word[i]
                i += 1
                j -= 1
            a = (''.join(word))
            out.append(a)
        return(' '.join(out))                     #joining the words back to form a string