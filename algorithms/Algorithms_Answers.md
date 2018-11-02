Add your answers to the Algorithms exercises here.

Exercise I. 

```
a)  a = 0
    while (a < n * n * n) 
      a = a + n * n
```
-big O: O(n)
-The number of loops carried out by the snippet above is n-1. 


```
b)  sum = 0
    for (i = 0; i < n; i++)
      for (j = i + 1; j < n; j++)
        for (k = j + 1; k < n; k++)
          for (l = k + 1; l < 10 + k; l++)
            sum++
```

-big O: O(n^4)
-The number of steps to carry out the above is O(n*(n-1)*(n-2)*(n-3))) which is O(n^4). 
-I used the following code in python tutor to make sure the big O time for the code was close to the initial big O given above. 

sum = 0
n = 7
        
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            for l in range (k+1, 10+k):
                sum = sum +1


```
c)  bunnyEars = function(bunnies) {
      if (bunnies == 0) return 0
      return 2 + bunnyEars(bunnies-1)
    }
```
-big O: O(n)
- If bunnies = 5, the recursive steps used to carry out the above can be visualized as follows:
    return 2 + bunnyEars(4)
                   |
                   v
                return 2 + bunnyEars(3)
                                |
                                v
                            return 2 + bunnyEars(2)
                                            |
                                            v 
                                        return 2 + bunnyEars(1)
                                                        |
                                                        v 
                                                    return 2 + 0

showing that when bunnies = 5, the function is called recursively 4 times, or n-1 times. This
pattern holds true for larger n, implying the that big O of this code snipper is O(n).


Exercise II:

<!-- **Exercise II**:
Suppose that you have an _n_-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor _f_ or higher, and doesn't get broken if dropped off a floor less than floor _f_. Devise a strategy to determine the value of _f_ such that the number of dropped eggs is minimized. -->


-strategy: binary search

-Drop egg from floor n/2. If egg breaks, drop egg from floor n/4 (halfway point between n/2 and n/4). If egg doesn't break, drop egg from floor 3n/4 (halfway point between n and n/2). Continue in this pattern until floor at which egg doesn't break is found. 


-big O: O(log(n))