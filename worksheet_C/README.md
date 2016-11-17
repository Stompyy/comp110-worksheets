worksheet_C

(a) It returns true if two objects in a list are the same, false if not.

(b) Because of the nested for loop. Best visualised as an n * n table where the possible permutations are n^2, adding another object to the list will cause it to have to loop through all values another cyle to include it, and an extra full loop additionally.

(c) Every object from 0 to n-1 is still being compared at some point.

(d) As the order of comparison is not a factor, the first algorithm was comparing each object twice. This new algorithm will not compare two objects that have already been compared beforehand.

(e) By truncating the already compared permutations, the worst case running time follows a 'triangular number' trend of 1, 3, 6, 10, ... The formula for which is n(n+1)/2. Whilst significantly less than the answer for n^2, the dominant term when expanded is still n^2, so yes. O(n^2).

(f) O(n log n)
From reading the python source code https://hg.python.org/cpython/file/c6880edaf6f3/Objects/listobject.c, Tim's official python readme text document http://svn.python.org/view/python/trunk/Objects/listsort.txt?revision=69846&view=markup, before googling the answer before my head exploded, at https://wiki.python.org/moin/TimeComplexity.

(g) SORT(list) is O(n log n). HasDuplicate(list) is linear O(n). Therefore the order of the combined algorithm is O(n) + O(n log n) == O(n log n + n), where the dominant term is O(n log n).

(h) As n increases, the dominant terms of n log n will tend to lower values than the dominant term of n^2. Therefore the first algorithm O(n log n) will run faster if the size of the input list is large.

(i) For readability and maintainability.
