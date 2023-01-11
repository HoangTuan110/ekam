"""
Ekam - The command runner for masochists
"""

from sys import stderr
from pprint import pprint

WHITESPACE = " \t\n\r\f"

TYPES = [
    "number",     # 0: value
    "string",     # 1: value
    "list",       # 2: array
    "identifier", # 3: name
    "verb",       # 4: name
    "nil"         # 5: nil/null
]

# Environments: Containing variables, aliases, and recipes
global_env = {}

# Helper functions
def o    (t, v): return { "t": t, "v": v }
def on   (v):    return o(0, v)
def os   (v):    return o(1, v)
def ol   (v):    return o(2, v)
def oi   (v):    return o(3, v)
def ov   (v):    return o(4, v)
def btoi (v):    return on(1) if v else on(0) # Boolean to o-integer
def error(v):    print("Error: ", v, file=stderr)
def warn (v):    print("Warn: ", v, file=stderr)

TRUE  = on(1)
FALSE = on(0)

symbol = lambda c: c.isascii() and (c not in WHITESPACE) and (not c.isalpha()) and (not c.isnumeric())

def consume(cond, code, pos):
    "Consume a token in `code` until the condition `cond` is false"
    prev_pos = pos
    pos += 1
    while pos < len(code) and cond(code[pos]):
        pos += 1
    return code[prev_pos:pos], pos

def consume_string(env: dict, code: str, pos: int):
    "Consume string literals"
    tmp = ""
    while pos < len(code) and code[pos] != "'":
        if code[pos] == "\\":
            tmp += rf"{code[pos + 1]}"
            pos += 2
        elif code[pos] == "$":
            ident, pos = identifier(code, pos)
            tmp += env[ident]
        else:
            tmp += code[pos]
            pos += 1
    return tmp, pos

def identifier(code, pos):
    "Consume an identifier"
    prev_pos = pos
    pos += 1
    if code[pos].isalpha():
        while pos < len(code) and (code[pos].isalpha() or code[pos].isnumeric() or code[pos] in "_-"):
            pos += 1
    return code[prev_pos:pos], pos

def parseVal(code, pos):
    if code[pos] == "'":
        val, pos = consume_string(global_env, code, pos + 1)
        return os(val), pos + 1
    elif code[pos] == "$":
        ident, pos = identifier(code, pos + 1)
        return oi(ident), pos
    elif code[pos] == '[':
        pos += 1
        lst = []
        while code[pos] != ']':
            val, pos = parseVal(code, pos)
            if val != None:
                lst.append(val)
        return ol(lst), pos + 1
    elif code[pos] == "#":
        _, pos = consume(lambda x: x != "\n", code, pos)
        return None, pos
    elif symbol(code[pos]):
        sym, pos = consume(lambda x: symbol(x), code, pos)
        return ov(sym), pos
    elif code[pos] in WHITESPACE:
        return None, pos + 1
    return None, pos + 1

def parse(code):
    pos = 0
    lst = []
    while pos < len(code):
        val, pos = parseVal(code, pos)
        lst.append(val)
    lst = list(filter(lambda x: x != None, lst))
    return lst

def format(o):
    "Format an object"
    if isinstance(o, list):
        return format(o[0])
    if o["t"] == 2:                  # Lists
        return [format(obj) for obj in o["v"]]
    elif o["t"] == 3 or o["t"] == 4: # Identifiers/Verbs
        return f'{o["v"]}'
    else:                            # Numbers/Strings/Other literals
        return o["v"]

def eval(tokens):
    """Evaluate the code from tokens"""
    i = 0
    while i < len(tokens):
        # Set
        if tokens[i]["v"] == "<-":
            value, name = tokens[i + 1], tokens[i + 2]
            env[name["v"]] = value["v"]
            i += 3
        else:
            i += 1

def run(code, tree=False):
    """Run the code"""
    parsed = parse(code)
    if tree:
        print("Parsed: ", end="")
        pprint(parsed)
    else:
        print(f"Parsed: {parsed}")
    eval(parsed)
    print("Environments: ", end="")
    pprint(env)
