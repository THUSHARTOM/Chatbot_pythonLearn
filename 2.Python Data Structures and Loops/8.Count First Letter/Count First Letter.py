# Write your count_first_letter function here:
def count_first_letter(names):
    new_dict = {}

    for key, values in names.items():
        if (key[0]) in new_dict.keys():
            new_dict[key[0]] = new_dict[key[0]] + len(names[key])
        else:
            new_dict[key[0]] = len(names[key])

    return new_dict


# Uncomment these function calls to test your  function:
print(
    count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow": ["Jon"], "Lannister": ["Jaime", "Cersei", "Tywin"]}))
# should print {"S": 4, "L": 3}
print(
    count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow": ["Jon"], "Sannister": ["Jaime", "Cersei", "Tywin"]}))
# should print {"S": 7}