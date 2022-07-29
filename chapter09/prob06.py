with open('log.txt') as f:
    content = f.read()

if 'python' in content.lower():
    print('python found')
else:
    print('python not found')    