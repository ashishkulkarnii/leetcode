class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        score = 0
        tokens.sort()
        if(0 == len(tokens)):
            return 0
        while(power > -1 and len(tokens) > 1):
            if(tokens[0] <= power):
                    power -= tokens[0]
                    tokens.pop(0)
                    score += 1
            elif score >= 1:
                    power += tokens[-1]
                    tokens.pop(-1)
                    score -= 1
            else:
                break
        if tokens[0] <= power:
            power -= tokens[0]
            tokens.pop(0)
            score += 1
        return score