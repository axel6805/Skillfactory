field= [[ '-', '-', '-'],
    [ '-', '-', '-'],
    [ '-', '-', '-']]
def showfield (f):
        print('  0 1 2')
        for i in range(len(f)):
            print(str(i), *f[i])
def user_input(f):
    while True:
        place=input('Введите координаты : ').split()
        if len(place)!=2:
            print('Введите только две координаты!')
            continue

        if not(place[0].isdigit()) and place[1].isdigit():
            print('Введите координаты в виде чисел!')
            continue
        x,y=map(int,place)
        if not(x>=0 and x<3 and y>=0 and y<3):
            print('Координаты вне поля!')
            continue
        if f[x][y]!='-':
            print('Клетка уже занята!')
            continue
        break
    return x,y
def winner(f,user):
    def check_line(a1,a2,a3,user):
        if a1==user and a2==user and a3==user:
            return True
    for i in range(3):
        if check_line(f[i][0],f[i][1],f[i][2], user) or \
                check_line(f[0][i],f[1][i],f[2][i], user) or \
                check_line(f[0][0],f[1][1],f[2][2], user) or \
                check_line(f[2][0],f[1][1],f[0][2], user):
                    return True
    return False
field=[['-']*3 for _ in range(3)]
count=0
while True:
    if count==9:
        print('Ничья!')
    if count%2==0:
        user='x'
    else:
        user='o'
    showfield(field)
    x,y=user_input(field)
    field[x][y]=user
    if winner(field,user):
        print(f"Поздравляем, {user} победил!")
        showfield((field))
        break
    count+=1


