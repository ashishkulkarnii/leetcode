class Solution:
    def bestClosingTime(self, customers: str) -> int:
        penalties = [0 if c == "N" else 1 for c in customers]
        running_sum = sum(penalties)
        min_penalty = running_sum
        closing_time = 0
        for h in range(1, len(customers) + 1):
            if penalties[h - 1] == 0:
                penalties[h - 1] = 1
                running_sum += 1
            else:
                penalties[h - 1] = 0
                running_sum -= 1
            if running_sum < min_penalty:
                min_penalty = running_sum
                closing_time = h
        return closing_time