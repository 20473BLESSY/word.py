word = "mississippi"
count = {"m":0 ,"i":0 ,"s":0 ,"p":0}
for i in word:

    if i == "m":
        count["m"] = count["m"] +1
    elif i == "i":
            count["i"] = count["i"] +1
    elif i == "s":
            count["s"] = count["s"] +1
    elif i == "p":
            count["p"] = count["p"] +1
print(count)
