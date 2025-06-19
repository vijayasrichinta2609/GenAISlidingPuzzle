#!/usr/bin/env python3
"""
Simple script to run the Sliding Puzzle Game
"""
import webbrowser
import time
import threading
from app import app, puzzle

def open_browser():
    """Open the browser after a short delay"""
    time.sleep(1.5)
    webbrowser.open('http://localhost:5000')

if __name__ == '__main__':
    print("🧩 Starting Sliding Puzzle Game...")
    print("🌐 Game will be available at: http://localhost:5000")
    print("🎮 Opening browser automatically...")
    print("⏹️  Press Ctrl+C to stop the game")
    
    # Start browser in a separate thread
    browser_thread = threading.Thread(target=open_browser)
    browser_thread.daemon = True
    browser_thread.start()
    
    # Start the Flask app
    try:
        app.run(debug=False, port=5000, host='127.0.0.1')
    except KeyboardInterrupt:
        print("\n👋 Thanks for playing! Game stopped.")
