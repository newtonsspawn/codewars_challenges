import re

from decimal import Decimal


class Calculator(object):
    
    def evaluate(self, string):
        
        string_old = (re.split(' ', string))
        string_new = []
        
        for item in string_old:
            if item not in '+-*/':
                string_new.append(Decimal(item))
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
        
        def operate(temp):
            if len(temp) == 1:
                return temp[0]
            if index(temp, '*') and index(temp, '/'):
                op = min(index(temp, '*'), index(temp, '/'))
                ans = math([temp[op-1], temp[op+1]], temp[op])
                del temp[op-1:op+2]
                temp.insert(op-1, ans)
                operate(temp)
            elif index(temp, '*'):
                op = index(temp, '*')
                ans = math([temp[op-1], temp[op+1]], temp[op])
                del temp[op-1:op+2]
                temp.insert(op-1, ans)
                operate(temp)
            elif index(temp, '/'):
                op = index(temp, '/')
                ans = math([temp[op - 1], temp[op + 1]], temp[op])
                del temp[op-1:op+2]
                temp.insert(op - 1, ans)
                operate(temp)
            elif index(temp, '+') and index(temp, '-'):
                op = min(index(temp, '+'), index(temp, '-'))
                ans = math([temp[op-1], temp[op+1]], temp[op])
                del temp[op-1:op+2]
                temp.insert(op-1, ans)
                operate(temp)
            elif index(temp, '+'):
                op = index(temp, '+')
                ans = math([temp[op-1], temp[op+1]], temp[op])
                del temp[op-1:op+2]
                temp.insert(op-1, ans)
                operate(temp)
            elif index(temp, '-'):
                op = index(temp, '-')
                ans = math([temp[op - 1], temp[op + 1]], temp[op])
                del temp[op-1:op+2]
                temp.insert(op - 1, ans)
                operate(temp)
        
        operate(string_new)
        
        return float(string_new[0])


if __name__ == '__main__':
    
    calc = Calculator()
    
    print(calc.evaluate(string='127'))
    print(calc.evaluate(string='2 + 3'))
    print(calc.evaluate(string='2 - 3 - 4'))
    print(calc.evaluate(string='10 * 5 / 2'))
    print(calc.evaluate(string='2 / 2 + 3 * 4 - 6'))
    print(calc.evaluate(string='2 + 3 * 4 / 3 - 6 / 3 * 3 + 8'))
    print(calc.evaluate(string='1.1 + 2.2 + 3.3'))
    print(calc.evaluate(string='1.1 * 2.2 * 3.3'))
