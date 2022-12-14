'''
This will be a Basic interpreter for the kattis problem: https://open.kattis.com/problems/basicinterpreter
For this problem, write an interpreter for a restricted dialect of BASIC. Here is a description of the language.

Each input line contains one statement. Each statement begins with a non-negative integer, which we will call its label.

 * LET X = <ARITHMETIC_STATEMENT>
    Assign the result of the arithmetic statement to variable X.
 * IF <CONDITION> THEN GOTO L
    If the boolean given is true, then go to the statement labeled L, 
    where L is a valid label. (If the condition is not true, continue 
    execution to the statement with the next lowest label.)
 * PRINT <PRINT_STATEMENT>
    Produce output, without an appended newline.
 * PRINTLN <PRINT_STATEMENT>
    Produce output, with an appended newline.
 * <ARITHMETIC_STATEMENT> 
    one of the following: X, X + Y, X - Y, X * Y, or X / Y where X and Y each indicate either a variable or an integer.
 * <CONDITION>
    one of the following: X = Y, X > Y, X < Y, X <> Y, X <= Y, or X >= Y. Again, X and Y each indicate either a 
    variable or an integer. Here, <> indicates inequality.
 * <PRINT_STATEMENT> 
    either a variable name or a literal string delimited by double quotes. Inside the quotes, the string contains 
    only alphanumeric characters (a-z, A-Z, 0-9) and spaces.

In the signed 32-bit arithmetic, the usual rules of truncation towards zero (for division) 
    and overflow (for addition and multiplication) and underflow (for subtraction) apply. 

Further, division by zero will not occur.

Program execution begins with the statement having the smallest label, and proceeds with the statement having the 
    next smallest label. (Unless a GOTO executes, in which case execution proceeds at the designated label.) 
    The program halts after it has completed the statement with the largest label (which is guaranteed not to contain a GOTO).

Input:
    Input consists of a single program. Each line contains a single valid statement. Each pair of adjacent tokens in the
        input is separated by a single space. Integers in the input will all be in the range  to . Input ends at end of file.

Output:
    Give the output (PRINT and PRINTLN statements) of the input program when it is executed.

'''

from typing import (
    List,
    Dict,
    Tuple
)


int32    : type = int
Label    : type = int
TokenType: type = str

Token     : type = Tuple[TokenType, str]
RawProgram: type = Dict[Label, str]
Program   : type = Dict[Label, List[Token]]

# Keyword tokens
PRINT   : TokenType = 'PRINT'
PRINTLN : TokenType = 'PRINTLN'
LET     : TokenType = 'LET'
IF      : TokenType = 'IF'
THEN    : TokenType = 'THEN'
GOTO    : TokenType = 'GOTO'

# Operator tokens
PLUS  : TokenType = '+'
MINUS : TokenType = '-'
TIMES : TokenType = '*'
DIVIDE: TokenType = '/'
EQUALS: TokenType = '='

# Relational operators
NE: TokenType = '<>'
LT: TokenType = '<'
GT: TokenType = '>'
LE: TokenType = '<='
GE: TokenType = '>='

# Other tokens
VARIABLE: TokenType = 'VARIABLE'
STRING  : TokenType = 'STRING'
INTEGER : TokenType = 'INTEGER'

Keywords: List[TokenType] = [
    PRINT,
    PRINTLN,
    LET,
    IF,
    THEN,
    GOTO,
    VARIABLE
]

Relations: List[TokenType] = [
    EQUALS,
    NE,
    LT,
    GT,
    LE,
    GE
]

Operators: List[TokenType] = [
    PLUS,
    MINUS,
    TIMES,
    DIVIDE
]

def Print(string: str):
    print(string, end='')

def Println(string: str):
    print(string)

def to_int32(x: int) -> int32:
    '''
        Convert a number to a 32-bit integer.
    '''
    val: int32 = int32(x)

    if x > 0xFFFFFFFF:
            raise OverflowError

    if x>0x7FFFFFFF:
        val = int32(0x100000000-x)
        if val < 2147483648:
            val *= -1
        else:
            val = -2147483648

    return val
        

