text = [["Glitch", "is", "a", "minor", "problem", "that", "causes", "a", "temporary", "setback"],
        ["Ephemeral", "lasts", "one", "day", "only"],
        ["Accolade", "is", "an", "expression", "of", "praise"]]
input_value = int(input())
output = [word for lst_word in text for word in lst_word if len(word) <= input_value]
print(output)