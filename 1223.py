import random
N=random.randint(4,30)
k=0
while N>0:
    if k==0:
        print('Ваш ход')
        print(f'в данный момент камней в куче: {N}')
        if N==1:
            print('вы можете и должны взять один камень')
            a=1
        elif N==2:
            print('вы можете взять 1 или 2 камня'
                  '/n введите количество камней, которое хотите взять')
            while(1):
                try:
                    a=int(input())
                except:
                    print('Ошибка: некоректный ввод. Попробуйте ввести еще раз')
                    continue
                if a!=2 and a!=1:
                    print('Ошибка: вам нужно ввести 1 или 2. Попробуйти еще раз')
                else:
                    break
        elif N>=3:
            print('вы можете взять 1, 2 или 3 камня\n'
                  'введите количество камней, которое хотите взять')
            while (1):
                try:
                    a = int(input())
                except:
                    print('Ошибка: некоректный ввод. Попробуйте ввести еще раз')
                    continue
                if a!=3 and a != 2 and a != 1:
                    print('Ошибка: вам нужно ввести 1, 2 или 3. Попробуйти еще раз')
                else:
                    break
        N=N-a
        k=1
        print(f'камней в куче: {N}')
    elif k==1:
        print('ход компьютера:')
        if N>=3:
            b=random.randint(1,3)
        elif N==2:
            b=random.randint(1,2)
        elif N==1:
            b=1
        N=N-b
        k=0
        print(f'компьютор взял {b} камень(я)')
        print(f'комней в куче: {N}')
if k==1:
    print('Вы проиграли :(')
elif k==0:
    print('Вы победили :)')