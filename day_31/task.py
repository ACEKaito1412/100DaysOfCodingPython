
with open("data.txt", mode="r", encoding="utf-8") as f:  # Ensure UTF-8 encoding
    content = f.readlines()  
    data = []
    print(len(content))
    
    for item in content:
        index = item.find(" – ")  

        if index != -1:
            item = item[index:len(item)].strip()
            text = item.replace("– ", "")
            data.append(text)


with open("new_data.txt", mode="w", encoding="utf-8") as f:
    for item in data:
        f.write(f"{item}\n")


