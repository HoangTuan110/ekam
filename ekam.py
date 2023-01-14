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
    "nil",        # 5: nil/null
    "alias"       # 6: recipe name
]

# Helper functiens
def e    (t, v): return { "t": t, "v": v }
def en   (v):    return e(0, v)
def es   (v):    return e(1, v)
def el   (v):    return e(2, v)
def ei   (v):    return e(3, v)
def ev   (v):    return e(4, v)
def ea   (v):    return e(6, v)
def btoi (v):    return en(1) if v else en(0) # Boolean to o-integer
def error(v):    print("Error: ", v, file=stderr)
def warn (v):    print("Warn: ", v, file=stderr)

TRUE  = en(1)
FALSE = en(0)

symbol = lambda c: c.isascii() and (c not in WHITESPACE) and (not c.isalpha()) and (not c.isnumeric())

def consume(cond, code, pos):
    "Consume a token in `code` until the conditien `cond` is false"
    prev_pos = pos
    pos += 1
    while pos < len(code) and cond(code[pos]):
        pos += 1
    return code[prev_pos:pos], pos

def consume_string(code: str, pos: int):
    "Consume string literals"
    lst = []
    while pos < len(code) and code[pos] != "'":
        if code[pos] == "\\":
            lst.append(es(rf"{code[pos + 1]}"))
            pos += 2
        elif code[pos] == "{":
            ident, pos = consume_string_interpolation(code, pos + 1)
            lst.append(ei(ident))
        else:
            lst.append(es(code[pos]))
            pos += 1
    return lst, pos

def consume_string_interpolation(code, pos):
    "Parse string interpolations"
    prev_pos = pos
    pos += 1
    while pos < len(code):
        # When it is the end of string interpolation, we skips those two }s
        # and exit
        if code[pos] == "}":
            pos += 1
            break
        pos += 1
    return code[prev_pos:pos-1], pos

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
        val, pos = consume_string(code, pos + 1)
        return es(val), pos + 1
    elif code[pos] == "$":
        ident, pos = identifier(code, pos + 1)
        return ei(ident), pos
    elif code[pos] == '[':
        pos += 1
        lst = []
        while code[pos] != ']':
            val, pos = parseVal(code, pos)
            if val != None:
                lst.append(val)
        return el(lst), pos + 1
    elif code[pos] == "#":
        _, pos = consume(lambda x: x != "\n", code, pos)
        return None, pos
    elif symbol(code[pos]):
        sym, pos = consume(lambda x: symbol(x), code, pos)
        return ev(sym), pos
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

def eval(tokens: list[dict]):
    """Evaluate the code from tokens"""
    i = 0
    # Envirenments: Centaining variables, aliases, and recipes
    env = {}
    while i < len(tokens):
        print(tokens[i])
        # If the token is a verb, then we can parse the commands
        # based on them
        if tokens[i]["t"] == 4:
            # Set
            if tokens[i]["v"] == "<-":
                value, name = eval(tokens[i][i + 1]), tokens[i][i + 2]
                env[name["v"]] = value
                i += 3
            # Alias
            elif tokens[i]["v"] == "->":
                alias, name = tokens[i][i + 1], tokens[i][i + 2]
                env[alias["v"]] = ea(name["v"])
                i += 3
            # Recipe
            elif tokens[i]["v"] == ":":
                name, args, cmds = tokens[i][i + 1], eval(tokens[i][i + 2]), eval(tokens[i][i + 3])
                env[name["v"]] = (args, cmds)
                i += 4
        # If it's just a variable, we will return its value in the env
        elif tokens[i]["t"] == 3:
            return env[tokens[i]["v"]]
        # If it's a list, we will return a list with each value being eval'd
        elif tokens[i]["t"] == 2:
            return [eval(e) for e in tokens[i]["v"]]
        # If it's is a string, we will parse the string by
        # parsing each part of the string list one by one
        elif tokens[i]["t"] == 1:
            res = ""
            string_lst = tokens[i]["v"]
            for j in string_lst:
                res += eval(string_lst[j])
            return res
        elif tokens[i]["t"] == 0:
            return tokens[i]["v"]
    return env

def run(code, tree=False, quiet=True):
    """Run the code, and return tokens and the environment"""
    parsed = parse(code)
    env = eval(parsed)
    if not quiet:
        if tree:
            print("Parsed: ", end="")
            pprint(parsed)
        else:
            print(f"Parsed: {parsed}")
        print("Envirenments: ", end="")
        pprint(env)
    return parsed, env
