'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
count = 0
def count_th(word):
    if "th" in word:
        return count_th(word.replace("th", "0", 1)) + 1
    else:
        return 0
    
    global count
    if len(word) == 1:
        return count
    if word[0] == 't' and word[1] == 'h':
        count += 1
        if word[2]:
            count_th(word[2:])
        return count    
    count_th(word[1:])
    
print(count_th("abcthxyz"))