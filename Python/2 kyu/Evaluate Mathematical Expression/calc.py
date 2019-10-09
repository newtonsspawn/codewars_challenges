import re


def calc(expression):
    
    repls = [
            ['/ -\(', '* -1 / ('],
            ['-\(', '-1 * ('],
            ['(?<=[\d\)])\)', ' )'],
            ['(?<=[\(])\(', ' ('],
            ['\((?=[\d\-])', '( '],
            ['(?<=[\d])\-', ' -'],
            ['(?<=[\d] )\-(?=[\d])', '- '],
            ['^\(', '1 * ('],
            ['(?<=\( )\(', '1 * (']
            ]
    
    string_old = expression
    for repl in repls:
        string_old = re.sub(repl[0], repl[1], string_old)
        
    print(string_old)
    
    string_old = (re.split(' ', string_old))
    string_new = []
    
    for item in string_old:
        if item not in '+-*/()':
            string_new.append(float(item))
        else:
            string_new.append(item)
    
    def index(lis, val):
        try:
            return lis.index(val)
        except ValueError:
            return None
    
    def math(exp, op):
        if op == '*':
            return exp[0] * exp[1]
        elif op == '/':
            return exp[0] / exp[1]
        elif op == '+':
            return exp[0] + exp[1]
        elif op == '-':
            return exp[0] - exp[1]
    
    def parens(temp, save=None):
        if save is None:
            save = []
        if index(temp, '('):
            start = index(temp, '(') + 1
            if index(temp[start:], '('):
                if index(temp[start:], '(') < index(temp[start:], ')'):
                    save.extend(temp[:start])
                    return parens(temp[start:], save)
            end = index(temp, ')')
            ans = operate(temp[start:end])
            del temp[start-1:end+1]
            temp.insert(start-1, ans)
            save.extend(temp)
            return parens(save)
        else:
            operate(temp)
        return temp[0]
        
    def operate(temp2):
        if len(temp2) == 1:
            return temp2[0]
        if index(temp2, '*') and index(temp2, '/'):
            op = min(index(temp2, '*'), index(temp2, '/'))
            ans = math([temp2[op - 1], temp2[op + 1]], temp2[op])
            del temp2[op - 1:op + 2]
            temp2.insert(op - 1, ans)
            if len(temp2) == 1:
                return temp2[0]
            return operate(temp2)
        elif index(temp2, '*'):
            op = index(temp2, '*')
            ans = math([temp2[op - 1], temp2[op + 1]], temp2[op])
            del temp2[op - 1:op + 2]
            temp2.insert(op - 1, ans)
            if len(temp2) == 1:
                return temp2[0]
            return operate(temp2)
        elif index(temp2, '/'):
            op = index(temp2, '/')
            ans = math([temp2[op - 1], temp2[op + 1]], temp2[op])
            del temp2[op - 1:op + 2]
            temp2.insert(op - 1, ans)
            if len(temp2) == 1:
                return temp2[0]
            return operate(temp2)
        elif index(temp2, '+') and index(temp2, '-'):
            op = min(index(temp2, '+'), index(temp2, '-'))
            ans = math([temp2[op - 1], temp2[op + 1]], temp2[op])
            del temp2[op - 1:op + 2]
            temp2.insert(op - 1, ans)
            if len(temp2) == 1:
                return temp2[0]
            return operate(temp2)
        elif index(temp2, '+'):
            op = index(temp2, '+')
            ans = math([temp2[op - 1], temp2[op + 1]], temp2[op])
            del temp2[op - 1:op + 2]
            temp2.insert(op - 1, ans)
            if len(temp2) == 1:
                return temp2[0]
            return operate(temp2)
        elif index(temp2, '-'):
            op = index(temp2, '-')
            ans = math([temp2[op - 1], temp2[op + 1]], temp2[op])
            del temp2[op - 1:op + 2]
            temp2.insert(op - 1, ans)
            if len(temp2) == 1:
                return temp2[0]
            return operate(temp2)
    
    return parens(string_new)


if __name__ == '__main__':
    print(calc('2 + 3 * 4 / 3 - 6 / 3 * 3 + 8'))
    print(calc('1 + 2 * 3 * 3 - 8'))
    print(calc('1 + 2 * 3 * (5 - 2) - 8'))
    print(calc('1 + 2 * 3 * (5 - (3 - 1)) - 8'))
    print(calc('4 + -(1)'))
    print(calc('4 - -(1)'))
    print(calc('4 * -(1)'))
    print(calc('4 / -(1)'))
    print(calc('-1'))
    print(calc('-(-1)'))
    print(calc('-(-(-1))'))
    print(calc('-(-(-(-1)))'))
    print(calc('(((((-1)))))'))
    print(calc('5 - 1'))
    print(calc('5- 1'))
    print(calc('5 -1'))
