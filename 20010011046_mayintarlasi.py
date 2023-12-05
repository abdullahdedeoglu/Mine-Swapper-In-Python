#Abdullah Dedeoglu 20010011046
import os
import random

mine_list = []
close_area = []
open_area = []

def clear():
    os.system('cls')

def mine_generator(size):
    num_mine = int((size * size) / 10 * 3)
    for i in range(num_mine):
        mine_list.append([0, 0])

    count = 0
    x = 0
    while count != num_mine:
        mine_list[count][0] = random.randint(1, size-1)
        mine_list[count][1] = random.randint(1, size-1)
        for i in range(num_mine):
            if (mine_list[count][0] == mine_list[i][0] and mine_list[count][1] == mine_list[i][1]) and i != count:
                x = 1
                break
        if x != 0:
            x = 0
            continue
        count = count+1

def mine_control(row, column):
    show_mine = 0
    #Sol üst kose kontrol
    if row == 0 and column == 0:       
        if game_area[1][0] == "X":
            show_mine += 1      
        if game_area[0][1] == "X": 
            show_mine += 1
        if game_area[1][1] == "X":
            show_mine += 1

        return show_mine

    #Sol alt kose kontrol
    elif row == size-1 and column == 0:
        if game_area[size-2][0] == "X":
            show_mine += 1        
        if game_area[size-1][1] == "X":
            show_mine += 1            
        if game_area[size-2][1] == "X":
            show_mine += 1

        return show_mine

    #Sag ust kose kontrol
    elif row == 0 and column == size-1:
        if game_area[0][size-2] == "X":
            show_mine += 1        
        if game_area[1][size-2] == "X":
            show_mine += 1            
        if game_area[1][size-1] == "X":
            show_mine += 1

        return show_mine

    #Sag alt kose kontrol
    elif row == size-1 and column == size-1:
        if game_area[size-1][size-2] == "X":
            show_mine += 1        
        if game_area[size-2][size-2] == "X":
            show_mine += 1            
        if game_area[size-2][size-1] == "X":
            show_mine += 1

        return show_mine

    #Sol kontrol 
    elif row != 0 and column == 0:
        if game_area[row-1][0] == "X":
            show_mine += 1
        if game_area[row+1][0] == "X":
            show_mine += 1
        if game_area[row-1][1] == "X":
            show_mine += 1
        if game_area[row][1] == "X":
            show_mine += 1
        if game_area[row+1][1] == "X":
            show_mine += 1

        return show_mine

    #Ust kontrol 
    elif row==0 and column != 0:
        if game_area[0][column-1] == "X":
            show_mine += 1
        if game_area[1][column-1] == "X":
            show_mine += 1
        if game_area[1][column] == "X":
            show_mine += 1
        if game_area[0][column+1] == "X":
            show_mine += 1
        if game_area[1][column+1] == "X":
            show_mine += 1

        return show_mine

   
    #Alt kontrol 
    elif row == size-1 and column != 0 or row==size-1 and column != size-1:
        if game_area[row][column-1] == "X":
            show_mine += 1
        if game_area[row-1][column-1] == "X":
            show_mine += 1
        if game_area[row-1][column] == "X":
            show_mine += 1
        if game_area[row-1][column+1] == "X":
            show_mine += 1
        if game_area[row][column+1] == "X":
            show_mine += 1

        return show_mine

    #Sag kontrol 
    elif row != 0 and column == size-1 or row != size-1 and column == size-1:
        if game_area[row-1][column] == "X":
            show_mine += 1
        if game_area[row-1][column-1] == "X":
            show_mine += 1
        if game_area[row][column-1] == "X":
            show_mine += 1
        if game_area[row+1][column-1] == "X":
            show_mine += 1
        if game_area[row+1][column] == "X":
            show_mine += 1

        return show_mine

    #Orta Kontrol
    else:
        if game_area[row-1][column-1] == "X":
            show_mine += 1
        if game_area[row][column-1] == "X":
            show_mine += 1
        if game_area[row+1][column-1] == "X":
            show_mine += 1
        if game_area[row+1][column] == "X":
            show_mine += 1
        if game_area[row+1][column+1] == "X":
            show_mine += 1
        if game_area[row][column+1] == "X":
            show_mine += 1
        if game_area[row-1][column+1] == "X":
            show_mine += 1
        if game_area[row-1][column] == "X":
            show_mine += 1

        return show_mine


