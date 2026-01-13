class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        st = []
        ans = 0

        for ch in s:
            if ch not in st:
                st.append(ch)
            else:
                while ch in st:
                    st.pop(0)
                st.append(ch)

            ans = max(ans, len(st))

        return ans

