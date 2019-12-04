template = """    "D[x]; PD[{}]; PD->D[next_char]; D->BASE [base]; BASE[{}]" :
    "D[x]; PD[x]; PD->D[next_char]; D->BASE [base]; BASE[{}]; PD->BIGGER [base]; BIGGER[{}]; PD->Q [quantity]; Q[{}]","""

bases = ["unit", "ten", "hundred", "thousand"]
for base, bigger in zip( bases, bases[1:] ):
    for digit in range( 10 ):
        print( template.format( digit, base,
                                base, bigger, digit ) )
            

template = """
    "B[{dir}]; B->A1[next_char]; A1[x]; A1->Q1[quantity]; Q1[{q}]; A1->U1 [base]; U1[{bigger}]" :
    "B[{dir}]; B->AX->A9->A8->A7->A6->A5->A4->A3->A2->A1[next_char]; 
     A1[x];       A1->Q1[quantity]; Q1[{q}]; A1->U1[base]; U1[{base}];
     A2[x];       A2->Q2[quantity]; Q2[{q}]; A2->U2[base]; U2[{base}];
     A3[x];       A3->Q3[quantity]; Q3[{q}]; A3->U3[base]; U3[{base}];
     A4[x];       A4->Q4[quantity]; Q4[{q}]; A4->U4[base]; U4[{base}];
     A5[x];       A5->Q5[quantity]; Q5[{q}]; A5->U5[base]; U5[{base}];
     A6[x];       A6->Q6[quantity]; Q6[{q}]; A6->U6[base]; U6[{base}];
     A7[x];       A7->Q7[quantity]; Q7[{q}]; A7->U7[base]; U7[{base}];
     A8[x];       A8->Q8[quantity]; Q8[{q}]; A8->U8[base]; U8[{base}];
     A9[x];       A9->Q9[quantity]; Q9[{q}]; A9->U9[base]; U9[{base}];
     AX[x];       AX->QX[quantity]; QX[{q}]; AX->UX[base]; UX[{base}];",
"""

directions = ['U', 'D', 'L', 'R']

for dir in directions:
    for base, bigger in zip( bases, bases[1:] ):
        for digit in range( 1, 10 ):
            print( template.format( dir=dir, q=digit, base=base, bigger=bigger ).replace( "\n", "" ) )


template = """
    "D[{dir}]; A[x]; B[x]; D->A->B[next_char]; A->Q[quantity]; A->U[base]; U[unit]; Q[0];" :
    "D[{dir}]; B[x]; D->B[next_char]",
    "D[{dir}]; A[x]; B[,]; D->A->B[next_char]; A->Q[quantity]; A->U[base]; U[unit]; Q[0];" :
    "D[{dir}]; B[x]; D->B[next_char]",
    "D[{dir}]; A[x]; B[x]; D->A->B[next_char]; A->Q[quantity]; A->U[base]; U[ten]; Q[0];" :
    "D[{dir}]; B[x]; D->B[next_char]",
    "D[{dir}]; A[x]; B[,]; D->A->B[next_char]; A->Q[quantity]; A->U[base]; U[ten]; Q[0];" :
    "D[{dir}]; B[x]; D->B[next_char]",
    "D[{dir}]; A[x]; B[x]; D->A->B[next_char]; A->Q[quantity]; A->U[base]; U[hundred]; Q[0];" :
    "D[{dir}]; B[x]; D->B[next_char]",
    "D[{dir}]; A[x]; B[,]; D->A->B[next_char]; A->Q[quantity]; A->U[base]; U[hundred]; Q[0];" :
    "D[{dir}]; B[x]; D->B[next_char]",
    "D[{dir}]; A[x]; B[x]; D->A->B[next_char]; A->Q[quantity]; A->U[base]; U[thousand]; Q[0];" :
    "D[{dir}]; B[x]; D->B[next_char]",
    "D[{dir}]; A[x]; B[,]; D->A->B[next_char]; A->Q[quantity]; A->U[base]; U[thousand]; Q[0];" :
    "D[{dir}]; B[x]; D->B[next_char]",

    "D[{dir}]; A[x]; D->A[next_char]; A->Q[quantity]; A->U[base]; U[unit]; Q[1];" :
    "D[{dir}]; A[{dir}]; D->A[next_char]",
    "D[{dir}]; A[x]; D->A[next_char]; A->Q[quantity]; A->U[base]; U[unit]; Q[2]" :
    "D[{dir}]; A2[{dir}]; A[{dir}]; D->A2->A[next_char]",
    "D[{dir}]; A[x]; D->A[next_char]; A->Q[quantity]; A->U[base]; U[unit]; Q[3]" :
    "D[{dir}]; A3[{dir}]; A2[{dir}]; A[{dir}]; D->A3->A2->A[next_char]",
    "D[{dir}]; A[x]; D->A[next_char]; A->Q[quantity]; A->U[base]; U[unit]; Q[4]" :
    "D[{dir}]; A4[{dir}]; A3[{dir}]; A2[{dir}]; A[{dir}]; D->A4->A3->A2->A[next_char]",
    "D[{dir}]; A[x]; D->A[next_char]; A->Q[quantity]; A->U[base]; U[unit]; Q[5]" :
    "D[{dir}]; A5[{dir}]; A4[{dir}]; A3[{dir}]; A2[{dir}]; A[{dir}]; D->A5->A4->A3->A2->A[next_char]",
    "D[{dir}]; A[x]; D->A[next_char]; A->Q[quantity]; A->U[base]; U[unit]; Q[6]" :
    "D[{dir}]; A6[{dir}]; A5[{dir}]; A4[{dir}]; A3[{dir}]; A2[{dir}]; A[{dir}]; D->A6->A5->A4->A3->A2->A[next_char]",
    "D[{dir}]; A[x]; D->A[next_char]; A->Q[quantity]; A->U[base]; U[unit]; Q[7]" :
    "D[{dir}]; A7[{dir}]; A6[{dir}]; A5[{dir}]; A4[{dir}]; A3[{dir}]; A2[{dir}]; A[{dir}]; D->A7->A6->A5->A4->A3->A2->A[next_char]",
    "D[{dir}]; A[x]; D->A[next_char]; A->Q[quantity]; A->U[base]; U[unit]; Q[8]" :
    "D[{dir}]; A8[{dir}]; A7[{dir}]; A6[{dir}]; A5[{dir}]; A4[{dir}]; A3[{dir}]; A2[{dir}]; A[{dir}]; D->A8->A7->A6->A5->A4->A3->A2->A[next_char]",
    "D[{dir}]; A[x]; D->A[next_char]; A->Q[quantity]; A->U[base]; U[unit]; Q[9]" :
    "D[{dir}]; A9[{dir}]; A8[{dir}]; A7[{dir}]; A6[{dir}]; A5[{dir}]; A4[{dir}]; A3[{dir}]; A2[{dir}]; A[{dir}]; D->A9->A8->A7->A6->A5->A4->A3->A2->A[next_char]",
"""

for dir in directions:
    print( template.format( dir=dir ) )
