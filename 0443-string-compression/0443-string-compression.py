class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        chars.append(1)
        while i < len(chars) - 1:
            j = i + 1
            while j < len(chars):
                if chars[i] != chars[j]:
                    chars[:] = chars[:i+1:] + chars[j::]
                    count = j - i
                    temp = 0
                    if count == 1:
                        break
                    while count > 0:
                        chars.insert(i + 1, str(count % 10))
                        count //= 10
                        temp += 1
                    i += temp
                    break
                j += 1
            i += 1
        return len(chars) - 1