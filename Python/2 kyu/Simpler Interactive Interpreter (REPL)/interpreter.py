import re


def calc(expression):
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
        elif op == '%':
            return exp[0] % exp[1]
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
            del temp[start - 1:end + 1]
            temp.insert(start - 1, ans)
            save.extend(temp)
            return parens(save)
        else:
            operate(temp)
        return temp[0]
    
    def operate(temp2):
        if len(temp2) == 1:
            return temp2[0]
        if index(temp2, '*') and index(temp2, '/') and index(temp2, '%'):
            op = min(index(temp2, '*'), index(temp2, '/'), index(temp2, '%'))
            ans = math([temp2[op - 1], temp2[op + 1]], temp2[op])
            del temp2[op - 1:op + 2]
            temp2.insert(op - 1, ans)
            if len(temp2) == 1:
                return temp2[0]
            return operate(temp2)
        elif index(temp2, '*') and index(temp2, '/'):
            op = min(index(temp2, '*'), index(temp2, '/'))
            ans = math([temp2[op - 1], temp2[op + 1]], temp2[op])
            del temp2[op - 1:op + 2]
            temp2.insert(op - 1, ans)
            if len(temp2) == 1:
                return temp2[0]
            return operate(temp2)
        elif index(temp2, '*') and index(temp2, '%'):
            op = min(index(temp2, '*'), index(temp2, '%'))
            ans = math([temp2[op - 1], temp2[op + 1]], temp2[op])
            del temp2[op - 1:op + 2]
            temp2.insert(op - 1, ans)
            if len(temp2) == 1:
                return temp2[0]
            return operate(temp2)
        elif index(temp2, '%') and index(temp2, '/'):
            op = min(index(temp2, '%'), index(temp2, '/'))
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
        elif index(temp2, '%'):
            op = index(temp2, '%')
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
    
    return parens(expression)


# def tokenize(expression):
#     if expression == "":
#         return []
#     regex = re.compile("\s*(=>|[-+*\/\%=\(\)]|[A-Za-z_][A-Za-z0-9_]*|["
#                        "0-9]*\.?[0-9]+)\s*")
#     tokens = regex.findall(expression)
#     return [s for s in tokens if not s.isspace()]


def tokenize(expression):
    repls = [
            ['/ -\(', '* -1 / ('],
            ['-\(', '-1 * ('],
            ['(?<=[\d\)])\)', ' )'],
            ['(?<=[\(])\(', ' ('],
            ['\((?=[\d\-])', '( '],
            ['(?<=[\d])\-', ' -'],
            ['(?<=[\d] )\-(?=[\d])', '- '],
            ['(?<=\d)\+(?=\d)', ' + '],
            ['^\(', '1 * ('],
            ['(?<=\( )\(', '1 * (']
    ]
    string_old = expression
    for repl in repls:
        string_old = re.sub(repl[0], repl[1], string_old)
    string_old = (re.split(' ', string_old))
    string_new = []
    for item in string_old:
        if item not in '+-*/%()':
            string_new.append(float(item))
        else:
            string_new.append(item)
    return string_new


class Interpreter:
    
    def __init__(self):
        self.vars = {}
        self.functions = {}
    
    def assign(self, expression):
        var = expression[0]
        exp = self.var_replace(re.search('(?<=\=).+', expression)[0].strip())
        tokens = tokenize(exp)
        value = calc(tokens)
        return var, value
    
    def var_replace(self, expression):
        for i in [m for m in re.finditer(r'[a-z]+', expression)]:
            key = expression[i.start():i.end()]
            if key in self.vars.keys():
                expression = re.sub(key, str(self.vars[key]), expression)
            else:
                raise ValueError()
        return expression
    
    def input(self, expression):
        if not expression.strip():
            return ''
        elif re.search('(?<=\d)[a-z]', expression) is not None:
            raise ValueError(f"input: '{expression}'")
        elif re.search('(?<=\d)\s+(?=\d)', expression) is not None:
            raise ValueError(f"input: '{expression}'")
        elif re.search('=', expression) is not None:
            var, value = self.assign(expression)
            self.vars[var] = value
            return value
        else:
            try:
                expression = self.var_replace(expression)
            except ValueError:
                raise ValueError(f"input: '{expression}'")
            tokens = tokenize(expression)
            return calc(tokens)


if __name__ == '__main__':
    interpreter = Interpreter()
    
    # print(interpreter.input("1 + 1"))       # 2
    # print(interpreter.input("2 - 1"))       # 1
    # print(interpreter.input("2 * 3"))       # 6
    # print(interpreter.input("8 / 4"))       # 2
    # print(interpreter.input("7 % 4"))       # 3
    #
    # print(interpreter.input("x = 1"))       # 1
    # print(interpreter.input("x"))           # 1
    # print(interpreter.input("x + 3"))       # 4
    #
    # print(interpreter.input("y"))           # error
    # print(interpreter.input("y = x + 5"))   # 6
    # print(interpreter.input("y"))           # 6
    
    print(interpreter.input("1 2"))         # error
    # print(interpreter.input("1two"))        # error
