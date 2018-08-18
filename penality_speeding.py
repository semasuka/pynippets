"""
You have been speeding on a motorway and a police car had to stop you. The policeman is a funny guy that likes to play games. Before issuing penalty charge notice he gives you a choice to change your penalty.

Your penalty charge is a combination of numbers like: speed of your car, speed limit in the area, speed of the police car chasing you, the number of police cars involved, etc. So, your task is to combine the given numbers and make the penalty charge to be as small as possible.

For example, if you are given numbers [45, 30, 50, 1] your best choice is 1304550

Examples:

['45', '30', '50', '1'] => '1304550'

['100', '10', '1'] => '100101'

['32', '3'] => '323'

"""
import itertools
def penalty(a_list):
    the_len = len(a_list)
    permuted_list = list(itertools.permutations(a_list,the_len))
    print(permuted_list)
    cont_list = []
    for elements in permuted_list:
        cont_element = "".join(map(str,elements))
        cont_list.append(int(cont_element))
    min_num = str(min(cont_list))
    return min_num

print(penalty(['31', '97', '6', '78']))