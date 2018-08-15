"""
At a job interview, you are challenged to write an algorithm to check if a given string, s, can be formed from two other strings, part1 and part2.

The restriction is that the characters in part1 and part2 are in the same order as in s.

The interviewer gives you the following example and tells you to figure out the rest from the given test cases.

For example:

'codewars' is a merge from 'cdw' and 'oears':

    s:  c o d e w a r s   = codewars
part1:  c   d   w         = cdw
part2:    o   e   a r s   = oears

"""

def is_merge(s, part1, part2):
    s_set = set(s)
    part1_set = set(part1)
    part2_set = set(part2)
    parts_set_union = part1_set.union(part2_set)

    if parts_set_union.issubset(s_set):
        return True
    else:
        return False



print(not is_merge('codewars', 'cod', 'wars'))