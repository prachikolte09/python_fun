from typing import Any


RPN_Expression = [3,4,"+", 2 ,"*", 1, "+",9,9,"+"]

operators = { '+': lambda y, x: x + y,
              '-': lambda y, x: x - y,
              '*': lambda y, x: x * y,
              '/': lambda y, x: int(x/y) }


def rpn_solver(rpn_expression: Any) -> int :
    data = []
    for n in rpn_expression:
        if isinstance(n,int):
            data.append(n)

        elif n in operators:
            y = data.pop()
            x = data.pop()
            result = operators[n](y,x)
            data.append(result)
        else:
            raise ValueError("Unknown values")

    return sum(data)

result = rpn_solver(RPN_Expression)
print(f'result:{result}')
