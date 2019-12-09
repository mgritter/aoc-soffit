
Idea: implement a 3-D dynamic programming solution

```
N( digit, num remaining digits, need_double )
```

Base cases:

```
N( digit, 1, true ) = 1
N( digit, 1, false ) = 10 - digit    (digit, digit+1, digit+2, ... 9)
```

Recurrence:
```
N( digit, num remaining digits, true ) =o
  N( digit, num_remaining_digits - 1, false ) +
  N( digit + 1, num_remaining_digits - 1, true ) +
  N( digit + 2, num_remaining_digits - 1, true ) +
  ...
  N( 9, num_remaining_digits - 1, true )`

N( digit, num remaining digits, false ) =
  N( digit, num_remaining_digits - 1, false ) +
  N( digit + 1, num_remaining_digits - 1, false ) +
  N( digit + 2, num_remaining_digits - 1, false ) +
  ...
  N( 9, num_remaining_digits - 1, false )
```

For the input bounds

```
367479-893698
```

we have to subtract 33xxxx, 35xxxx, 366xxx and 89xxxx.

We can represent each position in the DP via a node:

```
N->X [digit]; N->Y [remaining]; N->Z [need_double];
```

With an extra edge `N->V [val]` for evaluation.

If we try to construct these bottom-up, we need a mechanism to create each intermediate state just once.

If we construct them top-down, we need to merge duplicates, but the number of nodes created before merging
could be very large.
