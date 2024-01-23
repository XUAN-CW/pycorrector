import json

from fiction_correction import config


def read_lines(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = [line.strip() for line in file]
    return lines

def replace_in_file(file_path, source, target):
    # Read the file content
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Replace source with target
    modified_content = content.replace(source, target)

    # Write the modified content back to the file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(modified_content)

# Example usage:
# replace_in_file('path/to/your/file.txt', 'AAAA', 'BBBB')


if __name__ == '__main__':
    need_to_replace_sentence_list = read_lines("./fix_log/娇妻美妾任君尝_第一部.txt")

    for need_to_replace_sentence in need_to_replace_sentence_list:
        print(need_to_replace_sentence)
        data = json.loads(need_to_replace_sentence)
        replace_in_file(config.md_file,data['source'],data['target'])
