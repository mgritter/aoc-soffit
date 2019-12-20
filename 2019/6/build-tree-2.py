alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"


# Tokenizer

template = """    "X[{0}];" :
    "X[token]; X->U; U[letter]; U->U[{0}]","""

print()
for c in alphabet:
    print( template.format( c ) )

# Tree labeling
template = """    "PARENT[node]; PARENT->NODE [unlabeled]; NODE[node]; NODE->TOKEN [label]; TOKEN[token]; TOKEN->LETTER; LETTER[letter]; LETTER->LETTER [{0}] " :
    "PARENT[node]; PARENT->NODE [{0}];         NODE[node];                      TOKEN[token]; TOKEN->LETTER; LETTER[letter]; LETTER->LETTER [{0}] ","""

print()
for c in alphabet:
    print( template.format( c ) )

# Tree merging
template = """    "PARENT[node]; PARENT->NODE1 [{0}]; NODE1[node]; PARENT->NODE2[{0}]; NODE2[node];" :
    "PARENT[node]; PARENT->NODE1 [{0}]; NODE1^NODE2[node];","""


for c in alphabet:
    print( template.format( c ) )
    
# Doubled letter cleanup

template = """    "X[token]; X->L1; L1[letter]; L1->L1[{0}]; X->L2; L2[letter]; L2->L2[{0}]" :
    "X[token]; X->L1; L1^L2[letter]; L1->L1[{0}];","""

for c in alphabet:
    print( template.format( c ) )
