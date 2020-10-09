"""
Author: https://github.com/Romawechka
        https://t.me/Romawechka
Python version 3.8
"""

import os
import sys


def list_files(startpath=os.getcwd(), branch='├', last_branch='└', trunk='|', sep=' ', connection='─'):
    """
    Function imitating the tree command

     Parameters:

         ----path----
         startpath specifies the starting path, if not specified, then the starting path from the directory in which the file is located

         ---- Branch elements ----
         branch specifies the symbol for a branch with a branch, if not specified then '├'
         last_branch sets the symbol for the last branch, if not specified then '└'
         trunk specifies the symbol for the branch, if not specified then '|'
         sep sets the character to separate, if not specified then ''
         connection specifies the symbol for the branch, if not specified then '─'

     Example: python Main.py startpath="D:\Project\Python project" branch=├
     P.S. arguments must be separated by a space, path must be in quotes
    """
    full_str = ''

    # список с уровнями подкаталогов
    dir = []
    count_dir = -1
    count_files = 0
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)

        # определим прошлый путь
        last_path = ''
        for el in root.split('\\')[0:len(root.split('\\')) - 1]:
            last_path += '\\' + el
        # если прошлый путь это диск
        if last_path.endswith(':'):
            last_path += '\\'

        # Необходимо определить каталоги по прошлому пути
        last_dirs = os.listdir(last_path[1:])
        _last_dirs = []
        for el in last_dirs:
            if not last_path[1:].endswith('\\'):
                _path = last_path[1:] + '\\' + el
            else:
                _path = last_path[1:] + el
            if os.path.isdir(_path):
                _last_dirs.append(el)

        last_dirs = _last_dirs

        # для красивого отображения подкаталогов
        prefix = ''
        for i in range(level):
            if i != level:
                if i in dir and level - 1 != 0 and i != level - 1:
                    prefix += trunk
                if i != level - 1:
                    if prefix == '':
                        prefix += sep * 4
                    else:
                        if prefix.endswith(' '):
                            prefix += sep
                        prefix += sep * 3

        # определяем данный каталог последний или нет
        if last_dirs.index(os.path.basename(root)) == len(last_dirs) - 1:
            indent = sep * 4 * (level - 1) + last_branch + connection * 3
            # если данный каталог/файл был последним, удаляем из списка подкаталогов текущий уровень
            if level - 1 in dir:
                dir.pop(dir.index(level - 1))
        else:
            # определяем является ли текущий каталог стартовым
            if os.path.basename(root) != startpath.split('\\')[len(startpath.split('\\')) - 1]:
                indent = sep * 4 * (level - 1) + branch + connection * 3

                # т.к. данный каталог/файл не последний, заносим уровень подкаталога в список, если его там нету
                if level - 1 not in dir:
                    dir.append(level - 1)
            else:
                indent = ''

        # выводим каталог
        full_str += f'{prefix}{indent[len(prefix):]}{os.path.basename(root)}\n'
        count_dir += 1
        # выводим файлы внутри каталога
        for f in files:
            count_files += 1

            # для красивого отображения файлов
            prefix = ''
            for i in range(level):
                if i in dir:
                    prefix += trunk
                else:
                    prefix += sep
                if i != level - 1:
                    prefix += sep * 3

            # определяем данный файл последний или нет
            if (files.index(f) == len(files) - 1) and len(dirs) == 0:
                subindent = sep * 4 * (level) + last_branch + connection * 3
            else:
                subindent = sep * 4 * (level) + branch + connection * 3

            # выводим файл
            full_str += f'{prefix}{subindent[len(prefix):]}{f}\n'

    # Вывод общего колличества каталогов и файлов
    full_str += f'\n{count_dir} directories, {count_files} files'
    return full_str


# если запуск из консоли
if __name__ == "__main__":
    # получаем список аргументов из консоли
    list_arg = sys.argv[1:]
    # задаем стандартные значения
    startpath = os.getcwd()
    branch = '├'
    last_branch = '└'
    trunk = '|'
    sep = ' '
    connection = '─'
    for el in list_arg:
        if 'startpath' in el:
            startpath = el.split('=')[1].replace('\"', '').replace('\'', '')
        elif 'branch' in el:
            branch = el.split('=')[1]
        elif 'last_branch' in el:
            last_branch = el.split('=')[1]
        elif 'trunk' in el:
            trunk = el.split('=')[1]
        elif 'sep' in el:
            sep = el.split('=')[1]
        elif 'connection' in el:
            connection = el.split('=')[1]

    print(list_files(startpath=startpath, branch=branch, last_branch=last_branch,
               trunk=trunk, sep=sep, connection=connection))
