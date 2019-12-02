# Build digit-by-digit addition rules
# Adder maintains pointers to a, b, and carry.
# Put result in b, zero out a, update carry.
# Switch to advance mode to move a by one (or zero-extend)
# Then move b by one digit (or zero-extend)

template = """    "A[{}]; B[{}]; C[{}]; R->A [a]; R->B [b]; R->C [carry]; R[adder]" :
    "A[{}]; B[{}]; C[{}]; R->A [a]; R->B [b]; R->C [carry]; R[adder_advance]","""

# Need to handle a = 0-9, b = 0-9, c = 0 or 1

for a in range( 0, 10 ):
    for b in range( 0, 10 ):
        for c in range( 0, 2 ):
            s = a + b + c
            b_prime = s % 10
            a_prime = "x"
            carry_out = s // 10

            print( template.format( a, b, c, a_prime, b_prime, carry_out ) )
            