while True:

    size = int(input("Boyutlari giriniz: "))

    if (size < 10):
        print("Oyun alani en az 10 olmalidir. Lutfen tekrar seciniz")
        continue

    mine_generator(size)

    game_area = [[0 for x in range(size)]
                for y in range(size)]

    for i in range(len(game_area)):
        for j in range(len(game_area[0])):
            game_area[i][j] = "?"

    for i in range(len(mine_list)):
        game_area[mine_list[i][0]][mine_list[i][1]] = "X"
    
    
    choose = int(input(
        "Oynamak istediginiz oyun modunu seciniz (Kapali oyun modu icin 1'i acik oyun modu icin 2'yi giriniz.)=> "))
    
    total_score = (size*size) - ((size * size) / 10 * 3)
    score = 0
    repeat_control = 0

    if choose == 1:

        close_area = [[x for x in range(size)]
            for y in range(size)]
       
        for i in range(len(close_area)):
            for j in range(len(close_area[0])): 
                close_area[i][j] = "?"
        
        while score != total_score:
            clear()
            for i in range(len(close_area)):
                for j in range(len(close_area[0])):
                    print((close_area[i][j]), end="  ")
                print("")
                

            if repeat_control != 0:
                print("Hatali secim yaptiniz, lutfen tekrar deneyiniz.")
                repeat_control = 0

            rowx=int(input("Bir satir degeri giriniz: "))
            columnx=int(input("Bir sutun degeri giriniz: "))
            row=rowx - 1
            column=columnx - 1
                
            if game_area[row][column]=="X":
                print("Maalesef kaybetiniz.")
                break

            elif close_area[row][column] != "?":
                repeat_control += 1
                continue
        
            show_mine = mine_control(row,column)
            close_area[row][column]=str(show_mine)
            score += 1

            if score == (size*size) - ((size * size) / 10 * 3):
                print("Oyunu kazandiniz.")
                break


    elif choose == 2:

        open_area = [[0 for x in range(size)]
                for y in range(size)]

        for i in range(len(open_area)):
            for j in range(len(open_area[0])):
                open_area[i][j] = "?"

        for i in range(len(mine_list)):
            open_area[mine_list[i][0]][mine_list[i][1]] = "X"

        while score != total_score:
            clear()
            for i in range(len(open_area)):
                for j in range(len(open_area[0])):
                    print((open_area[i][j]), end="  ")
                print("")
            
            if repeat_control != 0:
                print("Hatali secim yaptiniz, lutfen tekrar deneyiniz.")
                repeat_control = 0
            
            rowx=int(input("Bir satir degeri giriniz: "))
            columnx=int(input("Bir sutun degeri giriniz: "))
            row=rowx - 1
            column=columnx - 1
                
            if game_area[row][column]=="X":
                print("Maalesef kaybetiniz.")
                break
            
            elif open_area[row][column] != "?":
                repeat_control += 1
                continue
        
            show_mine = mine_control(row,column)
            open_area[row][column]=str(show_mine)

            score += 1

            if score == (size*size) - ((size * size) / 10 * 3):
                print("Oyunu kazandiniz.")
                break

    else:
        print("Hatali secim yaptiniz, oyun tekrar baslatiliyor...")
        continue

    print("Puaniniz: {}".format(score))
    print("1-> Yeni oyuna basla 2-> Oyundan cik\nLutfen secim yapiniz:")
    choose = int(input())
    if choose == 1:
        print("Yeni oyun baslatiliyor")
        continue
    elif choose == 2:
        print("Oyundan cikiliyor...")
        break
    else:
        print("Hatali secim yaptiniz, oyundan cikiliyor...")
        break
