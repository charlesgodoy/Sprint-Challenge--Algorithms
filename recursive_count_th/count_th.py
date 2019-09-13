'''
Your function should take in a signle parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    if word == "" or len(word) == 1:
        return 0

    elif len(word) == 2:
        if word[0] == "t" and word[1] == "h":
            return 1
        else: 
            return 0

    elif word[0] != "t" and word[1] != "h":
        return 0 + count_th(word[1:])

    elif word[0] != "t" and word[1] == "h":
        return 0 + count_th(word[1:])

    elif word[0] == "t" and word[1] != "h":
        return 0 + count_th(word[1:])

    elif word[0] == "t" and word[1] == "h":
        return 1 + count_th(word[2:])

print(count_th('aaaaa'))
print(count_th('thth'))
print(count_th('abcthefthghith'))
print(count_th(''))