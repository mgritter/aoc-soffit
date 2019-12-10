dp = {}

for num_remaining in [1]:
    for digit in [3,4,5,6,7,8,9]:
        dp[(digit,num_remaining,True)] = 1
        dp[(digit,num_remaining,False)] = 10 - digit
            
for num_remaining in [2,3,4,5]:
    for digit in [3,4,5,6,7,8,9]:
        # True 
        n = ( dp[(digit,num_remaining-1,False)] +
              sum( dp[(next_digit,num_remaining-1,True)]
                   for next_digit in range( digit + 1, 10 ) ) )
        dp[(digit,num_remaining,True)] = n
        # False 
        n = sum( dp[(next_digit,num_remaining-1,False)]
                 for next_digit in range( digit, 10 ) )
        dp[(digit,num_remaining,False)] = n


# 3xx, True has possibilties
# 333 334 335 336 337 338 339
# 344 355 366 377 388 399
# N(3,2,True) = 13, check
#
# 3xx, False has possibilities
# 333 334 335 336 337 338 339
# 344 345 346 347 348 349 
# 355 356 357 358 359
# 366 367 368 369
# 377 378 379
# 388 389
# 399
# N(3,2,False) = 28, check

for num_remaining in [1,2,3,4,5]:
    for digit in [3,4,5,6,7,8,9]:
        for need_double in [False,True]:
            n = dp[(digit,num_remaining,need_double)]
            print( "N({},{},{}) = {} = {}_2R".format( digit, num_remaining, need_double,
                                                      n,
                                                      "".join(reversed(bin(n)[2:]))
                                                      ))

# Input: 367479-893698
# 3xxxxx but not 33xxxx 34xxxx 35xxxx 366xxx 
# 4xxxxx
# 5xxxxx
# 6xxxxx
# 7xxxxx
# 8xxxxx but not 89xxxx
soln_p = dp[(3,5,True)] + dp[(4,5,True)] + dp[(5,5,True)] + dp[(6,5,True)] + dp[(7,5,True)] + dp[(8,5,True)]
soln_m = dp[(3,4,False)] + dp[(4,4,True)] + dp[(5,4,True)] + dp[(6,3,False)] + dp[(9,4,False)]

print( soln_p, "-", soln_m, "=", soln_p - soln_m )
