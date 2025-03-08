class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        w_count = blocks[:k].count("W")
        res = w_count
        for i in range(1, len(blocks) - k + 1):
            w_count -= 1 if blocks[i-1] == "W" else 0
            w_count += 1 if blocks[i+k-1] == "W" else 0
            res = min(res, w_count)
        return res