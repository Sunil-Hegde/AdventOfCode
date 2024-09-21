def calculate_difference(input_file):
    total_code_count = 0
    total_memory_count = 0

    with open(input_file, 'r') as file:
        for line in file:
            code_count = len(line.strip())
            line = line[1:-2]  # Remove surrounding double quotes
            memory_count = 0

            i = 0
            while i < len(line):
                if line[i] == '\\':
                    i += 1
                    if line[i] in ['\\', '\"']:
                        memory_count += 1
                    elif line[i] == 'x':
                        memory_count += 1
                        i += 2
                else:
                    memory_count += 1
                i += 1

            total_code_count += code_count
            total_memory_count += memory_count

    difference = total_code_count - total_memory_count

    print("Total Code Count:", total_code_count)
    print("Total Memory Count:", total_memory_count)
    print("Difference:", difference)


def encode_strings(input_file):
    total_code_count = 0
    total_encoded_count = 0

    with open(input_file, 'r') as file:
        for line in file:
            code_count = len(line.strip())
            encoded_string = "\"" + "".join(["\\" + c if c in ['\\', '\"'] else c for c in line.strip()]) + "\""
            encoded_count = len(encoded_string)

            total_code_count += code_count
            total_encoded_count += encoded_count

    difference = total_encoded_count - total_code_count

    print("Total Code Count:", total_code_count)
    print("Total Encoded Count:", total_encoded_count)
    print("Difference:", difference)


# Example usage:
input_file = "instructions.txt"
print("Part One:")
calculate_difference(input_file)

print("\nPart Two:")
encode_strings(input_file)


    
