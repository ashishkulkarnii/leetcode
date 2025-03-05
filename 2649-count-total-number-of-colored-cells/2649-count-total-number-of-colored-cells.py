"""minute-by-minute:
1. 1
2. 5 = 1 + 4
3. 13 = 5 + 8
4. 25 = 13 + 12
5. 41 = 25 + 16

we see that at nth minute, we are adding 4(n-1) blocks to the number of blocks at the (n-1)th minute.

```
blue_count(n) = blue_count(n-1) + 4 * (n - 1)
bc(0) = 0
bc(1) = 1
bc(2) = bc(1) + 4(2-1)
bc(3) = bc(2) + 4(3-1)
bc(4) = bc(3) + 4(4-1)
      = bc(2) + 4(3-1) + 4(4-1)
      = bc(1) + 4(2-1) + 4(3-1) + 4(4-1)
      = bc(1) + 4(1 + 2 + 3)
bc(n) = 1 + 4 * n * (n - 1) / 2
"""

class Solution:
    def coloredCells(self, n: int) -> int:
        return 1 + 2 * n * (n - 1)
