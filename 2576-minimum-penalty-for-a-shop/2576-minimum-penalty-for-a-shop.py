class Solution:
    def bestClosingTime(self, customers: str) -> int:
        running_sum = customers.count("N")
        min_penalty = running_sum
        closing_time = 0
        for h, c in enumerate(customers):
            if c == "N":
                running_sum += 1
            else:
                running_sum -= 1
            if running_sum < min_penalty:
                min_penalty = running_sum
                closing_time = h + 1
        return closing_time