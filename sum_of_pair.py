def sum_pairs(int_list, the_sum):
    res_list = []
    for num_1 in int_list:
        #for num_2 in int_list[1:]:
        for num_2 in int_list:
            if (num_1+num_2) == the_sum:
                if num_1 != num_2:
                    res_list.extend((num_1,num_2))
            #break
    # if len(res_list) == 0:
    #     return
    # else:
    return res_list



print(sum_pairs([1, 2, 3, 4, 1, 0], 2))
