def bigger_is_greater(w):
    # Step1: Find the pivot character
    n = len(w)
    pivot = -1
    for i in range(n-2, -1, -1):
        if w[i] < w[i+1]:
            pivot = i
            break
    
    if pivot == -1:
        return "no answer"
    
    # Step 2: Find the swap character
    swap = n-1
    for i in range(n-1, pivot, -1):
        if w[i] > w[pivot]:
            swap = i
            break
    
    # Step 3: Swap the pivot and swap characters
    w_list = list(w)
    w_list[pivot], w_list[swap] = w_list[swap], w_list[pivot]
    
    # Step 4: Reverse the substring to the right of the pivot character
    w_list[pivot+1:] = reversed(w_list[pivot+1:])
    
    # Step 5: Return the modified string
    return "".join(w_list)
    
# Sample test cases
print(bigger_is_greater("ab"))    # ba
print(bigger_is_greater("bb"))    # no answer
print(bigger_is_greater("hefg"))  # hegf
print(bigger_is_greater("dhck"))  # dhkc
print(bigger_is_greater("dkhc"))  # hcdk
