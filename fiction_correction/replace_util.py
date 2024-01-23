def read_lines(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = [line.strip() for line in file]
    return lines



if __name__ == '__main__':
    need_to_replace_sentence_list = read_lines("./fix_log/娇妻美妾任君尝_第一部.txt")

    for need_to_replace_sentence in need_to_replace_sentence_list:
        print(need_to_replace_sentence)
