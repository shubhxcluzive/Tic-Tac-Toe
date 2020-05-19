#Sometimes it might be useful to convert texts from lowerCamelCase to snake_case.
# The main trick is to find the correct place where to insert an underscore.
# Let's make a rule that it's right before a capital letter of the next word.

stringo = "tongueIo"
updated_string = ""
for char in stringo:
    if char.isupper():
        updated_string += "_" + char .lower()
    else:
        updated_string += char
print(updated_string)