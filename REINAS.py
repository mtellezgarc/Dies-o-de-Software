# Este metodo se llama hasta contar el numero de veces las posibilidades de las reinas
def backtrack(Q,r):
    if r==len(Q):
        print_chess_board(Q)
    else :
        for j in range(len(Q)):
            legal = True
            for i in range(r):
                if((Q[i]==j)or(Q[i]==j+r-i)or(Q[i]==j-r+i)):
                    legal = False               
            if legal :
                Q[r]=j
                backtrack(Q,r+1)

#pintar la reina y colocarla en la posicion del metodo bactraking
def print_chess_board(d):
     chess_board=''
     for g in range((len(d)*3+6)):
         chess_board +="+"        
     chess_board += "\n"
     for i in range(len(d)):
         chess_board += "+  "
         for j in range(len(d)):
             if j==d[i]:
                 chess_board += " Q "
             else:
                 chess_board += " - "
         chess_board += "  +\n"
     for g in range((len(d)*3+6)):
         chess_board +="+"        
     chess_board += "\n"
     print(chess_board)

#tamaño de tablero, crea el tablero          
def create_chess_board(size):
    mat =[]
    for i in range(size):
        mat.append(0)
    return mat


print("Proyecto reinas")
numero =input("Número de reinas : ")
print("Que representa la Reina")
print("-Indica que no hay reina en la posición")
backtrack(create_chess_board(int(numero)),0)
