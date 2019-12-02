import json

# Build digit-by-digit division rules for division by 3
# 
# We need to handle 00 through 99, and then carries (10)0 through (29)9.
#

template = """    "C[div_position]; C->D; D[{}]; E[{}]; D->E[next_char]" : 
    "C[div_position]; C->E; D[{}]; E[{}]; D->E[next_char]","""

for dividend in range( 0, 30 ):
    for next_digit in range( 0, 10 ):
        quotient = dividend // 3
        remainder = dividend % 3
        next_with_carry = remainder * 10 + next_digit
        print( template.format( dividend, next_digit,
                                quotient, next_with_carry ) )
        
