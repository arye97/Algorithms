def getEmptyStringList(s1, s2, output_table, x, y):
    """if one of the strings is empty, then use this to continue to insert or delete strings"""
    if x == 0:
        # then insert s2 into s1
        char = 'I'
        for index in range(y):
            output_table.append((char, '', s2[index]))
        return output_table
    elif y == 0:
        # then delete all of 
        char = 'D'
        for index in range(x):
            output_table.append((char, s1[index], ''))    
        return output_table    

def getOutputList(s1, s2, dist_table):
    """gets the list of operations needed from the dp table"""
    x = len(s1)
    y = len(s2)
    output = [] 

    while (x > 0 and y > 0):
        minimum = min(dist_table[x][y-1],
                      dist_table[x-1][y],
                      dist_table[x-1][y-1])

        # PRIORITY
        # 1. Deletion
        # 2. Insertion
        # 3. Substitution

        if (s1[x-1] == s2[y-1]):
            step = ('T', s1[x - 1], s2[y - 1])
            output.append(step)
            x -= 1
            y -= 1   
        else:
            if dist_table[x-1][y] == minimum:
                # deletion
                step = ('D', s1[x - 1], '')
                x -= 1
                output.append(step)
            elif dist_table[x][y-1] == minimum:
                # insertion
                step = ('I', '', s2[y - 1])
                y -= 1
                output.append(step)
            elif dist_table[x-1][y-1] == minimum:
                # substitution
                step = ('S', s1[x - 1], s2[y - 1])
                output.append(step)
                x -= 1
                y -= 1   
        
    if (x == 0 or y == 0):
        output = getEmptyStringList(s1, s2, output, x, y)    
        
    return reversed(output)
    
    
def line_edits(s1, s2):
    """ returns the list of operations needed to turn s2 into s1"""
    
    s1 = s1.splitlines()
    s2 = s2.splitlines()
    
    x = len(s1) 
    y = len(s2)   
    output = []
    dist_table = [[-1]*(y + 1) for _ in range(x + 1)]
    
    
    # for each row and each column
    for i in range(x + 1):
        for j in range(y + 1):
            if (i == 0 and j == 0):
                dist_table[i][j] = 0
            elif j == 0:
                dist_table[i][j] = i
            elif i == 0:
                dist_table[i][j] = j
            elif s1[i - 1] == s2[j - 1]:
                dist_table[i][j] = dist_table[i - 1][j - 1]
            else:
                minimum = min(dist_table[i-1][j],
                              dist_table[i][j-1],
                              dist_table[i-1][j-1])
                dist_table[i][j] = 1 + minimum
       
    output = getOutputList(s1, s2, dist_table)
    return output


s1 = "Line1\nLine2\nLine3\nLine4\n"
s2 = "Line1\nLine3\nLine4\nLine5\n"
table = line_edits(s1, s2)
for row in table:
    print(row)