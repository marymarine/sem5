"""Task 1: A string is a repetition of a substring"""
input_str = input()
i = 0
substr = ''
while True:
    substr += input_str[i]
    i += 1
    k = len(input_str)//i
    if substr*k == input_str:
        break
print(k)
