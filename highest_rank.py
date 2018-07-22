"""
Write a method highestRank(arr) (or highest-rank in clojure) which returns the 
number which is most frequent in the given input array (or ISeq). 
If there is a tie for most frequent number, return the largest number of which 
is most frequent.

Example:

arr = [12, 10, 8, 12, 7, 6, 4, 10, 12];
highestRank(arr) //=> returns 12

arr = [12, 10, 8, 12, 7, 6, 4, 10, 12, 10];
highestRank(arr) //=> returns 12

arr = [12, 10, 8, 8, 3, 3, 3, 3, 2, 4, 10, 12, 10];
highestRank(arr) //=> returns 3
"""
import operator
def highest_rank(num_list):
    # your code here
    if len(num_list) > 0:
        seen = {}
        dupes = []

        for x in num_list:
            if x not in seen:
                seen[x] = 1
            else:
                if seen[x] == 1:
                    dupes.append(x)
                seen[x] += 1
        #print(seen)
        #print(dupes)

        return max(seen.items(), key=operator.itemgetter(1))[0]
    else:
        return 0

highest_rank([])