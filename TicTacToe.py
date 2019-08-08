#test_board = ['#', 'X','X','X','O','O','O','X','X','X']

def display_board(board):
    print(' ' + board[1] + '|' + board[2] + '|' + board[3])
    print('-------')
    print(' ' + board[4] + '|' + board[5] + '|' + board[6])
    print('-------')
    print(' ' + board[7] + '|' + board[8] + '|' + board[9])

def reference_board():
    print(' 1' + '|' + '2' + '|' + '3' )
    print('-------')
    print(' 4' + '|' + '5' + '|' + '6' )
    print('-------')
    print(' 7' + '|' + '8' + '|' + '9\n\n' )

def introduction():
    print('\n\n\nWELCOME TO TiC TAC TOE. ENTER AT YOUR OWN RISK. MAY THE BEST PLAYER WiN AND EARN ETERNAL GLORY. MAY THE LOSER BRING GREAT SHAME UPON HiS/HER FAMILY....\n')
    print('Player one, enter your name: ')
    introduction.name1 = input()
    print('Player two, enter your name: ')
    introduction.name2 = input()
    print(f"{introduction.name1}, would you like to be X or O")
    selection = input()
    while selection != 'X' and selection != 'O':
        print("Boy! enter X or O (oh not zero) ") 
        selection = input()
    print('\n' * 100)
    if selection == 'X':
        introduction.letter1 = 'X'
        introduction.letter2 = 'O'
        print(f"\nOkay {introduction.name1}, you are X's, and {introduction.name2} you are O's")
    elif selection == 'O':
        introduction.letter1 = 'O'
        introduction.letter2 = 'X'
        print(f"Okay {introduction.name1}, you are O's, and {introduction.name2} you are X's.\nAre you ready for the ride of your lives? Lets play tic tac succ on my toes\n")
    print("Use this as reference to how the board is set up: \n")
    reference_board()
    return 


def game(board):
    gameWon = False
    counter = 0

    while counter < 9 and not (gameWon):
        print(f'{introduction.name1}, enter where you would like you place your {introduction.letter1} (1-9):' )
        selection1 = input()
        digit1 = selection1.isdigit()
        while not digit1:
            print("Boy! Enter a number between 1 and 9 ")
            selection1 = input()
            digit1 = selection1.isdigit()
        selection1 = int(selection1)
        while selection1 > 9 or selection1 < 1 or selection1 == '':
            print("Boy! enter a number between 1 and 9 ") 
            selection1 = int(input())
        while board[selection1] != ' ': 
            print("Cant write over the other boi. try again")
            selection1 = int(input())
        print('\n' * 100)
        board[selection1] = introduction.letter1
        reference_board()
        print('\n'* 2)
        display_board(board)
        counter += 1

        if ((board[1] == introduction.letter1 and board[2] == introduction.letter1 and board[3] == introduction.letter1) or (board[4] == introduction.letter1 and board[5] == introduction.letter1 and board[6] == introduction.letter1) or (board[7] == introduction.letter1 and board[8] == introduction.letter1 and board[9] == introduction.letter1) or (board[1] == introduction.letter1 and board[4] == introduction.letter1 and board[7] == introduction.letter1) or (board[2] == introduction.letter1 and board[5] == introduction.letter1 and board[8] == introduction.letter1) or (board[3] == introduction.letter1 and board[6] == introduction.letter1 and board[9] == introduction.letter1) or (board[1] == introduction.letter1 and board[5] == introduction.letter1 and board[9] == introduction.letter1) or (board[3] == introduction.letter1 and board[5] == introduction.letter1 and board[7] == introduction.letter1)):
            print('\n' * 100)
            print(f'Congratulations {introduction.name1} you have won. Go rejoice in the streets. {introduction.name2} you are a loser and have brought shame upon your family.')
            gameWon = True
            break
        elif counter == 9:
            print("Tie! How boring >:{")
            break

        
        print(f'{introduction.name2}, enter where you would like you place your {introduction.letter2} (1-9):' )
        selection2 = input()
        digit2 = selection2.isdigit()
        while not digit2:
            print("Boy! Enter a number between 1 and 9 ")
            selection2 = input()
            digit2 = selection2.isdigit()
        selection2 = int(selection2)
        while selection2 > 9 or selection2 < 1 or selection2 == '':
            print("Boy! enter a number between 1 and 9 ") 
            selection2 = int(input())
        while board[selection2] != ' ': 
            print("Cant write over the other boi. try again")
            selection2 = int(input())
        print('\n' * 100)
        board[selection2] = introduction.letter2
        reference_board()
        print('\n'* 2)
        display_board(board)
        counter += 1

        if ((board[1] == introduction.letter2 and board[2] == introduction.letter2 and board[3] == introduction.letter2) or (board[4] == introduction.letter2 and board[5] == introduction.letter2 and board[6] == introduction.letter2) or (board[7] == introduction.letter2 and board[8] == introduction.letter2 and board[9] == introduction.letter2) or (board[1] == introduction.letter2 and board[4] == introduction.letter2 and board[7] == introduction.letter2) or (board[2] == introduction.letter2 and board[5] == introduction.letter2 and board[8] == introduction.letter2) or (board[3] == introduction.letter2 and board[6] == introduction.letter2 and board[9] == introduction.letter2) or (board[1] == introduction.letter2 and board[5] == introduction.letter2 and board[9] == introduction.letter2) or (board[3] == introduction.letter2 and board[5] == introduction.letter2 and board[7] == introduction.letter2)):
            print('\n' * 100)
            print(f'CONGRATULATiONS {introduction.name2} YOU HAVE WON. GO REJOiCE iN THE STREETS. {introduction.name1} YOU ARE A LOSER AND HAVE BROUGHT GREAT SHAME UPON YOUR FAMILY.')
            gameWon = True
            break
    
    return 


def main():
    print('\n'* 100)
    introduction()
    board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    game(board)
    print('\n' * 30)

if __name__ == '__main__':
    main()





