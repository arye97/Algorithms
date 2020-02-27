def key_positions(A, key):
    keys = list(map(key, A))
    array = []
    for i in A:
        array.append(i)
    k = max(keys) + 1
    count = [0 for _ in range(k)]
    for a in array:
        count[key(a)] = count[key(a)] + 1
    sumOf = 0
    #print(count)
    for i in range(k):
        count[i], sumOf = sumOf, count[i] + sumOf
    return count



def sorted_array(seq, key, positions):
    sorted_array = [0 for _ in range(len(seq))] 
    for item in seq:
        sorted_array[positions[key(item)]] = item
        positions[key(item)] += 1
    return sorted_array
        
    
def counting_sort(iterable, key):
    positions = key_positions(iterable, key)
    return sorted_array(iterable, key, positions)
    
    
    
def get_digit(n, d):
    for i in range(d-1):
        n //= 10
    return n % 10

def get_num_digits(n):
    i = 0
    while n > 0:
        n //= 10
        i += 1
    return i

def radix_sort(array, d):
    for i in range(0, d):
        array = counting_sort(array, lambda x : get_digit(x, i+1))
    return array


        
print(radix_sort([329, 457, 657, 839, 436, 720, 355], 3))