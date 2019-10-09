import re
import math


def diff(s):
    
    def function_add(f, g):
        _f, _g = derive(f), derive(g)
        args = [_f, _g]
        return {'type': 'apply', 'operator': '+', 'args': args}
    
    def function_min(f, g):
        _f, _g = derive(f), derive(g)
        args = [_f, _g]
        return {'type': 'apply', 'operator': '-', 'args': args}
    
    def function_mul(f, g):
        _f, _g = derive(f), derive(g)
        args = []
        if (_f['type'] == 'value') and (g['type'] == 'value'):
            args.append({'type': 'value',
                         'value': float(_f['value']) * float(g['value'])})
        else:
            args.append({'type': 'apply', 'operator': '*', 'args': [_f, g]})
        if (f['type'] == 'value') and (_g['type'] == 'value'):
            args.append({'type': 'value',
                         'value': float(f['value']) * float(_g['value'])})
        else:
            args.append({'type': 'apply', 'operator': '*', 'args': [f, _g]})
        if (args[0]['type'] == 'value') and (args[1]['type'] == 'value'):
            return {'type': 'value', 'value': args[0] + args[1]}
        else:
            return {'type': 'apply', 'operator': '+', 'args': args}
        
    def function_div(f, g):
        _f, _g = derive(f), derive(g)
        args = []
        args.append({'type': 'apply', 'operator': '*', 'args': [_f, g]})
        args.append({'type': 'apply', 'operator': '*', 'args': [f, _g]})
        dividend = {'type': 'apply', 'operator': '-', 'args': args}
        divisor = {'type': 'apply', 'operator': '*', 'args': [g, g]}
        return {'type': 'apply', 'operator': '/', 'args': [dividend, divisor]}
    
    def function_pow(f, n):
        if (f['type'] == 'variable') and (n['type'] == 'value'):
            if float(n['value'] == 2):
                return {'type': 'apply', 'operator': '*', 'args': [n, f]}
            _n = derive(n)
            _n['value'] = n['value'] - 1
            return {'type': 'apply', 'operator': '*',
                    'args': [n, {'type': 'apply', 'operator': '^',
                                 'args': [f, _n]}]}
        elif (f['type'] == 'apply') and (n['type'] == 'value'):
            if float(n['value']) == 2:
                return {'type': 'apply', 'operator': '*', 'args': [n, f]}
            _n = derive(n)
            _n['value'] = n['value'] - 1
            return {'type': 'apply', 'operator': '*',
                    'args': [n, {'type': 'apply', 'operator': '^',
                                 'args': [f, _n]}]}
    
    def function_sin(x):
        if x['type'] == 'variable':
            return {'type': 'apply', 'operator': 'cos', 'args': [x['value']]}
        elif x['type'] == 'value':
            return math.cos(float(x['value']))
        elif x['type'] == 'apply':
            args = []
            args.append(derive(x))
            args.append({'type': 'apply', 'operator': 'cos', 'args': [x]})
            return {'type': 'apply', 'operator': '*', 'args': args}
    
    def function_cos(x):
        if x['type'] == 'variable':
            return {'type': 'apply', 'operator': '*',
                    'args': [{'type': 'value', 'value': -1},
                             {'type': 'apply', 'operator': 'sin',
                              'args': [x['value']]}]}
        elif x['type'] == 'value':
            return -1 * math.sin(float(x['value']))
        elif x['type'] == 'apply':
            args = []
            args.append({'type': 'apply', 'operator': '*',
                         'args': [{'type': 'value', 'value': -1}, derive(x)]})
            args.append({'type': 'apply', 'operator': 'sin', 'args': [x]})
            return {'type': 'apply', 'operator': '*', 'args': args}
    
    def function_tan(x):
        if x['type'] == 'variable':
            args = [{'type': 'value', 'value': 1},
                    {'type': 'apply', 'operator': '^',
                     'args': [{'type': 'apply', 'operator': 'tan',
                               'args': [x['value']]},
                              {'type': 'value', 'value': 2}]}]
            return {'type': 'apply', 'operator': '+', 'args': args}
        elif x['type'] == 'value':
            return 1 + math.pow(math.tan(float(x['value'])), 2)
        elif x['type'] == 'apply':
            args = [{'type': 'value', 'value': 1},
                    {'type': 'apply', 'operator': '^',
                     'args': [{'type': 'apply', 'operator': 'tan', 'args': [x]},
                              {'type': 'value', 'value': 2}]}]
            return {'type': 'apply', 'operator': '*',
                    'args': [derive(x), {'type': 'apply', 'operator': '+',
                                         'args': args}]}
    
    def function_exp(x):
        if x['type'] == 'variable':
            return {'type': 'apply', 'operator': 'exp', 'args': [x['value']]}
        elif x['type'] == 'value':
            return math.exp(float(x['value']))
        elif x['type'] == 'apply':
            return {'type': 'apply', 'operator': '*',
                    'args': [derive(x),
                             {'type': 'apply', 'operator': 'exp', 'args': [x]}]}
    
    def function_ln(x):
        if x['type'] == 'variable':
            return {'type': 'apply', 'operator': '/',
                    'args': [{'type': 'value', 'value': 1}, x['value']]}
        elif x['type'] == 'value':
            return 1 / float(x['value'])
        elif x['type'] == 'apply':
            return {'type': 'apply', 'operator': '*',
                    'args': [derive(x),
                             {'type': 'apply', 'operator': '/',
                              'args': [{'type': 'value', 'value': 1}, x]}]}
    
    env = {
            '+':    function_add,
            '-':    function_min,
            '*':    function_mul,
            '/':    function_div,
            '^':    function_pow,
            'sin':  function_sin,
            'cos':  function_cos,
            'tan':  function_tan,
            'exp':  function_exp,
            'ln':   function_ln
    }
    
    def reduce(args):
        if (not isinstance(args, list)) or (len(args) < 3):
            return args
        [val1, op, val2] = args
        if str(val1) == str(val2):
            if op == '+':
                return [float(2), '*', val2]
            elif op == '-':
                return 0
            elif op == '*':
                return [val1, '^', float(2)]
            elif op == '/':
                return 1
        return [val1, op, val2]
    
    def reduce_plus(val1, op, val2):
        if (op == '+') or (op == '-'):
            if val1 == 0:
                return val2
            elif val2 == 0:
                return val1
            else:
                return [val1, op, val2]
        elif op == '*':
            if val1 == 0:
                return 0
            elif val2 == 0:
                return 0
            elif val1 == 1:
                return val2
            elif val2 == 1:
                return val1
            else:
                return [val1, op, val2]
        elif op == '/':
            if val1 == 0:
                return 0
            else:
                return [val1, op, val2]
        else:
            return [val1, op, val2]
    
    def calc(val1, op, val2):
        if all([isinstance(val1, (float, int)),
                isinstance(val2, (float, int))]):
            if op == '+':
                return val1 + val2
            elif op == '-':
                return val1 - val2
            elif op == '*':
                return val1 * val2
            elif op == '/':
                return val1 / val2
        return [val1, op, val2]
    
    def format_final(arr):
        return arr
    
    def convert(operation):
        if not isinstance(operation, dict):
            return operation
        if (operation['type'] != 'apply'):
            if 'value' in operation.keys():
                return operation['value']
            else:
                return operation
        else:
            if len(operation['args']) < 2:
                result = {'type': 'func', 'body': []}
                temp = convert_plus(operation)
                result['body'] = ('(' + ' '.join(temp['body']) + ')')
                return result
            if isinstance(operation['operator'], dict) and \
                    ('name' in operation['operator'].keys()):
                operator = operation['operator']['name']
            else:
                operator = operation['operator']
            result = {'type': 'func', 'body': []}
            left = convert(operation['args'][0])
            if isinstance(left, dict) and ('body' in left.keys()):
                left = left['body']
            result['body'].append(left)
            result['body'].append(operator)
            right = convert(operation['args'][1])
            if isinstance(right, dict) and ('body' in right.keys()):
                right = right['body']
            result['body'].append(right)
            result['body'] = calc(*result['body'])
            if isinstance(result['body'], (float, int)):
                return result['body']
            result['body'] = reduce_plus(*result['body'])
            if isinstance(result['body'], (float, int)):
                return result['body']
            result['body'] = reduce(result['body'])
            if (not isinstance(result['body'], list)) or \
                    (len(result['body']) < 3):
                return result
            if isinstance(result['body'][0], (float, int)):
                b0 = f"{result['body'][0]:.5g}"
            else:
                b0 = result['body'][0]
            if isinstance(result['body'][2], (float, int)):
                b2 = f"{result['body'][2]:.5g}"
            else:
                b2 = result['body'][2]
            result['body'] = ('(' + ' '.join([result['body'][1], b0, b2]) + ')')
            return result
    
    def convert_plus(operation):
        if isinstance(operation['operator'], dict) and \
                ('name' in operation['operator']):
            operator = operation['operator']['name']
        else:
            operator = operation['operator']
        result = {'type': 'func', 'body': []}
        left = convert(operation['args'][0])
        if isinstance(left, dict) and ('body' in left.keys()):
            left = left['body']
        result['body'].append(operator)
        result['body'].append(left)
        return result
    
    def parse(program):
        result = parse_expr(program)
        if len(program) > 0:
            raise SyntaxError(f'Unexpected text after program')
        return result
        
    def parse_expr(program):
        match_num = re.search(r'^\d+.?\d*\b', program[0])
        match_wrd = re.search(r'^[^\s()"]+', program[0])
        if match_num:
            expr = {'type': 'value', 'value': float(match_num[0])}
        elif program[0] == 'x':
            expr = {'type': 'variable', 'value': 'x'}
        elif program[0] == '(':
            expr = {'type': 'delimiter', 'value': '('}
        elif match_wrd:
            expr = {'type': 'word', 'name': match_wrd[0]}
        else:
            raise SyntaxError(f'Unexpected syntax: {program[0]}')
        program.pop(0)
        return parse_apply(expr, program)
    
    def parse_apply(expr, program):
        if expr['type'] != 'delimiter':
            return expr
        expr = {'type': 'apply', 'operator': parse_expr(program), 'args': []}
        while (len(program) > 0) and (program[0] != ')'):
            arg = parse_expr(program)
            expr['args'].append(arg)
        if program[0] != ')':
            raise SyntaxError("Expected ')'")
        program.pop(0)
        return parse_apply(expr, program)
    
    def derive(expr):
        if expr['type'] == 'value':
            return {'type': 'value', 'value': 0}
        elif expr['type'] == 'variable':
            return {'type': 'value', 'value': 1}
        elif expr['type'] == 'apply':
            if expr['operator']['name'] in env:
                result = env[expr['operator']['name']](*expr['args'])
                return result
            else:
                raise TypeError('Applying a non-function')
    
    def function(expr):
        regex = re.compile(r'\s*(=>|[-+*/%=()]|[A-Za-z_][A-Za-z0-9_]*|['
                           r'0-9]*\.?[0-9]+)\s*')
        tokens = re.split(regex, expr)
        tokens = [i for i in tokens if not re.search(r'^\s*$', i)]
        result = convert(derive(parse(tokens)))
        
        if isinstance(result, (float, int)):
            return f'{result:.5g}'
        elif result['type'] == 'func':
            return format_final(result['body'])
        else:
            return result
        
    print(f'Expression: {s}')
    result = function(s)
    print(f'Derivative: {result}')
    
    return result


