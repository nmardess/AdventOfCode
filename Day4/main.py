# File opening and reading file as one string
with open("input.txt", "r") as file:
    lines = file.read()


def lists_containing(list_a: list, list_b: list) -> int:
    fea = int(list_a[0])
    lea = int(list_a[1])
    feb = int(list_b[0])
    leb = int(list_b[1])
    if (fea >= feb and lea <= leb) or (feb >= fea and leb <= lea):
        return 1
    return 0


def list_overlap(list_a: list, list_b: list) -> int:
    fea = int(list_a[0])
    lea = int(list_a[1])
    feb = int(list_b[0])
    leb = int(list_b[1])

    list_1 = list(range(fea, lea+1))
    list_2 = list(range(feb, leb+1))

    for i in list_1:
        if i in list_2:
            return 1
    return 0


split = lines.split()

clean = [s.split(',') for s in split]

final_list_1 = []
final_list_2 = []
for c in clean:
    a = c[0].split('-')
    b = c[1].split('-')
    final_list_1.append(lists_containing(a, b))
    final_list_2.append(list_overlap(a, b))

print(sum(final_list_1))
print(sum(final_list_2))
