Part 1:

```
--------------------------------------------------------------------------------
    Grammar              Steps  Time  
  1 tokenify.json          7398 2997.7s
  2 input_to_graph_tree.json  30102 316353.5s
  3 count_paths.json     170070 83038.2s
--------------------------------------------------------------------------------
+100000+10000+10000+10000+1000+1000+1000+1000+1000+1000+1000+1000+1000+100+100+100+100+100+10+10+10+10+10+10+10+10+10+1+1+1+1+1+1+1(end)
```

After a lot of false starts, the approach I took here is to insert all the strings
into a tree, and then merge tree nodes that had the same label, then all bodies
attached to the same tree node.  This was SUPER SLOW.

![complete tree, after step 2](complete-tree.svg)
