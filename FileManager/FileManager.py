import os
import shutil

def dir_work():
    print ("1 - Создать папку" + "\n" + "2 - Удалить папку")
    mark = int(input())
    if mark == 1:
        print ("Введите полный путь до папки:" + '\n')
        name = str(input())
        if "ППП" not in name:
            print("Нельзя работать вне папки ППП")
        else:
            os.mkdir(name)
    if mark == 2:
        print ("Введите полный путь до папки:" + '\n')
        name = str(input())
        if "ППП" not in name:
            print("Нельзя работать вне папки ППП")
        else:
            os.rmdir(name)


def file_work():
    print ("Введите полный путь до файла:")
    mark = str(input())
    if "ППП" not in mark:
            print("Нельзя работать вне папки ППП")
    else:
        print ("1 - Создать файл" + "\n" + "2 - Удалить файл" + "\n" + "3 - Читать файл" + "\n" + "4 - Запись в файл" + "\n" + "5 - Переименовывание" + "\n" + "6 - Копирование")
        mark2 = int(input())
        if mark2 == 1:
           file = open(mark,'a+')
           file.close()
        elif mark2 == 2:
           os.remove(mark)
        elif mark2 == 3:
            with open(mark) as file:
                for line in file:
                    print(line)
        elif mark2 == 4:
            print("Введите строку для записи:")
            phrase = str(input())
            file = open(mark,'a+')
            file.write(phrase)
            file.close()
        elif mark2 == 5:
            print("введите новое название (полный путь)")
            mark3 = str(input())
            os.rename(mark, mark3)
        elif mark2 == 6:
             print("введите новый путь (полный)")
             mark3 = str(input())
             shutil.copyfile(mark, mark3)


while True:
    print ("1 - Создать/удалить папку" + '\n' + "2 - Запустить cmd" + '\n' + "3 - Создать/удалить файл/Работа с файлом")
    otvet = int(input())
    if otvet == 1:
        dir_work()
    elif otvet == 2:
        os.system('"C:\WINDOWS\system32\cmd.exe"')
    elif otvet == 3:
        file_work()
