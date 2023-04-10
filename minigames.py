import random
from copy import deepcopy

# - Digunakan untuk mencetak main board
def b_display():  
    for i, value in enumerate(vboard1, 1):
        if(i%3 == 1):
            print('||' + value, end='||')
        else:
            print(value, end='||')
        if i % 3 == 0: print()

# - untuk saya(x) untuk main giliran
def action_h(): 
    c = int(input('Hallo, Giliran mu! Pilih salah satu nomor untuk bermain (1 - 9): '))
    print("--------------------------")
    if c == vboard[c - 1]:
        vboard[c - 1] = current_player
        vboard1[c - 1] = current_player

# - untuk komputer(o) untuk main giliran
def action_a():  
    print("Giliran Kamu untuk memilih:")
    c = minimax(vboard, depth(vboard), True)
    c = c[1]
    vboard[c - 1] = current_player
    vboard1[c - 1] = current_player

# - algoritma Minimax buat mencari ruang pengembalian langkah 
def minimax(b, depth_of_the_board, max_player): 
    if (depth(b) == 0) or (is_terminal(b) == True):
        return evaluate(b)

    if max_player:
        max_eval, best_move = float("-inf"), -1
        for move, child in moves_boards(b):
            ev = minimax(child, depth_of_the_board - 1, False)[0]
            max_eval = max(ev, max_eval)
            if ev == max_eval:  best_move = move
        return max_eval, best_move

    else:
        min_eval = float('inf')
        for move, child in moves_boards(b, 'X'):
            ev = minimax(child, depth_of_the_board - 1, True)[0]
            min_eval = min(ev, min_eval)
        return min_eval, -1

def depth(b):  # - Mengembalikan jumlah nilai yang tidak diambil
    d = 0
    for i in b:
        if isinstance(i, int): d += 1
    return d

def is_terminal(b):  # - Mengembalikan true jika kombinasi pemenang sudah tercapai
    w_c = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for c in w_c:
        if b[c[0]] == b[c[1]] and b[c[1]] == b[c[2]]:   return True

def evaluate(b):  # - Menetapkan nilai berdasarkan kesukaan pemain X
    w_c = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for c in w_c:
        if b[c[0]] == b[c[1]] and b[c[1]] == b[c[2]] and b[c[2]] == 'O':
            return [20 - depth(b), -1]
        elif b[c[0]] == b[c[1]] and b[c[1]] == b[c[2]] and b[c[2]] == 'X':
            return [-10 + depth(b), -1]
    return [10 - depth(b), -1]

def moves_boards(b, player='O'):  # Mengembalikan daftar yang memiliki pasangan tindakan yang diambil dan daftar yang dihasilkan dari mengambil gerakan tersebut misalnya: [ [1,['x',2,3,4,5,6,7,8,9,]], [1,[1,'x',3,4,5,6,7,8,9,]], ... ]
    available_values = [x for x in b if isinstance(x, int)]
    possible_boards = []
    output = []
    for i in available_values:
        c = deepcopy(b)
        c[i - 1] = player
        output.append([i, c])
    return output

def win(b, current_player):  # - mengembalikan true jika salah satu pemain menang, jika tidak mengembalikan false
    if (b[0] == current_player and b[1] == current_player and b[2] == current_player) or \
            (b[3] == current_player and b[4] == current_player and b[5] == current_player) or \
            (b[6] == current_player and b[7] == current_player and b[8] == current_player) or \
            (b[0] == current_player and b[3] == current_player and b[6] == current_player) or \
            (b[1] == current_player and b[4] == current_player and b[7] == current_player) or \
            (b[2] == current_player and b[5] == current_player and b[8] == current_player) or \
            (b[0] == current_player and b[4] == current_player and b[8] == current_player) or \
            (b[2] == current_player and b[4] == current_player and b[6] == current_player):
        return True
    else:
        return False


print("Selamat datang")
print("Pilihan akan di acak salah satu untuk memulai pertama...")
player = random.choice([1,2])
first = ['', 'AI', 'Kamu']
print("yang memulai pertama adalah:",first[player],'\n')

#1 = AI
#2 = player (kamu)
#print(player)

#if player == 1:


#else:


vboard = [1,2,3,4,5,6,7,8,9]
vboard1 = [" "," "," "," "," "," "," "," "," "]

for turn in range(len([a for a in vboard if isinstance(a, str)]) + 1, 10):

    if player == 1:
        if turn % 2 == 0:
            current_player = 'X'
            action_h()
        else:
            current_player = 'O'
            action_a()

    else:
        if turn % 2 == 0:
            current_player = 'O'
            action_a()
        else:
            current_player = "X"
            action_h()


    b_display()

    if win(vboard, current_player) == True:
        print('player ini {} telah memenangkan permainan '.format(current_player))
        print('Selamat Yaa....')
        break
    elif (depth(vboard) == 0):
        print("Hasilnya seri Mas Bro :(")
        break
    else:
        print(" ")