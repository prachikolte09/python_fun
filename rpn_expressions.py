from typing import Any, List, Union

RPN_Expression = ["4","13","5","/","+"]

operators = {
    '+': lambda y, x: x + y,
    '-': lambda y, x: x - y,
    '*': lambda y, x: x * y,
    '/': lambda y, x: int(x / y)  # Ensure integer division
}

def rpn_solver(rpn_expression: List[Union[int, str]]) -> int:
    # data = []
    # for n in rpn_expression:
    #     if  (isinstance(n, str) and n.lstrip('-').isdigit()):  # Check if n is an integer or a digit string (including negatives)
    #         data.append(int(n))  # Convert to int if it's a string representation of a digit
    #     elif n in operators:
    #         if len(data) >= 2:
    #             y = data.pop()
    #             x = data.pop()
    #             result = operators[n](y, x)
    #             data.append(result)
    #
    #
    # return data[0]  # The result should be the only element left in the stack


    result = []

    for n in rpn_expression:

        if n.lstrip('-').isdigit():
            result.append(int(n))
        elif n in operators:
            if len(result) >= 2:

                x = result.pop()
                y = result.pop()
                val = operators[n](x,y)
                result.append(val)

    return result[0]

# Example usage
result = rpn_solver(RPN_Expression)
print(f'result: {result}')  # Output: 22
