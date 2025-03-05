# squirel data
# count the number of squirel by color

import pandas

data = pandas.read_csv('squirel_data.csv')

colors = data['Primary Fur Color'].unique()
print(colors)

total_data = []
for col in colors[1::]:
    n = data[data['Primary Fur Color'] == col]
    total = n['Primary Fur Color'].count()
    total_data.append(total)

save_data = {
    "color" : colors[1::],
    "total" : total_data
}

n_data = pandas.DataFrame(save_data)
n_data.to_csv('squirel_color.csv') 


