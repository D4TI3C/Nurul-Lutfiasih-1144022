import sys
print("Langkah Benar 1-7-2-4-3-7-1\n")
print (" 1.Kambing Menyeberang\n 2.Serigala Menyeberang\n 3.Sayuran Menyeberang\n 4.Kambing Kembali\n 5.Serigala Kembali\n 6.Sayur Kembali\n 7.Perahu Kembali")
def game():
    a = raw_input("1th Step : ")
    if a == '1'    : b = raw_input("2nd Step : ")
    else           : print('Game Over')
    if b == '7'    : c = raw_input("3rd Step : ")
    else           : print('Game Over')
    if c == '2'    : d = raw_input("4th Step : ")
    else           : print('Game Over')
    if d == '4'    : e = raw_input("5th Step : ")
    else           : print('Game Over')
    if e == '3'    : f = raw_input("6th Step : ")
    else           : print('Game Over')
    if f == '7'    : g = raw_input("7th Step : ")
    else           : print('Game Over')
    if g == '1'    : h = raw_input("Well Done")
game()
