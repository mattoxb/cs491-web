+++
title = "Inclusion/Exclusion"
date = 2023-03-08
draft = false
weight = 2
+++

The principle of inclusion/exclusion is a counting technique used to calculate the size of a union of sets. It states that:

\\(|A \cup B \cup C| = |A| + |B| + |C| - |A \cap B| - |B \cap C| - |A \cap C| + |A \cap B \cap C|\\)

where \\(A\\), \\(B\\), and \\(C\\) are any finite sets.

In other words, to find the size of the union of three sets \\(A\\), \\(B\\), and \\(C\\), you first add the sizes of each set
individually, then subtract the sizes of the overlaps \\((A \cap B, B \cap C\\), and \\(A \cap C\\)), and finally add the size of the
triple overlap \\((A \cap B \cap C)\\).

This principle can be extended to any number of sets, and is a useful tool in combinatorics, probability theory, and
other areas of mathematics.


## Materials {#materials}

-   [Inclusion-Exclusion Slides](/slides/inclusion-exclusion.pdf)
