def do_search(array, target_value):
    min_index = 0
    max_index = len(array) - 1
    
    while min_index <= max_index:
        guess_index = (min_index + max_index) // 2
        guess_value = array[guess_index]
        
        if guess_value == target_value:
            return guess_index
        elif guess_value < target_value:
            min_index = guess_index + 1
        else:
            max_index = guess_index - 1
    return -1

primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]

result = do_search(primes, 73) 

print("Found prime at index ", result)  
            
