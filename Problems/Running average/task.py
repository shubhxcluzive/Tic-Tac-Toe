my_string = input()

result = [((int(my_string[i]) + int(my_string[i + 1])) / 2) for i in range(len(my_string) - 1)]

print(result)