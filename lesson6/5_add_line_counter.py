import os


def read_from_file(filename):
    normalized_lines = []
    with open(filename) as file:
        counter = 1
        for line in file:
            line = line.strip()
            if line:
                normalized_lines.append(f'{counter}: {line}\n')
                counter += 1
    return normalized_lines


def write_to_file(filename, data):
    with open(filename, 'w') as file:
        for line in data:
            file.write(line)
    print(f'Write to {filename} complete')


current_dir = os.getcwd()
input_file = os.path.join(current_dir, 'examples', 'input.txt')
output_file = os.path.join(current_dir, 'examples', 'output.txt')

normalized_data = read_from_file(input_file)
write_to_file(output_file, normalized_data)
