
alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

output = ["UNIQUE[unique]"]

for c in alphabet:
    output.append( "T{0}[letter]".format( c ) )
    output.append( "T{0}->UNIQUE [{0}]".format( c ) )

print( '"' + "; ".join( output ) + '"' )

template = """    "X[{0}]; U[letter]; UNIQUE[unique]; U->UNIQUE[{0}]" :
    "X[letter]; X->U; U[letter]; UNIQUE[unique]; U->UNIQUE[{0}]","""

print()
for c in alphabet:
    print( template.format( c ) )

template = """    "X[{0}];" :
    "X[token]; X->U; U[letter]; U->U[{0}]","""


print()
for c in alphabet:
    print( template.format( c ) )

template = """    "X[token]; Y[token]; XX[letter]; YY[letter]; X->XX; Y->YY; XX->XX [{0}]; YY->YY [{0}]" :
    "X[token]; Y[token]; XX[letter]; YY[letter]; X->XX; Y->YY; XX->XX [{0}]; YY->YY [{0}]; X--Y [eq]","""    

print()
for c in alphabet:
    print( template.format( c ) )

