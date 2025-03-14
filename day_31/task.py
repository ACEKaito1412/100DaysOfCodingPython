import json
# with open("data.txt", mode="r", encoding="utf-8") as f:  # Ensure UTF-8 encoding
#     content = f.readlines()  
#     data = []
#     print(len(content))
    
#     for item in content:
#         index = item.find(" – ")  

#         if index != -1:
#             item = item[index:len(item)].strip()
#             text = item.replace("– ", "")
#             data.append(text)


# with open("new_data.txt", mode="w", encoding="utf-8") as f:
#     for item in data:
#         f.write(f"{item}\n")

data_dic = {}
with open('new_data.txt', "r", encoding="utf8") as f:
    content = f.readlines()
    for item in content:
        index = item.find("(")

        jap = item[index:-1].strip()
        jap = jap.replace("(", "")
        jap = jap.replace(")", "")

        translation = item[0:index].strip()

        data_dic[jap] = {"translation" : translation, "learned": 0}

with open('data.json', 'w') as f:
        json.dump(data_dic, f, indent=5)


