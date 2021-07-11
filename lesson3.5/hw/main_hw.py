def compare_lines(file_name1, file_name2):
    s1 = open(file_name1)
    s2 = open(file_name2)
    line1 = s1.readline()
    line2 = s2.readline()
    count_line = 1
    while True:
        if line1 == '' and line2 == '':
            break
        if str(line1) != str(line2):
            print('line number:', count_line)
            if line1:
                print('file1:', line1, end='\t--\t')
            if line2:
                print('file2:', line2)
        line1 = s1.readline()
        line2 = s2.readline()
        count_line += 1
    s1.close()
    s2.close()


def file_statistics(file_in):
    digits = set(['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'])
    vowels = set(['A', 'E', 'I', 'O', 'U', 'Y'])
    consonants = set(['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z'])
    file_out = 'task_2_statistics.txt'
    s1 = open(file_in)
    count_lines = len(s1.readlines())
    count_ch = 0
    count_digits = 0
    count_vowels = 0 # гласные
    count_consonants = 0 # согласные
    s1.seek(0)
    ch = s1.read(1)
    while ch != '':
        count_ch += 1
        if ch in digits:
            count_digits += 1
        if ch.upper() in vowels:
            count_vowels += 1
        if ch.upper() in consonants:
            count_consonants += 1
        ch = s1.read(1)
    s1.close()
    s2 = open(file_out, mode='w')
    list = []
    list.append(f'file: {file_in}\n')
    list.append(f'characters: {count_ch}\n')
    list.append(f'lines: {count_lines}\n')
    list.append(f'digits: {count_digits}\n')
    list.append(f'vowels: {count_vowels}\n')
    list.append(f'consonants: {count_consonants}')
    s2.writelines(list)
    s2.close()


def remove_last_line(
        file_name, 
        file_name_result='task_3_result.txt'
    ):
    s1 = open(file_name)
    lines = s1.readlines()
    s1.close()
    s2 = open(file_name_result, mode='w')
    s2.writelines(lines[:-1])
    s2.close()


def longest_line(file_name):
    s = open(file_name)
    lines = s.readlines()
    s.close()
    max_len_line = 0
    for line in lines:
        max_len_line = max(max_len_line, len(line)) 
    print('maximum characters in line:', max_len_line)


def number_of_words_found(file_name):
    import re

    search = input('Введите слово для поиска:')
    s = open(file_name)
    file = s.read()
    s.close()
    count_words_found = 0
    r1 = re.findall(search, file)
    print('Количество найденных слов: ', len(r1))


def find_replace(file_name):
    search = input('Введите слово для поиска:')
    replace = input('Введите слово для замены:')
    s = open(file_name)
    lines = s.readlines()
    s.close()
    new_lines = []
    for line in lines:
        new_lines.append(line.replace(search, replace))
    # print(new_lines)
    # print('Количество замененных слов: ', len(new_lines))
    file_result = 'new_file_result.txt'
    s = open(file_result, mode='w')
    s.writelines(new_lines)
    s.close()


if __name__ == '__main__':
    file_name1 = 'data1.txt'
    file_name2 = 'data2.txt'
    file_name3 = 'data_for_manipulation.txt'

    '''Задание 1
    TODO
    Дано два текстовых файла. Выяснить, совпадают ли их строки. 
    Если нет, то вывести несовпадающую строку из каждого файла.'''
    print('Задание 1 (сравнить строки файлов) - Результат:')
    compare_lines(file_name1, file_name2)

    '''Задание 2
    TODO
    Дан текстовый файл. Необходимо создать новый файл и записать в него 
    следующую статистику по исходному файлу:
    ■ Количество символов;
    ■ Количество строк;
    ■ Количество гласных букв;
    ■ Количество согласных букв; 
    ■ Количество цифр.'''
    print('Задание 2 (статистика по файлу) - Результат:')
    file_statistics(file_name1)

    '''Задание 3
    TODO
    Дан текстовый файл. Удалить из него последнюю строку. 
    Результат записать в другой файл.'''
    print('Задание 3 (удалить последнюю строку) - Результат:')
    remove_last_line(file_name1)

    '''Задание 4
    TODO
    Дан текстовый файл. Найти длину самой длинной строки.'''
    print('Задание 4 (самая длинная строка) - Результат:')
    longest_line(file_name1)
    
    '''Задание 5
    TODO
    Дан текстовый файл. 
    Посчитать сколько раз в нем встречается заданное пользователем слово.'''
    print('Задание 5 (к-во найденных слов) - Результат:')
    number_of_words_found(file_name3)

    '''Задание 6
    TODO
    Дан текстовый файл. Найти и заменить в нем заданное слово. 
    Что искать и на что заменять определяется пользователем.'''
    print('Задание 6 (найти , заменить) - Результат:')
    find_replace(file_name3)