
# Rock, Paper, Scissors

def find_winner(move1, move2):
    rock = "rock"
    scissors = "scissors"
    paper = "paper"
    if move1 == rock and move2 == scissors:
        return "player one"
    elif move1 == rock and move2 == paper:
        return "player two"
    elif move1 == paper and move2 == scissors:
        return "player two"
    elif move1 == paper and move2 == rock:
        return "player one"
    elif move1 == scissors and move2 == rock:
        return "player two"
    elif move1 == scissors and move2 == paper:
        return "player one"
    elif move1 == move2:
        return "tie"

def main():
    return True

if __name__ == "__main__":
    main()

