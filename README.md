# GenAISlidingPuzzle

## 🚀 How to Play:

1. Start the game:
  bash
   cd /Users/vijayasrichinta/puzzle_game
   python run_game.py
   

2. The game will:
   • Start a local server on port 5000
   • Automatically open your browser
   • Show the puzzle interface

3. Game Controls:
   • Click tiles next to the empty space to move them
   • Use "New Game" to start fresh
   • Change difficulty with the dropdown menu
   • Try to solve in as few moves as possible!

## 🛠️ Technical Architecture:

Backend (Python/Flask):
• SlidingPuzzle class handles all game logic
• RESTful API for frontend communication
• Smart shuffling algorithm
• Move validation and win detection

Frontend (HTML/CSS/JavaScript):
• Modern, responsive design
• Smooth animations and effects
• Real-time communication with backend
• Mobile-friendly interface

## 📁 Project Structure:
puzzle_game/
├── app.py           # Main Flask application
├── run_game.py      # Easy startup script
├── requirements.txt # Dependencies
├── README.md        # Documentation
└── templates/
    └── index.html   # Game interface
