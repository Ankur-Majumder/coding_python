def powerset(s, current=[]):
    if not s:
        print(current)
        return
    
    powerset(s[1:], current + [s[0]])

    powerset(s[1:], current)

arr = [1, 2, 3]

powerset(arr)
