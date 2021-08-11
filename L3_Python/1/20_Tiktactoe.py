# this will give us a board with 9 blank spaces
board = [" " for i in range(9)]

def printing():
    row1 = "| {} | {} | {} |".format(board[0], board[1], board[2])
    row2 = "| {} | {} | {} |".format(board[3], board[4], board[5])
    row3 = "| {} | {} | {} |".format(board[6], board[7], board[8])

    print ("*" *22)
    print(row1)
    print(row2)
    print(row3)
    print ("*" *22)

def player_move(icon):
    print("your turn player {}".format(icon))
    choice =  input("Enter your move 1-9 :").strip()
    if board[ int(choice) - 1 ] == " ":
     board[ int(choice) - 1 ] = "{}".format(icon)

    else:
     print("REENTER!! that space is taken \n \n \n")
    

while True:  
     printing()
     player_move("X")
     printing()
     player_move("O")
     printing()