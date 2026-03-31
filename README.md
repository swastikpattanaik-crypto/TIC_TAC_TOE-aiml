# Tic-Tac-Toe with AI

A classic Tic-Tac-Toe game where you play against an AI opponent powered by the Minimax algorithm.

**Name:** Swastik Pattanaik
**Reg No:** [25BCE11281]
**Branch:** B.Tech – Computer Science and Engineering
**Year:** First Year (2025–2029)
**Institution:** VIT Bhopal University
**Course:** CSA2001-foundation in aiml

## Features

- Play against an AI opponent
- AI uses Minimax algorithm for optimal moves
- Score tracking across multiple games
- Simple command-line interface
- Option to continue playing or reset scores

## How to Play

### Game Rules
- Play on a 3x3 grid
- You play as **X**, AI plays as **O**
- Get 3 in a row to win (horizontal, vertical, or diagonal)
- Draw if all 9 cells are filled

### Controls
- Enter row and column numbers (1-3) to place your mark
- Type `quit` to stop the current game
- After each game:
  - `continue` - Play another game
  - `end` - Reset score and start fresh

## Installation

```bash
python tic_tac_toe.py
```

## Scoring System

- **Player wins**: +1 point
- **AI wins**: -1 point  
- **Draw**: No change

## Code Structure

```
tic_tac_toe.py
├── print_board()      # Displays the board
├── check_winner()     # Checks winning combinations
├── is_full()          # Checks if board is full
├── minimax()          # AI decision algorithm
├── ai_move()          # Makes AI move
└── Main game loop     # Handles game flow
```

## AI Algorithm

The AI uses the **Minimax algorithm**:
- AI maximizes its chance to win
- Player minimizes AI's chance
- Scores: AI win = +1, Player win = -1, Draw = 0

## Example Gameplay

```
New Game Started!

Current Board:
  |   |  
---------
  |   |  
---------
  |   |  

Enter row (1-3): 2
Enter col (1-3): 2

AI played at (1, 1)

Current Board:
O |   |  
---------
  | X |  
---------
  |   |  


## Troubleshooting

- **Invalid input**: Enter numbers 1-3 only
- **Move doesn't work**: Cell may already be taken
- **Game stops**: Check if you typed 'quit'

## License

Open source for personal use and learning.



**Enjoy the game!**
