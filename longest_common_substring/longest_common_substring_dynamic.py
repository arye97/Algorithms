def longest_common_substring(s1, s2):
    """ uses the table of longest substring values to create longest
        substring"""
    
    length_table = [[-1]*(len(s2) + 1) for _ in range(len(s1) + 1)]
    lowest_common_helper(s1, s2, length_table, 0, 0)
    for row in length_table:
        print(row)
    i = 0
    j = 0
    strings = []
    # reads the table and gives the string    
    def print_string(i, j):
        """ uses the table of values to print out the longest common string """
        if not (i == len(s1) or j == len(s2)):
            # if the end of either string hasnt been reached
            if s1[i] == s2[j]:
                # if the letters match increase both lengths
                strings.append(s1[i])
                i += 1
                j += 1
            elif length_table[i][j + 1] > length_table[i + 1][j]:
                # the jth + 1 is greater than jth below, move forward not down
                j += 1
            else:
                # move down the table
                i += 1
            # next letter
            print_string(i, j)
            
    print_string(i, j)
    #join the list strings to one string
    return "".join(strings)


 
def lowest_common_helper(s1, s2, length_table, i, j):
    """ creates table of longest substring values """
    if length_table[i][j] >= 0:
        # if the length has already been altered
        # then just return the value
        return length_table[i][j]
    if i == len(s1) or j == len(s2):
        # if the index values are the end of a string
        # then default to zero as has no length
        length_longest = 0
    else:
        # recurrence relation taken from lecture notes
        if s1[i] == s2[j]:
            length_longest = 1 + lowest_common_helper(s1, s2, length_table, i + 1, j + 1)
        else:
            length_longest = max(lowest_common_helper(s1, s2, length_table, i + 1, j),
                    lowest_common_helper(s1, s2, length_table, i, j + 1))
    # input the table values of longest length
    length_table[i][j] = length_longest
    return length_longest





 
s1 = "Look at me, I can fly!"
s2 = "Look at that, it's a fly"
print(longest_common_substring(s1, s2))