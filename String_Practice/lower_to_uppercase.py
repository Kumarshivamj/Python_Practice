# text = "i love python"
# upper_text = text.upper()
# print(upper_text)


text = "i love python"
result = ""
for i in text:
    if 'a' <= i <= 'z':
        result += chr(ord(i)- 32)
    else:
        result += i
print(result)