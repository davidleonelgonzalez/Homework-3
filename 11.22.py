# David Gonzalez
# 1630338

word_l = list(input().split(' '))
word_f = []

for word in word_l:
    word_f.append(word_l.count(word))
for num in range(len(word_l)):
    print(word_l[num], word_f[num])
