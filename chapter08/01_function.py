marks = [45, 78, 86, 77]
percentage = (sum(marks)/400)*100

marks2 = [45, 64, 46, 75]
percentage2 = (sum(marks2)/400 )*100
# print(percentage, percentage2)


# function:
def percent(marks):
    return((marks[0]+ marks[1]+marks[2]+ marks[3])/400)*100
marks = [45, 78, 86, 77]
percentage = percent(marks)
print(percentage)