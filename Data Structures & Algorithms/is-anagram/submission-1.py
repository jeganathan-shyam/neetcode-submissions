class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_count: dict[str, int] = {}

        #populate dictionary with char and count.
        for char_s in s:
            s_count[char_s] = s_count.get(char_s, 0) + 1

        for char_t in t:
            s_count[char_t] = s_count.get(char_t, 0) - 1
            if s_count[char_t] == -1:
                return False
            if s_count[char_t] == 0:
                del s_count[char_t]

        if len(s_count.items()) == 0:    
            return True
        
        return False