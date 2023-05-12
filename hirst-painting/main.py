import colorgram

rgb_colors = []

colors = colorgram.extract("image.jpg", 30)
for color in colors:
    rgb_colors.append(color.rgb)

colors_list = []

for index, item in enumerate(rgb_colors):
    r = rgb_colors[index][0]
    g = rgb_colors[index][1]
    b = rgb_colors[index][2]
    colors_list.append((r, g, b))

print(colors_list)
