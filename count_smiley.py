def count_smileys(the_list_smiley):
    smiley_count = 0
    for smiley in the_list_smiley:
        if len(smiley) == 2:
            if smiley[0] == ":" or smiley[0] == ";":
                if smiley[1] == ")" or smiley[1] == "D":
                    smiley_count += 1
        elif len(smiley) == 3:
            if smiley[0] == ":" or smiley[0] == ";":
                if smiley[2] == ")" or smiley[2] == "D":
                    smiley_count +=1
    return smiley_count

print(count_smileys([':)', ';(', ';}', ':-D']))


