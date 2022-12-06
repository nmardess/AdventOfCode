# File opening and reading file as one string
with open("input.txt", "r") as file:
    lines = file.readline()


def are_different(substr: str, nb_char: int) -> bool:
    if len(substr) == nb_char and len(set(substr)) == nb_char:
        return True
    return False


for i in range(len(lines)):
    if test := (are_different(lines[i:i+4], 4)):
        print(f"Vrai à l'index démarrage : {i} et fin : {i+4}")
        break

for i in range(len(lines)):
    if test := (are_different(lines[i:i+14], 14)):
        print(f"Vrai à l'index démarrage : {i} et fin : {i+14}")
        break
