from colorama import init
from colorama import Back, Style
from os import system, name
from time import sleep
import csv
import os
#cd \STUDY\ITMO\1_course_ITMO\1_semester(1)\Pyton\Laboratory_Work_2\Scripts
print('Флаг японии')
init(autoreset=True)
print(Back.LIGHTWHITE_EX + '                                                            ')
print(Back.LIGHTWHITE_EX + '                                                            ')
print(Back.LIGHTWHITE_EX + '                           '+'\033[41m'+'      '+Back.LIGHTWHITE_EX + '                           ')
print(Back.LIGHTWHITE_EX + '                        '+Back.RED+'            '+Back.LIGHTWHITE_EX + '                        ')
print(Back.LIGHTWHITE_EX + '                     '+Back.RED+'                  '+Back.LIGHTWHITE_EX + '                     ')
print(Back.LIGHTWHITE_EX + '                  '+'\033[41m'+'                        '+Back.LIGHTWHITE_EX + '                  ')
print(Back.LIGHTWHITE_EX + '                '+Back.RED+'                            '+Back.LIGHTWHITE_EX + '                ')
print(Back.LIGHTWHITE_EX + '                '+'\033[41m'+'                            '+Back.LIGHTWHITE_EX + '                ')
print(Back.LIGHTWHITE_EX + '                  '+Back.RED+'                        '+Back.LIGHTWHITE_EX + '                  ')
print(Back.LIGHTWHITE_EX + '                     '+'\033[41m'+'                  '+Back.LIGHTWHITE_EX + '                     ')
print(Back.LIGHTWHITE_EX + '                        '+'\033[41m'+'            '+Back.LIGHTWHITE_EX + '                        ')
print(Back.LIGHTWHITE_EX + '                           '+'\033[41m'+'      '+Back.LIGHTWHITE_EX + '                           ')
print(Back.LIGHTWHITE_EX + '                                                            ')
print(Back.LIGHTWHITE_EX + '                                                            ')
print('\n\n\n')

sleep(1.5)

print('Узор')

print('         '+'\033[40m'+'   '+ '\033[0m'+'               ' +'\033[40m'+'   '+ '\033[0m')
print('      '+'\033[40m'+'   '+ '\033[0m'+'   '+'\033[40m'+'   '+ '\033[0m'+'         ' +'\033[40m'+'   '+ '\033[0m'+'   '+'\033[40m'+'   '+ '\033[0m')
print('   '+'\033[40m'+'   '+ '\033[0m'+'         '+'\033[40m'+'   '+ '\033[0m'+'   ' +'\033[40m'+'   '+ '\033[0m'+'         '+'\033[40m'+'   '+ '\033[0m')
print('\033[40m'+'   '+ '\033[0m'+'               '+'\033[40m'+'   '+ '\033[0m'+'' +'\033[40m'+''+ '\033[0m'+'               '+'\033[40m'+'   '+ '\033[0m')
print('   '+'\033[40m'+'   '+ '\033[0m'+'         '+'\033[40m'+'   '+ '\033[0m'+'   ' +'\033[40m'+'   '+ '\033[0m'+'         '+'\033[40m'+'   '+ '\033[0m')
print('      '+'\033[40m'+'   '+ '\033[0m'+'   '+'\033[40m'+'   '+ '\033[0m'+'         ' +'\033[40m'+'   '+ '\033[0m'+'   '+'\033[40m'+'   '+ '\033[0m')
print('         '+'\033[40m'+'   '+ '\033[0m'+'               ' +'\033[40m'+'   '+ '\033[0m')

sleep(1.5)


