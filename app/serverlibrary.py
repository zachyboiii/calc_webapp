

def merge(array, p, q, r, byfunc=None):
    nleft = q - p +1
    nright = r - q
    leftarray = array[p:q+1]
    rightarray = array[q+1:r+1]
    left = 0
    right = 0 
    dest = p
    while left < nleft and right < nright:
        if (byfunc(leftarray[left]) < byfunc(rightarray[right])) if byfunc else (leftarray[left] < rightarray[right]):
            array[dest] = leftarray[left]
            left += 1
        else:
            array[dest] = rightarray[right]
            right += 1
        dest += 1
    while left < nleft:
        array[dest] = leftarray[left]
        left += 1
        dest += 1
    while right < nright:
        array[dest] = rightarray[right]
        right += 1
        dest += 1
        

def mergesort_recursive(array, p, r, byfunc=None):
    if r - p > 0:
        q = (r+p) // 2
        mergesort_recursive(array, p, q, byfunc)
        mergesort_recursive(array, q+1, r, byfunc)
        merge(array, p, q, r, byfunc)

def mergesort(array, byfunc=None):
    mergesort_recursive(array, 0, len(array)-1, byfunc)

class Stack:
    def __init__(self):
        self.__items: list = []
        
    def push(self, item):
        self.__items.append(item)

    def pop(self):
        if self.is_empty:
            return None
        return self.__items.pop()

    def peek(self):
        if self.is_empty:
            return None
        return self.__items[-1]

    @property
    def is_empty(self) -> bool:
        if self.size == 0:
            return True
        else:
            return False

    @property
    def size(self):
        return len(self.__items)

class EvaluateExpression:
  valid_char = '0123456789+-*/() '
  operands: str = "0123456789"
  operators: str = "+-*/()"

  def __init__(self, string=""):
    self.expression = string

  @property
  def expression(self):
    return self._expression

  @expression.setter
  def expression(self, new_expr):
    valid = True
    for i in new_expr:
      if i not in self.valid_char:
        valid = False
        self._expression = ""

    if valid == True:
      self._expression = new_expr
  
  def insert_space(self):
    new_str = ""
    old_str = self.expression.replace(" ", "")
    i = 0
    print(self.expression)
    while i < len(old_str):
        char = old_str[i]
        # Case of negative numbers
        if char == '-' and (i == 0 or (old_str[i - 1] in self.operators and old_str[i+1] in self.operands)):
            new_str += f'{char}'
        elif char in self.operators:
            new_str += f' {char} '
        else:
            new_str += char
        i += 1
    return new_str

  def process_operator(self, operand_stack, operator_stack):
    op = operator_stack.pop()
    op2 = operand_stack.pop()
    op1 = operand_stack.pop()
    print(op1, op, op2)
    if op == '+':
        operand_stack.push(op1+op2)
    elif op == '-':
        operand_stack.push(op1-op2)
    elif op == '*':
        operand_stack.push(op1*op2)
    elif op == '/':
        if op2 == 0:
                raise ZeroDivisionError("Division by zero is not allowed.")
        operand_stack.push(op1//op2)
    else:
        operator_stack.push(op)
        operand_stack.push(op2)
        operand_stack.push(op1)

  def evaluate(self):
    operand_stack = Stack()
    operator_stack = Stack()
    expression = self.insert_space()
    print(expression)
    tokens = expression.split()
    print(tokens)
    for i in range(len(tokens)):
        token = tokens[i]
        print(token)
        # If the extracted character is an operand, push it to operand_stack
        if token in self.operands:
            operand_stack.push(int(token))
        # If extracted character is a negative number
        elif token.lstrip('- ').isdigit():  # Check if it's a number (allow negative numbers)
            operand_stack.push(-int(token.lstrip('- ')))
        # If the extracted character is + or - operator
        elif token == '+' or token == '-':
            # process all the operators as long as the operator_stack is not empty and the top of the operator_stack is not ( or ) symbols
            while not operator_stack.is_empty and (operator_stack.peek() not in ('(', ')')):
                # process all the operators at the top of the operator_stack
                self.process_operator(operand_stack, operator_stack)
            # and push the extracted operator to operator_stack
            operator_stack.push(token)
        # If the extracted character is a * or / operator
        elif token == '*' or token == '/':
            while (not operator_stack.is_empty and operator_stack.peek() in ("*", "/")):
                # process all the * or / operators at the top of the operator_stack
                self.process_operator(operand_stack, operator_stack)
            # push the extracted operator to operator_stack
            operator_stack.push(token)
        # If the extracted character is a ( symbol, push it to operator_stack
        elif token == '(':
            operator_stack.push(token)
        # If the extracted character is a ) symbol,
        elif token == ')':
            # repeatedly process the operators from the top of operator_stack until seeing the ( symbol on the stack.
            while not operator_stack.is_empty and operator_stack.peek() != '(':
                self.process_operator(operand_stack, operator_stack)
            if not operator_stack.is_empty:
                operator_stack.pop()
        elif token.isalpha():
            raise ValueError("Invalid Input.")
    
    # Repeatedly process the operators from the top of operator_stack until operator_stack is empty.
    while operator_stack.is_empty != True:
        self.process_operator(operand_stack, operator_stack)
    
    return operand_stack.peek()


def get_smallest_three(challenge):
  records = challenge.records
  times = [r for r in records]
  mergesort(times, lambda x: x.elapsed_time)
  return times[:3]





