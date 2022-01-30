wardrobe = {"shirt": ["red", "blue", "white"], "jeans": ["blue", "black"]}
for i in wardrobe:
    for j in wardrobe[i]:
        print("{} {}".format(j, i))
