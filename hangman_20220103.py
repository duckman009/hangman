def hangman(word):
    wrong = 0
    stages = ["",
              "______________          ",
              "|                       ",
              "|           |           ",
              "|           0           ",
              "|          /|\          ",
              "|          / \          ",
              "|                       "
             ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("ハングマンへようこそ")
    print("len(stages):"  + str(len(stages)))
    print("len(word):"  + str(len(word)))
    print(board)
    print(rletters)
    while wrong < len(stages) -1:
        print("\n")
        msg = "一文字を予想してね"
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
            print(board)
            print(rletters)
        else:
            wrong += 1
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("your win")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("your lose.正解は{}.".format(word))


hangman("cat")