print('\n\n\n График у=3х')
print('^')
print('|  x')
print('12 ' +Back.LIGHTWHITE_EX +'           '+Back.BLACK + ' '+Back.LIGHTWHITE_EX + '                                ')
print('11 ' +Back.LIGHTWHITE_EX +'          '+Back.BLACK + ' '+Back.LIGHTWHITE_EX + '                                 ')
print('10 ' +Back.LIGHTWHITE_EX +'         '+Back.BLACK + ' '+Back.LIGHTWHITE_EX + '                                  ')
print('9  ' +Back.LIGHTWHITE_EX +'________'+Back.BLACK + ' '+Back.LIGHTWHITE_EX + '                                   ')
print('8  ' +Back.LIGHTWHITE_EX +'       '+Back.BLACK + ' '+Back.LIGHTWHITE_EX + ' |                                  ')
print('7  ' +Back.LIGHTWHITE_EX +'      '+Back.BLACK + ' '+Back.LIGHTWHITE_EX + '  |                                  ')
print('6  ' +Back.LIGHTWHITE_EX +'     '+Back.BLACK + ' '+Back.LIGHTWHITE_EX + '   |                                  ')
print('5  ' +Back.LIGHTWHITE_EX +'    '+Back.BLACK + ' '+Back.LIGHTWHITE_EX + '    |                                  ')
print('4  ' +Back.LIGHTWHITE_EX +'   '+Back.BLACK + ' '+Back.LIGHTWHITE_EX + '     |                                  ')
print('3  ' +Back.LIGHTWHITE_EX +'  '+Back.BLACK + ' '+Back.LIGHTWHITE_EX + '      |                                  ')
print('2  ' +Back.LIGHTWHITE_EX +' '+Back.BLACK + ' '+Back.LIGHTWHITE_EX + '       |                                  ')
print('1  ' + Back.BLACK + ' '+Back.LIGHTWHITE_EX + '        |                                  ')
print('   0  1  2  3  4  5  6  7  8  9            -> ')
print('                                           y')

sleep(1.5)
print('\n\n\n')
c=0
c1=0
c2=0
with open('D:/STUDY/ITMO/1_course_ITMO/1_semester(1)/Pyton/Lab-1/books.csv', "r") as csvfile:
    table = csv.reader(csvfile, delimiter=";")
    for row in list(table):
        if c>0:

            if float(row[7].replace(',', '.'))>100:
                c1+=1
            else:
                c2+=1
        c+=1
    costFirstProcent = str(c1 / (c1 + c2) * 100)
    costSecondProcent = str(c2 / (c1 + c2) * 100)

print(f'{costFirstProcent[:5] } %,{costSecondProcent[:5]} %')

print('Диаграмма Книг до 100 рублей и дороже')
cost1 = int(c1 / (c1 + c2)*100)
cost2 = int(c2 / (c1 + c2) * 100)


print(Back.LIGHTWHITE_EX + '                                                                ')
print(Back.LIGHTWHITE_EX + '                                                                ')
print(Back.LIGHTWHITE_EX + f'  {costFirstProcent[:5]} %  дороже 100Р                                          ')
for i in range(0,  cost1):
    print(Back.BLUE + ' ', end='')
print(Back.LIGHTWHITE_EX + '         ')
print(Back.LIGHTWHITE_EX + '                                                                ')
print(Back.LIGHTWHITE_EX + f'    {costSecondProcent[:5]} %  дешевле 100Р                                       ')
for i in range(0,  cost2):
    print(Back.GREEN + ' ', end='')

print(Back.LIGHTWHITE_EX + '                    ')
print(Back.LIGHTWHITE_EX + '                                                                ')
print(Back.LIGHTWHITE_EX + '                                                                ')
sleep(1.5)
print('\n\n\n Дополнительное задание')
sleep(1.5)

system('cls')

