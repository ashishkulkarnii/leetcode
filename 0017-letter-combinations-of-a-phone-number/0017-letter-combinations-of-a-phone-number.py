def numMap(c):
    match c:
        case '2':
            return ['a', 'b', 'c']
        case '3':
            return ['d', 'e', 'f']
        case '4':
            return ['g', 'h', 'i']
        case '5':
            return ['j', 'k', 'l']
        case '6':
            return ['m', 'n', 'o']
        case '7':
            return ['p', 'q', 'r', 's']
        case '8':
            return ['t', 'u', 'v']
        case '9':
            return ['w', 'x', 'y', 'z']
        
def combinations(l1, l2):
    result = []
    for i in l1:
        for j in l2:
            result.append(i+j)
    return(result)

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        match len(digits):
            case 0:
                return []
            case 1:
                return numMap(digits[0])
            case 2:
                return combinations(numMap(digits[0]), numMap(digits[1]))
            case 3:
                return combinations(combinations(numMap(digits[0]), numMap(digits[1])), numMap(digits[2]))
            case 4:
                return combinations(combinations(numMap(digits[0]), numMap(digits[1])), combinations(numMap(digits[2]), numMap(digits[3])))