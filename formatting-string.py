nums = [4, 5, 6]
msg = "Numbers: {0} {1} {2}". format(nums[0], nums[1], nums[2])
print(msg)

print("{0}{1}{0}".format("abra", "cad"))

a = "{x}, {y}".format(x=5, y=12)
print(a)


str="{c}, {b}, {a}".format(a=5, b=9, c=7)
print(str)


x = ", ".join(["spam", "eggs", "ham"])
print(x)
print(type(x))

#Fill in the blanks to output the second word of the given string 'x'
words = x.split(' ')
res = words[1]
print(res)


#Fill in the blanks to replace all '!' characters in str with a dot '.'
x = str.replace('!', '.')

#Your friend sent you a message, however his keyboard is broken and types a # instead of a space.
#Replace all of the # characters in the given input with spaces and output the result.
msg = input()
msg = msg.replace('#',' ')
print(msg)


txt = "hello"
print(max(txt))