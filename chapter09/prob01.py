f = open('poems.txt')
t = f.read()
if 'twinkle' in t:
    print('twinkle is in the poem')
else:
    print('twinkle is not in the poem')
f.close()