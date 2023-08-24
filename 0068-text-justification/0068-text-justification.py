class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        line = []
        result = []
        for word in words:
            if len(' '.join(line) + ' ' + word) <= maxWidth:
                line.append(word)
            else:
                result.append(line)
                line = []
                line.append(word)
        result.append(line)
        
        for i in range(len(result) - 1):
            for spaces in range(maxWidth):
                if len(result[i]) == 1:
                    result[i] = result[i][0] + (maxWidth - len(result[i][0])) * ' '
                    break
                if len((spaces * ' ').join(result[i])) == maxWidth:
                    result[i] = (spaces * ' ').join(result[i])
                    break
                if len((spaces * ' ').join(result[i])) >= maxWidth:
                    extra = maxWidth - len(((spaces - 1) * ' ').join(result[i])) + 1
                    temp = result[i]
                    result[i] = ((spaces) * ' ').join(temp[:extra:])
                    result[i] += (spaces - 1) * ' ' + ((spaces - 1) * ' ').join(temp[extra::])
                    break
        
        result[-1] = ' '.join(result[-1])
        result[-1] += (maxWidth - len(result[-1])) * ' '
        
        if result[0] == []:
            result.pop(0)
        
        return result