def get_input() -> RawProgram:
    lines = 0
    # Read in the input
    input_lines = []

    while True:
        try:
            input_lines.append(input())
        except EOFError:
            break

    lines = len(input_lines)

    # Parse the input
    program = {}
    for line in input_lines:
        split_line = line.split()
        # print(split_line)
        lablel: Label = int(split_line[0])
        entry: str = ' '.join(split_line[1:])
        program[lablel] = entry
        
    return program


def tokenize(line: str) -> List[Token]:
    """
        Convert the string into a list of tokens.
    """

    length: int = len(line)
    pos: int = 0
    offset: int = 0
    tokens: List[Token] = []

    while(pos < length):
        char: str = line[pos]

        # Skip whitespace
        if char == ' ' or char == '\t':
            pos += 1
            continue
        
        # Check for String
        if char == '"':
            offset = 0
            pos += 1
            
            while(pos + offset < length):
                if line[pos + offset] == '"':
                    break
                offset += 1

            tokens.append((STRING, line[pos:pos+offset]))
            pos += offset + 1
            continue

        # Check for variable or keyword
        if char.isalpha():
            offset = 0
            while(pos + offset < length):
                if not line[pos + offset].isalpha():
                    break
                offset += 1

            token: str = line[pos:pos+offset]

            if token in Keywords:
                tokens.append((token, token))
            elif len(token) == 1 and token.isalpha() and token.isupper():
                tokens.append((VARIABLE, token))
            else:
                raise ValueError(f'Invalid token: {token}')

            pos += offset
            continue

        # Check for integer
        if char.isdigit():
            offset = 0
            while(pos + offset < length):
                if not line[pos + offset].isdigit():
                    break
                offset += 1

            tokens.append((INTEGER, line[pos:pos+offset]))
            pos += offset
            continue

        # Check for relations
        if char in ['=', '<', '>']:
            if pos + 1 < length and (line[pos + 1] == '=' or line[pos + 1] == '>'):
                for rel in Relations:
                    if line[pos:pos+2] == rel:
                        tokens.append((rel, rel))
                        pos += 2
                        break
            else:
                for rel in Relations:
                    if char == rel:
                        tokens.append((rel, rel))
                        pos += 1
                        break
            continue

        # Check for operators
        for operator in Operators:
            if char == operator:
                tokens.append((operator, operator))
                pos += 1
                break
            
            continue

        raise ValueError(f'Invalid token: {char}')

    return tokens

def main(): 
    print("Hello World")
    # lines = 0
    # # Read in the input
    # input_lines = []
    # while True:
    #     try:
    #         input_lines.append(input())
    #     except EOFError:
    #         break

    # program = {}
    # lines = len(input_lines)

    # # Parse the input
    # for line in input_lines:
    #     l = line.split()
    #     print(l)
    #     program[int(l[0])] = ' '.join(l[1:])
        

    #     # program.append(line.split())

    program = get_input()
    lines = len(program.keys())
    # program.sort(key=lambda x: int(x[0]))

    print(program)

    for key in program:
        print(key, ":", program[key])

    print()

    for i in range(lines):
        label = (i + 1) * 10
        print(label, program[label])

    # Run the program
    variables = {}
    line_number = 0
    while line_number < len(program):
        line = program[line_number][1:]
        if line[0] == "PRINT":
            if line[1] in variables:
                print(variables[line[1]])
            else:
                print(line[1])
        elif line[0] == "LET":
            variables[line[1]] = line[2]
        elif line[0] == "GOTO":
            line_number = int(line[1]) - 2
        elif line[0] == "IF":
            if line[1] in variables:
                if variables[line[1]] == line[3]:
                    line_number = int(line[5]) - 2
            else:
                if line[1] == line[3]:
                    line_number = int(line[5]) - 2
        line_number += 1
    

if __name__ == "__main__":
    
    main()