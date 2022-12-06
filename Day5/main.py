from copy import deepcopy


stack = [
    ['R', 'S', 'L', 'F', 'Q'],
    ['N', 'Z', 'Q', 'G', 'P', 'T'],
    ['S', 'M', 'Q', 'B'],
    ['T', 'G', 'Z', 'J', 'H', 'C', 'B', 'Q'],
    ['P', 'H', 'M', 'B', 'N', 'F', 'S'],
    ['P', 'C', 'Q', 'N', 'S', 'L', 'V', 'G'],
    ['W', 'C', 'F'],
    ['Q', 'H', 'G', 'Z', 'W', 'V', 'P', 'M'],
    ['G', 'Z', 'D', 'L', 'C', 'N', 'R']
]

stack_part_one = deepcopy(stack)
stack_part_two = deepcopy(stack)


with open('input.txt', 'r') as file:
    lines = file.read()

split = lines.split('\n')

clean = [s.split() for s in split]

list_dict = [{c[0]:int(c[1]), c[2]:int(c[3]), c[4]:int(c[5])}
             for c in clean if len(c) == 6]


for ld in list_dict:
    for move in range(ld['move']):
        _to = ld['to'] - 1
        _from = ld['from'] - 1
        _move = ld['move']

        stack_part_one[_to].append(stack_part_one[_from].pop())

        index = (_move - move) * (-1)
        stack_part_two[_to].append(stack_part_two[_from].pop(index))

part_one = [(sone[len(sone)-1]) for sone in stack_part_one]
print(''.join(part_one))

part_two = [(stwo[len(stwo)-1]) for stwo in stack_part_two]
print(''.join(part_two))
