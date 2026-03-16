class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        et = [0 for func in range(n)]
        stack = []
        t = 0
        for log in logs:
            log_split = log.split(":")
            func = int(log_split[0])
            start = log_split[1] == "start"
            t_ = int(log_split[2])
            if start:
                if stack:
                    et[stack[-1]] += t_ - t
                stack.append(func)
            else:
                t_ += 1
                if stack[-1] == func:
                    et[func] += t_ - t
                for i, f in list(enumerate(stack))[::-1]:
                    if f == func:
                        stack.pop(i)
                        break
            t = t_
        return et