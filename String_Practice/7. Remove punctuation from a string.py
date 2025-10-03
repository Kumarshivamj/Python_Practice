import string

input_str = "Hello, world! How's everything going?"

punctuation = ".,!?;:'\"()-[]{}"
result = ""

# for ch in input_str:
#     if ch not in punctuation:
#         result = result + ch
#
# print("Original:", input_str)
# print("Without punctuation:", result)


for ch in input_str:
    is_punctuation = False
    for p in punctuation:
        if ch == p:
            is_punctuation = True
            break
    if not is_punctuation:
        result = result + ch
print("Original:", input_str)
print("Without punctuation:",result)
