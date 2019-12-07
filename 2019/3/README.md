The solution strategy I tried here is:

* Convert the input into two unary strings of moves.
* Implement each move and record the locations in a radix tree (using binary digits)
* Find all locations in the radix tree visited by both wires, and output their keys.

The implementation isn't *too* difficult, but it's not efficient enough. The day 3 example problem takes more than 54 hours with this grammar.  (And I didn't find the minimum, though that can be done by hand.)

```
--------------------------------------------------------------------------------
    Grammar              Steps  Time  
  1 pad_input.json            2    0.0s
  2 convert_to_unary.json    226   88.4s
  3 off_by_one.json          20    4.2s
  4 follow_wire.json      24597 184808.8s
  5 extract_matches.json   3773 12255.5s
--------------------------------------------------------------------------------
100+10011011+
101110+10010010+
1011+10011011+
1100-10011110+
y+, x+
```
