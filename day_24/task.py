
with open('my_file.txt', mode='r') as f:
    content = f.read()
    print(content)

# append mode = a
# write mode = w
# read mode = r

with open('my_file.txt', mode='w') as f:
    f.write("new text")