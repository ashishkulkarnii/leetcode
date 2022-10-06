class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        return [("Fizz" if i % 3 == 0 else "") + ("Buzz" if i % 5 == 0 else "") + (str(i) if i % 3 and i % 5 else "") for i in range(1, n+1)]