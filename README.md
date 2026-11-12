# Flappy Bird in Python

A classic implementation of the Flappy Bird game built using Python and the Pygame library.


<img width="752" height="977" alt="Screenshot 2026-11-07 001250" src="https://github.com/user-attachments/assets/5bb5a239-43fb-4693-8b0b-2a9da1af4549" />


## Overview

This project recreates the core mechanics of the popular arcade game. Players control a bird navigating through a series of obstacles while managing gravity, velocity, and collision detection.

## Features

- Physics-based movement including gravity and jump velocity.
- Real-time score tracking and display.
- Interactive start and restart screens.
- Pixel-art aesthetic matching the original style.

## Prerequisites

Ensure you have Python 3.x installed on your system. The game depends on the Pygame library for rendering, audio, and input handling.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/flappy-bird-python.git
   cd flappy-bird-python
   ```

2. (Optional) Create and activate a virtual environment:
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. Install the required dependencies:
   ```bash
   pip install pygame
   ```

## Running the Game

Execute the main script from the root directory:
```bash
python main.py
```
*(Note: Replace `main.py` with your entry point file name if it differs).*

## Controls

| Action | Input |
| :--- | :--- |
| Jump / Flap | Spacebar / Up Arrow / Left Click |
| Restart | Spacebar (on game over screen) |
| Quit | Escape key / Close window |

## Project Structure

```text
flappy-bird-python/
│
├── assets/
│    ├── images/
│             └── score/
│
├── Game.py
├── bird.py
├── highscore.txt
├── score.py
└── README.md
```

## Contributing

Contributions, bug reports, and feature requests are welcome. Feel free to open an issue or submit a pull request.

