text = 'apple and banana one apple one banana a red apple and a green apple'
word_list = text.split()
print (word_list)
word_list_unique = set(word_list)
print (word_list_unique)
count = {}
for elem in word_list:
    if elem in count:
        count[elem] += 1
    else:
        count[elem] = 1
for word, times in count.items():
    print ('|{:<6}|{:<1}|'.format(word, times))
