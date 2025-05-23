class Solution:
    def reverseWords(self, s: str) -> str:
        s_list = s.split()
        return " ".join(s_list[::-1])

    def reverseWords2(self, s: str) -> str:
        i = len(s) - 1
        parsed_str = []
        word = ""
        while i >= 0:
            if s[i] == " ":
                if word:
                    parsed_str.append(word[::-1])
                    word = ""
            else:
                word += s[i]
            i -= 1
        if word:
            parsed_str.append(word[::-1])
        return " ".join(parsed_str)
