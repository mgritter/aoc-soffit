## Design notes

It's possible but tedious to construct a fixed-sized grid node by node,
so I took a shortcut and created a single production that makes the
25x6 grid for this problem.

I needed to substantially improve the performance of Soffit to handle
graphs of this size.  The eventual run time for part 1 was:

```
--------------------------------------------------------------------------------
    Grammar              Steps  Time  
  1 read_layers.json      15102 22961.7s
  2 count_per_layer.json  16467 98574.1s
  3 reverse_tokens.json    5414 4828.4s
--------------------------------------------------------------------------------
    Grammar              Steps  Time  
  1 compare_0.json          422  424.0s
  2 prettify.json           700  830.4s
```

I ended up doing this in two parts because my comparison grammar had a bug,
so I restarted using the saved Dot file.

![part 1 output](output-part-1.svg)
