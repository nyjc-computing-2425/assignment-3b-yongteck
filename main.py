stdform = input('Enter a number in scientific notation: ')
stdform = stdform.strip()
# Type your code below
stdpos = stdform.find("x")
caretpos = stdform.find("^")
mantissa = stdform[0:stdpos]
expo = stdform[caretpos+1:]

print(f"This number in E notation is {mantissa}E{expo}.")