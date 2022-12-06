import string

# File opening and reading file as one string
with open("input.txt", "r") as file:
    lines = file.read()


############
# Partie 1 #
############


def return_same_char(str1: str, str2: str) -> int:
    for s in str1:
        if s in str2:
            return string.ascii_letters.index(s)+1


split = lines.split()

clean = [[s[:len(s)//2], s[len(s)//2:]] for s in split]

new_list = [return_same_char(c[0], c[1]) for c in clean]

print(f"partie 1: {sum(new_list)}")

############
# Partie 2 #
############

split_by_three = [split[i:i+3] for i in range(0, len(split), 3)]


def return_same_char_part_two(str1: str, str2: str, str3: str) -> int:
    for s in str1:
        if s in str2 and s in str3:
            return string.ascii_letters.index(s)+1


new_list_part_two = [return_same_char_part_two(c[0], c[1], c[2]) for c in
                     split_by_three]


print(f"Partie 2 : {sum(new_list_part_two)}")
