# File opening and reading file as one string
with open("input.txt", "r") as file:
    lines = file.read()


combinaisons_part_1 = {
    "A X": 4, "A Y": 8, "A Z": 3,
    "B X": 1, "B Y": 5, "B Z": 9,
    "C X": 7, "C Y": 2, "C Z": 6
}

split = lines.split("\n")

clean = [combinaisons_part_1.get(s, 0) for s in split]

print(f"partie 1 : {sum(clean)}")


combinaisons_part_2 = {
    "A X": 3, "A Y": 4, "A Z": 8,
    "B X": 1, "B Y": 5, "B Z": 9,
    "C X": 2, "C Y": 6, "C Z": 7
}

split = lines.split("\n")

clean = [combinaisons_part_2.get(s, 0) for s in split]

print(f"partie 2 : {sum(clean)}")
