import re

class Wire:
    def __init__(self, instruction):
        self.calculate = self.generate_value_getter(instruction)
        self.value = None

    def get_value(self):
        if self.value is None:
            self.value = self.check_range(self.calculate())
        return self.value

    def check_range(self, i):
        n = 65536
        return ((i % n) + n) % n

    def generate_value_getter(self, instruction):
        assign_match = re.match(r'^(NOT )?([0-9]+|[a-z]+)$', instruction)
        op_match = None

        if assign_match:
            return lambda: ~parse_value(assign_match.group(2)) if assign_match.group(1) else parse_value(assign_match.group(2))
        elif (op_match := re.match(r'^([a-z]+|[0-9]+) (AND|OR|LSHIFT|RSHIFT) ([a-z]+|[0-9]+)$', instruction)):
            op_code = self.ops[op_match.group(2)]
            return lambda: eval(f"{parse_value(op_match.group(1))} {op_code} {parse_value(op_match.group(3))}")

    ops = {
        'AND': '&',
        'OR': '|',
        'LSHIFT': '<<',
        'RSHIFT': '>>',
    }


def parse_value(key):
    try:
        i = int(key)
        return i
    except ValueError:
        return wires[key].get_value() if key in wires else 0 


wires = {}

with open('input.txt') as f:
    for item in f:
        if match := re.match(r'(.*) -> ([a-z]+)', item):
            wires[match.group(2)] = Wire(match.group(1))

part_one = wires['a'].get_value()
print('Part One:', part_one)

for key in wires:
    wires[key].value = None
wires['b'].value = part_one

print('Part Two:', wires['a'].get_value())
