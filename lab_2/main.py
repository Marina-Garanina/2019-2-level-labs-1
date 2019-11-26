def generate_edit_matrix(num_rows: int, num_cols: int) -> list:
    edit_matrix = []
    if not isinstance(num_rows, int) or not isinstance(num_cols, int):
        return edit_matrix
    if num_cols <= 0 or num_rows <= 0:
        return edit_matrix
    for _ in range(num_rows):
        string = []
        for _ in range(num_cols):
            string.append(0)
        edit_matrix.append(string)
    return edit_matrix


def initialize_edit_matrix(edit_matrix: tuple, add_weight: int, remove_weight: int) -> list:
    if not isinstance(edit_matrix, tuple):
        return []
    edit_matrix = list(edit_matrix)
    if not isinstance(add_weight, int) or not isinstance(remove_weight, int):
        return edit_matrix
    if edit_matrix == [[]] * len(edit_matrix):
        return edit_matrix
    for i in range(1, len(edit_matrix)):
        edit_matrix[i][0] = edit_matrix[i - 1][0] + remove_weight
    for j in range(1, len(edit_matrix[0])):
        edit_matrix[0][j] = edit_matrix[0][j - 1] + add_weight
    return edit_matrix


def minimum_value(numbers: tuple) -> int:
    if isinstance(numbers, tuple):
        res = min(list(numbers))
        return res


def fill_edit_matrix(edit_matrix: tuple,
                     add_weight: int,
                     remove_weight: int,
                     substitute_weight: int,
                     original_word: str,
                     target_word: str) -> list:
    if not isinstance(edit_matrix, tuple):
        return []
    edit_matrix = list(edit_matrix)
    if not isinstance(original_word, str) or not isinstance(target_word, str) or original_word == '' \
            or target_word == '':
        return edit_matrix
    if not isinstance(add_weight, int) or not isinstance(remove_weight, int) or not isinstance(substitute_weight, int):
        return edit_matrix
    original_word = ' ' + original_word
    target_word = ' ' + target_word
    for i in range(1, len(edit_matrix)):
        for j in range(1, len(edit_matrix[0])):
            ad = edit_matrix[i][j - 1] + add_weight
            re = edit_matrix[i - 1][j] + remove_weight
            su = edit_matrix[i - 1][j - 1]
            if original_word[i] != target_word[j]:
                su += substitute_weight
            edit_matrix[i][j] = minimum_value((ad, re, su))
    return edit_matrix




def find_distance(original_word: str,
                  target_word: str,
                  add_weight: int,
                  remove_weight: int,
                  substitute_weight: int) -> int:
    wrong_result = -1
    if type(original_word) == str and type(target_word) == str and type(add_weight) == int and type(remove_weight) == int and type(substitute_weight) == int:
        num_rows = len(original_word) + 1
        num_cols = len(target_word) + 1
        new_matrix = generate_edit_matrix(num_rows, num_cols)
        matrix = initialize_edit_matrix(tuple(new_matrix), add_weight, remove_weight)
        return fill_edit_matrix(tuple(matrix), add_weight, remove_weight, substitute_weight, original_word, target_word)[num_rows - 1][num_cols - 1]
    else:
        return wrong_result


def save_to_csv(edit_matrix: tuple, path_to_file: str) -> None:
    save_file = open(path_to_file,'w')
    for string in edit_matrix:
        row = ''
        for el in string:
            row = str(el)+','
            save_file.write(row)
        save_file.write('\n')
    save_file.close(row)

def load_from_csv(path_to_file: str) -> list:
    new_file = open(path_to_file)
    matrix = []
    for string in new_file:
        line_with_z = string.split(',')
        line =[]
        for el in line_with_z:
            line.append(int(el))
        matrix.append(line)
    return matrix
