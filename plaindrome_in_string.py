
def palindrom_in_string(word):
    output = ''
    size = len(word)
    for i in range(size):
        text = word[::-1][:-i]
        for j in range(len(text)):
            if word[i] == text[j] and i != size-j-1:
                temp = word[i:-j+size]
                if temp == temp[::-1]:
                    # if contains only one palindrome in sequence
                    return temp
                    # To get all possible palindrome words
                    #  output += '%s ' % temp
    return output
input = 'xyzlolvbxcv'
print('List of palindrom words in the string: %s' % input)
result=palindrom_in_string(input)
print(result)