if __name__ == '__main__':
    print(diff("(tan x)"))  # three possible
    print(diff("5"))  # '0'
    print(diff("x"))  # '1'
    print(diff("(+ x x)"))  # '2'
    print(diff("(- x x)"))  # '0'
    print(diff("(* x 2)"))  # '2'
    print(diff("(/ x 2)"))  # '0.5'
    print(diff("(^ x 2)"))  # '(* 2 x)'
    print(diff("(cos x)"))  # '(* -1 (sin x))'
    print(diff("(sin x)"))  # '(cos x)'
    print(diff("(exp x)"))  # '(exp x)'
    print(diff("(ln x)"))  # '(/ 1 x)'
    print(diff("(+ x (+ x x))"))  # '3'
    print(diff("(- (+ x x) x)"))  # '1'
    print(diff("(* 2 (+ x 2))"))  # '2'
    print(diff("(/ 2 (+ 1 x))"))  # '(/ -2 (^ (+ 1 x) 2))'
    print(diff("(cos (+ x 1))"))  # '(* -1 (sin (+ x 1)))'
    print(diff("(sin (+ x 1))"))  # '(cos (+ x 1))'
    print(diff("(sin (* 2 x))"))  # '(* 2 (cos (* 2 x)))'
    print(diff("(exp (* 2 x))"))  # '(* 2 (exp (* 2 x)))'
    print(diff("(tan (* 2 x))"))  # three possible
    print(diff("(cos (* 2 x))"))  # two possible
    print(diff("(* x 41)"))  # '41'
    print(diff("(cos (+ x 41))"))  # '(* -1 (sin (+ x 41)))'
    print(diff("(sin (* 41 x))"))  # '(* 41 (cos (* 41 x)))'
