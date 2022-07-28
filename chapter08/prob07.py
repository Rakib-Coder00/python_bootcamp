this = "    Rakib is a Bad   "
print(this)
print(this.strip())


def remove_and_split(str, word):
    newStr = str.replace(word, "")
    return newStr.strip()

n = remove_and_split(this, 'Rakib')   
print(n)