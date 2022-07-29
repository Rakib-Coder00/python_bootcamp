content = True
i = 1
with open("log.txt") as f:
    while content:
        content.readline()
        if 'python' in content.lower():
            print(content)
            print(f'Yes python is found in line {i}')
        i+=1