# from random import randint

# def candies(number,count,max_win_pos,cycle):
#     if count == 0:
#         return print(f'Победил {number} игрок')
#     if number == 1:
#         player_candies = int(input('Выберите количество конфет от 1 до 28 '))
#         count -= player_candies
#         print(f'осталось {count} конфет')
#         if count != 0:
#             number = 2
#     elif number == 2:
#         if count != max_win_pos - (29 * cycle):
#             help = count
#             count = (max_win_pos - (29 * (cycle)))
#             print (f'Игрок 2 взял {help - count} конфет, всего конфет осталось {count}')
#         else:
#             help = count
#             count -= randint(1,28)
#             print (f'Игрок 2 взял {help - count} конфет, всего конфет осталось {count}')
#         if count != 0:
#             number = 1  
#         cycle += 1
#     candies(number,count,max_win_pos,cycle)
    
# first_number = 1
# count = 2021
# cycle = 0
# max_win_pos = 29 * (count // 29)
# candies(first_number,count,max_win_pos,cycle)

# 3. Создайте программу для игры в ""Крестики-нолики"".

# def print_mark(player,mas):
#     if mas[0][0] == 'X' and mas[1][1] == 'X' and mas[2][2] == 'X':
#         return print(f'Выиграл первый игрок')
#     elif mas[0][2] == 'X' and mas[1][1] == 'X' and mas[2][0] == 'X':
#         return print(f'Выиграл первый игрок')
#     elif mas[0][0] == 'O' and mas[1][1] == 'O' and mas[2][2] == 'O':
#         return print(f'Выиграл второй игрок')
#     elif mas[0][2] == 'O' and mas[1][1] == 'O' and mas[2][0] == 'O':
#         return print(f'Выиграл второй игрок')
#     if player == 1:
#         mark = 'X'
#         pos = int(input(f'Выберите номер ячейки куда поставить {mark} '))
#         player = 2
#     else:
#         mark = 'O'
#         pos = int(input(f'Выберите номер ячейки куда поставить {mark} '))
#         player = 1
#     if pos == 1:
#         mas[0][0] = f'{mark}'
#         for i in range(0,len(mas)):
#             for k in range(0,len(mas[i])):
#                 print(mas[i][k],end = ' ')
#             print()
#     elif pos ==2:
#         mas[0][1] = f'{mark}'
#         for i in range(0,len(mas)):
#             for k in range(0,len(mas[i])):
#                 print(mas[i][k],end = ' ')
#             print()
#     elif pos ==3:
#         mas[0][2] = f'{mark}'
#         for i in range(0,len(mas)):
#             for k in range(0,len(mas[i])):
#                 print(mas[i][k],end = ' ')
#             print()
#     elif pos ==4:
#         mas[1][0] = f'{mark}'
#         for i in range(0,len(mas)):
#             for k in range(0,len(mas[i])):
#                 print(mas[i][k],end = ' ')
#             print()
#     elif pos ==5:
#         mas[1][1] = f'{mark}'
#         for i in range(0,len(mas)):
#             for k in range(0,len(mas[i])):
#                 print(mas[i][k],end = ' ')
#             print()
#     elif pos ==6:
#         mas[1][2] = f'{mark}'
#         for i in range(0,len(mas)):
#             for k in range(0,len(mas[i])):
#                 print(mas[i][k],end = ' ')
#             print()
#     elif pos ==7:
#         mas[2][0] = f'{mark}'
#         for i in range(0,len(mas)):
#             for k in range(0,len(mas[i])):
#                 print(mas[i][k],end = ' ')
#             print()
#     elif pos ==8:
#         mas[2][1] = f'{mark}'
#         for i in range(0,len(mas)):
#             for k in range(0,len(mas[i])):
#                 print(mas[i][k],end = ' ')
#             print()
#     elif pos ==9:
#         mas[2][2] = f'{mark}'
#         for i in range(0,len(mas)):
#             for k in range(0,len(mas[i])):
#                 print(mas[i][k],end = ' ')
#             print()
#     print_mark(player,mas)
# mas = [[1,2,3],[4,5,6],[7,8,9]]
# for i in range(0,len(mas)):
#     for k in range(0,len(mas[i])):
#         print(mas[i][k],end = ' ')
#     print()
# print_mark(1,mas)

# 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

# def rle(input):
#     count = 1
#     list = []
#     for i in range(0,len(input)):
#         if  i == len(input)-1:
#             list.append(f'{count}{input[i]}')
#         elif input[i] == input[i+1]:
#             count += 1 
#         else:
#             list.append(f'{count}{input[i]}')
#             count = 1
#     return list
# input = 'aaaabbfffeeeedddss'
# print(list(filter(rle,input)))