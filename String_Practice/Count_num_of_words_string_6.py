text = "Hello welcome to INDIA"
count = 0
in_word = False
for i in text:
    if i != " " and not in_word:
        count = count+1
        in_word = True
    elif i == " ":
        in_word = False
print("Number of words is", count)