for cx in range(0,10):

    print(Back.LIGHTWHITE_EX + '                                                               ')
    print(Back.LIGHTWHITE_EX + '                           '+Back.LIGHTYELLOW_EX+'      '+Back.LIGHTWHITE_EX + '                              ')
    print(Back.LIGHTWHITE_EX + '                        '+Back.LIGHTYELLOW_EX+'            '+Back.LIGHTWHITE_EX + '                           ')
    print(Back.LIGHTWHITE_EX + '                     '+Back.LIGHTYELLOW_EX+'                  '+Back.LIGHTWHITE_EX + '                        ')
    print(Back.LIGHTWHITE_EX + '                  '+Back.LIGHTYELLOW_EX+'      '+Back.LIGHTWHITE_EX+'     '+Back.LIGHTYELLOW_EX+'  '+Back.LIGHTWHITE_EX+'     '+Back.LIGHTYELLOW_EX+'      '+Back.LIGHTWHITE_EX + '                     ')
    print(Back.LIGHTWHITE_EX + '               '+Back.LIGHTYELLOW_EX+'         '+Back.LIGHTWHITE_EX+'  ●  '+Back.LIGHTYELLOW_EX+'  '+Back.LIGHTWHITE_EX+'  ●  '+Back.LIGHTYELLOW_EX+'         '+Back.LIGHTWHITE_EX + '                  ')
    print(Back.LIGHTWHITE_EX + '               '+Back.LIGHTYELLOW_EX+'         '+Back.LIGHTWHITE_EX+'     '+Back.LIGHTYELLOW_EX+'  '+Back.LIGHTWHITE_EX+'     '+Back.LIGHTYELLOW_EX+'         '+Back.LIGHTWHITE_EX + '                  ')
    print(Back.LIGHTWHITE_EX + '             '+Back.LIGHTYELLOW_EX+'                                  '+Back.LIGHTWHITE_EX + '                ')
    print(Back.LIGHTWHITE_EX + '             '+Back.LIGHTYELLOW_EX+'                                  '+Back.LIGHTWHITE_EX + '                ')
    print(Back.LIGHTWHITE_EX + '                '+Back.LIGHTYELLOW_EX+ '\033[31m'+'           /‾‾‾\             '+Back.LIGHTWHITE_EX + '                  ')
    print(Back.LIGHTWHITE_EX + '                  '+Back.LIGHTYELLOW_EX+ '\033[31m'+'         \___/          '+Back.LIGHTWHITE_EX + '                     ')
    print(Back.LIGHTWHITE_EX + '                     '+Back.LIGHTYELLOW_EX+'                  '+Back.LIGHTWHITE_EX + '                        ')
    print(Back.LIGHTWHITE_EX + '                        '+Back.LIGHTYELLOW_EX+'            '+Back.LIGHTWHITE_EX + '                           ')
    print(Back.LIGHTWHITE_EX + '                           '+Back.LIGHTYELLOW_EX+'      '+Back.LIGHTWHITE_EX + '                              ')
    print(Back.LIGHTWHITE_EX + '                                                               ')



    #sleep(1)
    system('cls')


    print(Back.LIGHTWHITE_EX + '                                                               ')
    print(Back.LIGHTWHITE_EX + '                           '+Back.LIGHTYELLOW_EX+'      '+Back.LIGHTWHITE_EX + '                              ')
    print(Back.LIGHTWHITE_EX + '                        '+Back.LIGHTYELLOW_EX+'            '+Back.LIGHTWHITE_EX + '                           ')
    print(Back.LIGHTWHITE_EX + '                     '+Back.LIGHTYELLOW_EX+'                  '+Back.LIGHTWHITE_EX + '                        ')
    print(Back.LIGHTWHITE_EX + '                  '+Back.LIGHTYELLOW_EX+'      '+Back.WHITE+'     '+Back.LIGHTYELLOW_EX+'  '+Back.WHITE+'     '+Back.LIGHTYELLOW_EX+'      '+Back.LIGHTWHITE_EX + '                     ')
    print(Back.LIGHTWHITE_EX + '               '+Back.LIGHTYELLOW_EX+'         '+Back.LIGHTWHITE_EX+'  ●  '+Back.LIGHTYELLOW_EX+'  '+Back.LIGHTWHITE_EX+'  ●  '+Back.LIGHTYELLOW_EX+'         '+Back.LIGHTWHITE_EX + '                  ')
    print(Back.LIGHTWHITE_EX + '               '+Back.LIGHTYELLOW_EX+'         '+Back.WHITE+'     '+Back.LIGHTYELLOW_EX+'  '+Back.WHITE+'     '+Back.LIGHTYELLOW_EX+'         '+Back.LIGHTWHITE_EX + '                  ')
    print(Back.LIGHTWHITE_EX + '             '+Back.LIGHTYELLOW_EX+'                                  '+Back.LIGHTWHITE_EX + '                ')
    print(Back.LIGHTWHITE_EX + '             '+Back.LIGHTYELLOW_EX+'                                  '+Back.LIGHTWHITE_EX + '                ')
    print(Back.LIGHTWHITE_EX + '                '+Back.LIGHTYELLOW_EX+'                             '+Back.LIGHTWHITE_EX + '                  ')
    print(Back.LIGHTWHITE_EX + '                  '+Back.LIGHTYELLOW_EX+ '\033[31m'+'         \___/          '+Back.LIGHTWHITE_EX + '                     ')
    print(Back.LIGHTWHITE_EX + '                     '+Back.LIGHTYELLOW_EX+'                  '+Back.LIGHTWHITE_EX + '                        ')
    print(Back.LIGHTWHITE_EX + '                        '+Back.LIGHTYELLOW_EX+'            '+Back.LIGHTWHITE_EX + '                           ')
    print(Back.LIGHTWHITE_EX + '                           '+Back.LIGHTYELLOW_EX+'      '+Back.LIGHTWHITE_EX + '                              ')
    print(Back.LIGHTWHITE_EX + '                                                               ')

    #sleep(1)
    system('cls')


    print(Back.LIGHTWHITE_EX + '                                                               ')
    print(Back.LIGHTWHITE_EX + '                           '+Back.LIGHTYELLOW_EX+'      '+Back.LIGHTWHITE_EX + '                              ')
    print(Back.LIGHTWHITE_EX + '                        '+Back.LIGHTYELLOW_EX+'            '+Back.LIGHTWHITE_EX + '                           ')
    print(Back.LIGHTWHITE_EX + '                     '+Back.LIGHTYELLOW_EX+'                  '+Back.LIGHTWHITE_EX + '                        ')
    print(Back.LIGHTWHITE_EX + '                  '+Back.LIGHTYELLOW_EX+'      '+Back.WHITE+'     '+Back.LIGHTYELLOW_EX+'  '+Back.WHITE+'     '+Back.LIGHTYELLOW_EX+'      '+Back.LIGHTWHITE_EX + '                     ')
    print(Back.LIGHTWHITE_EX + '               '+Back.LIGHTYELLOW_EX+'         '+Back.LIGHTWHITE_EX+' ●   '+Back.LIGHTYELLOW_EX+'  '+Back.LIGHTWHITE_EX+' ●   '+Back.LIGHTYELLOW_EX+'         '+Back.LIGHTWHITE_EX + '                  ')
    print(Back.LIGHTWHITE_EX + '               '+Back.LIGHTYELLOW_EX+'         '+Back.WHITE+'     '+Back.LIGHTYELLOW_EX+'  '+Back.WHITE+'     '+Back.LIGHTYELLOW_EX+'         '+Back.LIGHTWHITE_EX + '                  ')
    print(Back.LIGHTWHITE_EX + '             '+Back.LIGHTYELLOW_EX+'                                  '+Back.LIGHTWHITE_EX + '                ')
    print(Back.LIGHTWHITE_EX + '             '+Back.LIGHTYELLOW_EX+'                                  '+Back.LIGHTWHITE_EX + '                ')
    print(Back.LIGHTWHITE_EX + '                '+Back.LIGHTYELLOW_EX+'                             '+Back.LIGHTWHITE_EX + '                  ')
    print(Back.LIGHTWHITE_EX + '                  '+Back.LIGHTYELLOW_EX+ '\033[31m'+'         \___/          '+Back.LIGHTWHITE_EX + '                     ')
    print(Back.LIGHTWHITE_EX + '                     '+Back.LIGHTYELLOW_EX+'                  '+Back.LIGHTWHITE_EX + '                        ')
    print(Back.LIGHTWHITE_EX + '                        '+Back.LIGHTYELLOW_EX+'            '+Back.LIGHTWHITE_EX + '                           ')
    print(Back.LIGHTWHITE_EX + '                           '+Back.LIGHTYELLOW_EX+'      '+Back.LIGHTWHITE_EX + '                              ')
    print(Back.LIGHTWHITE_EX + '                                                               ')

    #sleep(1)
    system('cls')

    print(Back.LIGHTWHITE_EX + '                                                               ')
    print(Back.LIGHTWHITE_EX + '                           '+Back.LIGHTYELLOW_EX+'      '+Back.LIGHTWHITE_EX + '                              ')
    print(Back.LIGHTWHITE_EX + '                        '+Back.LIGHTYELLOW_EX+'            '+Back.LIGHTWHITE_EX + '                           ')
    print(Back.LIGHTWHITE_EX + '                     '+Back.LIGHTYELLOW_EX+'                  '+Back.LIGHTWHITE_EX + '                        ')
    print(Back.LIGHTWHITE_EX + '                  '+Back.LIGHTYELLOW_EX+'      '+Back.WHITE+'     '+Back.LIGHTYELLOW_EX+'  '+Back.WHITE+'     '+Back.LIGHTYELLOW_EX+'      '+Back.LIGHTWHITE_EX + '                     ')
    print(Back.LIGHTWHITE_EX + '               '+Back.LIGHTYELLOW_EX+'         '+Back.LIGHTWHITE_EX+'●    '+Back.LIGHTYELLOW_EX+'  '+Back.LIGHTWHITE_EX+'●    '+Back.LIGHTYELLOW_EX+'         '+Back.LIGHTWHITE_EX + '                  ')
    print(Back.LIGHTWHITE_EX + '               '+Back.LIGHTYELLOW_EX+'         '+Back.WHITE+'     '+Back.LIGHTYELLOW_EX+'  '+Back.WHITE+'     '+Back.LIGHTYELLOW_EX+'         '+Back.LIGHTWHITE_EX + '                  ')
    print(Back.LIGHTWHITE_EX + '             '+Back.LIGHTYELLOW_EX+'                                  '+Back.LIGHTWHITE_EX + '                ')
    print(Back.LIGHTWHITE_EX + '             '+Back.LIGHTYELLOW_EX+'                                  '+Back.LIGHTWHITE_EX + '                ')
    print(Back.LIGHTWHITE_EX + '                '+Back.LIGHTYELLOW_EX+'                             '+Back.LIGHTWHITE_EX + '                  ')
    print(Back.LIGHTWHITE_EX + '                  '+Back.LIGHTYELLOW_EX+ '\033[31m'+'         \___/          '+Back.LIGHTWHITE_EX + '                     ')
    print(Back.LIGHTWHITE_EX + '                     '+Back.LIGHTYELLOW_EX+'                  '+Back.LIGHTWHITE_EX + '                        ')
    print(Back.LIGHTWHITE_EX + '                        '+Back.LIGHTYELLOW_EX+'            '+Back.LIGHTWHITE_EX + '                           ')
    print(Back.LIGHTWHITE_EX + '                           '+Back.LIGHTYELLOW_EX+'      '+Back.LIGHTWHITE_EX + '                              ')
    print(Back.LIGHTWHITE_EX + '                                                               ')

    #sleep(1)
    system('cls')

    print(Back.LIGHTWHITE_EX + '                                                               ')
    print(Back.LIGHTWHITE_EX + '                           '+Back.LIGHTYELLOW_EX+'      '+Back.LIGHTWHITE_EX + '                              ')
    print(Back.LIGHTWHITE_EX + '                        '+Back.LIGHTYELLOW_EX+'            '+Back.LIGHTWHITE_EX + '                           ')
    print(Back.LIGHTWHITE_EX + '                     '+Back.LIGHTYELLOW_EX+'                  '+Back.LIGHTWHITE_EX + '                        ')
    print(Back.LIGHTWHITE_EX + '                  '+Back.LIGHTYELLOW_EX+'      '+Back.WHITE+'     '+Back.LIGHTYELLOW_EX+'  '+Back.WHITE+'     '+Back.LIGHTYELLOW_EX+'      '+Back.LIGHTWHITE_EX + '                     ')
    print(Back.LIGHTWHITE_EX + '               '+Back.LIGHTYELLOW_EX+'         '+Back.LIGHTWHITE_EX+' ●   '+Back.LIGHTYELLOW_EX+'  '+Back.LIGHTWHITE_EX+' ●   '+Back.LIGHTYELLOW_EX+'         '+Back.LIGHTWHITE_EX + '                  ')
    print(Back.LIGHTWHITE_EX + '               '+Back.LIGHTYELLOW_EX+'         '+Back.WHITE+'     '+Back.LIGHTYELLOW_EX+'  '+Back.WHITE+'     '+Back.LIGHTYELLOW_EX+'         '+Back.LIGHTWHITE_EX + '                  ')
    print(Back.LIGHTWHITE_EX + '             '+Back.LIGHTYELLOW_EX+'                                  '+Back.LIGHTWHITE_EX + '                ')
    print(Back.LIGHTWHITE_EX + '             '+Back.LIGHTYELLOW_EX+'                                  '+Back.LIGHTWHITE_EX + '                ')
    print(Back.LIGHTWHITE_EX + '                '+Back.LIGHTYELLOW_EX+'                             '+Back.LIGHTWHITE_EX + '                  ')
    print(Back.LIGHTWHITE_EX + '                  '+Back.LIGHTYELLOW_EX+ '\033[31m'+'         \___/          '+Back.LIGHTWHITE_EX + '                     ')
    print(Back.LIGHTWHITE_EX + '                     '+Back.LIGHTYELLOW_EX+'                  '+Back.LIGHTWHITE_EX + '                        ')
    print(Back.LIGHTWHITE_EX + '                        '+Back.LIGHTYELLOW_EX+'            '+Back.LIGHTWHITE_EX + '                           ')
    print(Back.LIGHTWHITE_EX + '                           '+Back.LIGHTYELLOW_EX+'      '+Back.LIGHTWHITE_EX + '                              ')
    print(Back.LIGHTWHITE_EX + '                                                               ')
    system('cls')


    print(Back.LIGHTWHITE_EX + '                                                               ')
    print(Back.LIGHTWHITE_EX + '                           '+Back.LIGHTYELLOW_EX+'      '+Back.LIGHTWHITE_EX + '                              ')
    print(Back.LIGHTWHITE_EX + '                        '+Back.LIGHTYELLOW_EX+'            '+Back.LIGHTWHITE_EX + '                           ')
    print(Back.LIGHTWHITE_EX + '                     '+Back.LIGHTYELLOW_EX+'                  '+Back.LIGHTWHITE_EX + '                        ')
    print(Back.LIGHTWHITE_EX + '                  '+Back.LIGHTYELLOW_EX+'      '+Back.WHITE+'     '+Back.LIGHTYELLOW_EX+'  '+Back.WHITE+'     '+Back.LIGHTYELLOW_EX+'      '+Back.LIGHTWHITE_EX + '                     ')
    print(Back.LIGHTWHITE_EX + '               '+Back.LIGHTYELLOW_EX+'         '+Back.LIGHTWHITE_EX+'  ●  '+Back.LIGHTYELLOW_EX+'  '+Back.LIGHTWHITE_EX+'  ●  '+Back.LIGHTYELLOW_EX+'         '+Back.LIGHTWHITE_EX + '                  ')
    print(Back.LIGHTWHITE_EX + '               '+Back.LIGHTYELLOW_EX+'         '+Back.WHITE+'     '+Back.LIGHTYELLOW_EX+'  '+Back.WHITE+'     '+Back.LIGHTYELLOW_EX+'         '+Back.LIGHTWHITE_EX + '                  ')
    print(Back.LIGHTWHITE_EX + '             '+Back.LIGHTYELLOW_EX+'                                  '+Back.LIGHTWHITE_EX + '                ')
    print(Back.LIGHTWHITE_EX + '             '+Back.LIGHTYELLOW_EX+'                                  '+Back.LIGHTWHITE_EX + '                ')
    print(Back.LIGHTWHITE_EX + '                '+Back.LIGHTYELLOW_EX+'                             '+Back.LIGHTWHITE_EX + '                  ')
    print(Back.LIGHTWHITE_EX + '                  '+Back.LIGHTYELLOW_EX+ '\033[31m'+'         \___/          '+Back.LIGHTWHITE_EX + '                     ')
    print(Back.LIGHTWHITE_EX + '                     '+Back.LIGHTYELLOW_EX+'                  '+Back.LIGHTWHITE_EX + '                        ')
    print(Back.LIGHTWHITE_EX + '                        '+Back.LIGHTYELLOW_EX+'            '+Back.LIGHTWHITE_EX + '                           ')
    print(Back.LIGHTWHITE_EX + '                           '+Back.LIGHTYELLOW_EX+'      '+Back.LIGHTWHITE_EX + '                              ')
    print(Back.LIGHTWHITE_EX + '                                                               ')
    system('cls')






