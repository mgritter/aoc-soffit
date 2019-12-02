# Advent of Code 2019 Solutions in Soffit

[Soffit](https://github.com/mgritter/soffit) is a nondeterministic [graph grammar](https://en.wikipedia.org/wiki/Graph_rewriting) engine that implements
[double-pushout (DPO)](https://steemit.com/mathematics/@markgritter/double-pushouts-on-graphs) rewriting.

Basically, it's pattern matching. Take a graph, find a subgraph of its that matches some pattern, and alter the graph by adding or deleting elements.

[Advent of Code](https://adventofcode.com/) is "an Advent calendar of small programming puzzles for a variety of skill sets and skill levels that can be solved in any programming language you like."

Soffit is not a *great* choice for most Advent of Code puzzles, since it lacks features such as basic mathematics, but graph rewrite systems are
Turing-complete.

## Introduction to Soffit syntax and semantics

Soffit is an attempted homage to [Tracery](https://tracery.io/), and uses a JSON input format.
Graphs are written as strings in the [dot](https://www.graphviz.org/doc/info/lang.html) language.
Graph rewrite rules are JSON name-value pairs consisting of strings on each side. Nodes and edges in the graph may have a textual tag attached.

For example, the rewrite rule
```
    "L[line]; X[6]; L->X[next_char]" : 
    "L[started_line]; X[6]; L->X[next_char]; C[div_position]; C->X",
```
says to find a node with tag `line`, a node with tag `6`, and an edge between them with tag `next_char`.  The result of appying this rule is to
change the tag to `started_line`, introduce a new node with tag `div_position`, and create an edge from the new node to the node with tag `6`.  Any
node or edge mentioned in the "before" part of the rule but not in the "after" part of the rule is deleted.

A nonstandard addition to the Dot syntax is a mechanism to specify merging of nodes. With double-pushout semantics, merges are important because they
allow preservation of edges not specified in the rewrite rule.  DPO rewrite rules do not match in cases where their action would leave an edge "dangling",
if one end is deleted but the entire edge is not specified for deletion.

For example, the rewrite rule
```
    "A[foo]; B[bar]; A--B" :
    "A[foo]"    
```
will delete node `B` only if it has no other edges than the one to `A`.  To preserve `B`'s edges and make the rule more broadly applicable, we can
specify `A^B` (A merge B) in the production of a rule.  
```
    "A[foo]; B[bar]; A--B" :
    "A^B[foo]"    
```
The two nodes will be merged into one, and any edge adjacent to either will be preserved, with one exception.  Because Soffit implements simple graphs,
not multigraphs, a rewrite rule that would silently merge two edges (say, in the graph `A--B--C--A`) will not match.

By convention, Soffit node names are `CAPITALIZED` and tag names are `lowercase`, but Soffit permits a wide range of characters to be used
in either label type, including emoji. A disadvantage of using Python's JSON parser is that it does not permit comments, so another convention
is to use unique tags as comments; they will be interpreted as production rules that never match.

Soffit's nondeterminism operates as follows:
* For each iteration, the production rules are shuffled so that they are attempted in random order.
* If the rule has multiple right-hand sides, then they are attempted in random order as well.
* The first production rule with a match is applied. The match is chosen uniformly form all matches present in the graph, for that production.

This means it is computationally expensive to build determinstic grammars where only one rule can fire at a time; Soffit is currently not
smart enough to tell if this is the case.  Purely deterministic grammars will thus have to check about half the productions to find one that works.
Productions which have a large number of possible matches (particularly due to combinatorial explosions) are also inefficient; the number of matches
and the time spent enumerating matches are capped to mitigate this.

## Running the Advent of Code solutions

This repository augments Soffit with text input and output facilities, and a simple job scheduler (represented, naturally, as a graph.) 

After checking out the code, the easiest way to get Soffit and its dependencies is

```
pipenv install
```

Though you will probably need to install [GraphViz](https://www.graphviz.org/) separately.

Then you can run examples as:

```
pipenv shell
python -m aoc.main <path/to/part1.json> <path/to/input.txt>
```

Soffit's debug output lists the match identified for each rule, and statistics about the graph.  Unfortunately, one of the many downsides of
the initial JSON format I chose is that it makes it difficult to give rules proper names, and so report on which rule was chosen.  One way to mitigate
this is to give descriptive names to the nodes in the production, since the match will identify them.

The final graph will be rendered to `aoc.svg` in the working directory; intermediate results may also be rendered.
