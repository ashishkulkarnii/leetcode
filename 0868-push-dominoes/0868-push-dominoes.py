class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        while "R." in dominoes or ".L" in dominoes:
            dominoes = dominoes.replace("R.L", "^")
            dominoes = dominoes.replace("R.", "RR").replace(".L", "LL")
        dominoes = dominoes.replace("^", "R.L")
        return dominoes