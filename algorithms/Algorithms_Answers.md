Add your answers to the Algorithms exercises here.

I. 

```
a)  a = 0
    while (a < n * n * n) 
      a = a + n * n
```
-The number of loops carried out by the snippet above is n-1. 
-O(n) runtime


```
b)  sum = 0
    for (i = 0; i < n; i++)
      for (j = i + 1; j < n; j++)
        for (k = j + 1; k < n; k++)
          for (l = k + 1; l < 10 + k; l++)
            sum++
```

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