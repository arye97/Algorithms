def longest_common_substring(s1, s2):
    """ uses the table of longest substring values to create longest
        substring"""
    
    length_table = [[-1]*(len(s2) + 1) for _ in range(len(s1) + 1)]
    
    x = len(s1) 
    y = len(s2)    
    
    # for each row and each column
    for i in range(x + 1):
        for j in range(y + 1):
            # taken from class notes, bottom up approach
            if (i == 0 or j == 0):
                length_table[i][j] = 0
            elif s1[i-1] == s2[j-1]:
                # if they match
                length_table[i][j] = length_table[i-1][j-1] + 1
            else:
                # if they dont match
                length_table[i][j] = max(length_table[i][j-1], length_table[i - 1][j])    
    
    # start at the very last table entry and move up
    current_index = length_table[x][y] 
  
    # substrings stores the list of output characters
    substrings = [""] * (current_index + 1)  
  
    # as long as the lengths of both strings are larger than 0
    while x > 0 and y > 0:       
        if s1[x - 1] == s2[y - 1]: 
            substrings[current_index - 1] = s1[x - 1] 
            # move up a row
            x -= 1
            # move back a column
            y -= 1
            # current_index moves backwards through the list
            current_index -= 1
        elif length_table[x - 1][y] > length_table[x][y-1]: 
            # up a row
            x -= 1
        else: 
            # move back a column
            y -= 1    

    # make the list a string
    return "".join(substrings)

s1 = "thro"
s2 = "throw"
print(longest_common_substring(s1, s2))