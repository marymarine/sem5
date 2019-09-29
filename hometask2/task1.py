"""Task 1: A string is a repetition of a substring"""
inputStr = input()
i = 0
subStr = ''
while True:
    subStr += inputStr[i]
    i += 1
    k = len(inputStr)//i
    if subStr*k == inputStr:
        break
print(k)
