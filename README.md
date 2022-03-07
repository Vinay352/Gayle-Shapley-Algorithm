# Gayle-Shapley-Algorithm

The stable matching problem, in its most basic form, takes as input equal numbers of two types of participants (n men and n women, 
or n medical students and n internships, for example), and an ordering for each participant giving their preference for whom to be 
matched to among the participants of the other type. A stable matching always exists, and the algorithmic problem solved by the 
Gale–Shapley algorithm is to find one. A matching is not stable if:  

1. There is an element A of the first matched set which prefers some given element B of the second matched set over the element to which A is already matched, and 
2. B also prefers A over the element to which B is already matched. 

In other words, a matching is stable when there is no pair (A, B) where both participants prefer each other to their matched partners.
