letter = '''Dear <|Name|>,
Thank you for your letter.
Date: <|Date|>
'''

name= input("Enter Your Name: \n")
date= input("Enter Your Date: \n")

letter = letter.replace("<|Name|>", name)
letter = letter.replace("<|Date|>", date)
print(letter)
