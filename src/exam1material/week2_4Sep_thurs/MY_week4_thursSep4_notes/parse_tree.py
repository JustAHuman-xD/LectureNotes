operators = {
    "implies": {
        "i": 0,
        "left_to_right": False,
        "symbols": ["->:", "->", "→"]
    },
    "and": {
        "i": 1,
        "left_to_right": True,
        "symbols": ["&", "∧"]
    },
    "or": {
        "i": 2,
        "left_to_right": True,
        "symbols": ["|", "∨", "v", "V"]
    },
    "not": {
        "i": 3,
        "left_to_right": False,
        "symbols": ["!", "¬"]
    }
}

expression = input("Enter your expression: ")
pieces = []

def parse_tree(depth, piece, pieces):
    foundS = None
    found = None
    for props in operators.values():
        for symbol in props["symbols"]:
            if symbol in piece and (found is None or props["i"] < found["i"]):
                foundS = symbol
                found = props
                break
    
    layer = []
    if len(pieces) > depth:
        layer = pieces[depth]
    else:
        pieces.append(layer)

    if found is None:
        layer.append(piece)
        return
    
    layer.append(foundS)
    left_to_right = props["left_to_right"]
    index = piece.find(foundS)
    if not left_to_right:
        index = piece.rfind(foundS)
    left = piece[:index - 1]
    right = piece[index + len(foundS)::]

    parse_tree(depth + 1, left, pieces)
    parse_tree(depth + 1, right, pieces)

parse_tree(0, expression, pieces)

print(pieces)

"""
     &
   /   \
  |     |
 / \   / \
p   q r   s
"""