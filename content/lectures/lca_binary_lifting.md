+++
title = "Least Common Ancestor and Binary Lifting"
date = 2023-04-05
draft = false
weight = 11
+++

## Materials {#materials}

-   [LCA and Binary Lifting Slides](/slides/lca-binary-lifting.pdf)

## Transcript

### Title Slide

The WIFI here is terrible and it ate my recording, so I'm just going to type out the lecture.

I didn't bother making a video of the previous algorithm because it was just regular DFS and BFS
and you already know them.  Today we will talk about a new algorithm which most of you probably
will **not** know.

### DFS for Ancestry

One thing we often want to do is, given two nodes `u` and `v`, check if one is the ancestor of the other.  In the
example tree, `A` is the ancestor of `H`, but `H` is not the ancestor of `E`.  It turns out we can modify DFS to make
this quick and easy.  The way we do that is to create a timer and keep three vectors: `tin`, `tout`, and `up`.  The DFS
function takes two parameters.  The first is `v`, the node we are considering.  The second is `p`, the parent of `v`.

`tin` is short for "timer in", and represents the value of `timer` when we enter the node.  We set this on line 3.  Note
that we increment the timer each time we use it.  After we set `tin`, we set `up` for node `v` in row 0.  `up[v][0]`
will hold the parent of `v`.  Next, we DFS the children.  When that's done, we are ready to exit `v`, so we set
`tout[v]` to be the preincremented timer value.

You may want to try filling out the values for this tree yourself.  The root is done for you; the upper value is `tin`
for that node, and the lower value is `tout`.

### DFS for Ancestory, ctd

Here is the tree with the completed `tin` and `tout` values.  Check the values and see if you can work out how we can
tell if one node is the ancestor of another.

### Is it an ancestor?

Here is the code to check if `u` is an ancestor of `v`.  The in-value of an ancestor will always be smaller than the
in-value of a descendant, and the out-value of an ancestor will always be larger than the out value of a descendant.
So, `A` has in-value of 1 and out-value of 4, and `H` as in-value of 2 and out-value of 3.  `A`'s range completely covers
`H`'s range, so `A` is an ancestor of `H`.  If you compare `H` with `G`, you see the ranges do not overlap, therefore
`H` is not an ancestor of `G`.

### Least Common Ancestor

In tree algorithms, it's sometimes necessary to take two notes and ask what their least common ancestor is.  For example,
in the previous graph, `D` and `G` have LCA of `B`.  How would you compute this?

The way that might come to you is to start with one node, say `B`, and traverse all the way to the root and put each node
you see in a set.  In this example, you'd have `G`, `B`, and `R`.  Next you start at the other node and traverse to the root
and stop when you find a node already in your set.

Assuming you use a standard red-black tree implementation of sets, this would run in ${\cal O}(n \log n)$ time.  This is
not bad, but for a very deep tree you could get TLE trying to do this.  It turns out we can check this in sub-linear
time: ${\cal O}(\log n)$.

Here is the idea: if I ask who your parent is, and then ask who their parent is, what I have is the
parent-of-the-parent, or the grand-parent: 2 generations.  If I ask the grand-parent of the grand-parent, then I get the
great-great-grand-parent: 4 generations.  Each time you repeat this you double the generations back you are looking.

To capture this in our `up` array, we first set the parents in row zero.  In row 1, we will store the parents.  In row 
2 we will store the great-grand-parents.  Calculating this is simple.  Line 8 and 9 show how to do it.  Starting with row 1,
you populate column `v` with lookup at `up[up[v][0]][0]`.  In other words, we look up the parent, and then look up /its/
parent.  For row 2 we double-lookup row 1, and so on.

This is why you see on line 1 we take the log of the number of nodes and use that to create the 2D `up` array.

### Least Common Ancestor (2nd of it's name)

If we do this for the example tree, we get this rather boring array.  This is because that tree was not particularly deep.
Note there's a typo here: row 1 should have entries other that `R` for `D`, `E`, and `F`: all should point to `B`.

On the slides is a description of another tree.  Try to make the up array for it.  The answer is on the next slide.

### Answer

Here it is.  Be sure to verify you came to the same conclusion.

### Find LCA

Now we can use this to find the LCA of `u` and `v`.  Lines 3 to 6 check to be sure that one of these is not already the
ancestor of the other one.

If we get past that, we arbitrarily pick `u` and look up the further ancestor away.  You see this as we set `i` in the
`for` loop to be maximum depth.  If the lookup of `u` is not an ancestor of `v`, we set `u` and try again.

If the lookup of `u` is an ancestor, we decrement `i` and try again.  For each level of the `for` loop we look up `u`'s
ancestor until it would make it an ancestor of `v`, and we keep doing that until we process row 0, the simple parents.
This leaves `u` being one level below the common ancestor.  We complete it by looking up `u`'s parent on line 11 and
we're done.

Anyway, that's the algorithm.  You will need it in a future problem coming soon.  I hope this lecture helps!
