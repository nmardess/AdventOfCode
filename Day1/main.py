# File opening and reading file as one string
with open("input.txt", "r") as file:
    lines = file.read()

# Split the giant line as one list
# Separator is blank line
split = lines.split("\n\n")

# Split the list into many list, separator
# is carriage return
clean = [s.split("\n") for s in split]

# Sum each list independently
calcul = [sum(map(int, c)) for c in clean]

# Reverse the list
calcul.sort(reverse=True)

print(f"Max calorie : {calcul[:1][0]}")
print(f"Somme top 3 calories : {sum(calcul[:3])}")
