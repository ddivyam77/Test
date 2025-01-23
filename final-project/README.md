# Rock, Paper, Scissors Game with Statistics

This project is a command-line Rock, Paper, Scissors game implemented in Python. Players can challenge the computer in the classic game, and the program will keep track of wins, losses, and ties for the session. In addition, unit tests have been provided using `pytest` to ensure that each function behaves as expected.

## Table of Contents
- [Features](#features)
- [How It Works](#how-it-works)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running the Game](#running-the-game)
- [Testing](#testing)
  - [Running Tests](#running-tests)
- [Game Functions](#game-functions)
- [Sample Gameplay](#sample-gameplay)
- [Future Enhancements](#future-enhancements)
- [License](#license)

## Features

- **Interactive Gameplay**: Players choose `rock`, `paper`, or `scissors` to compete against a random computer selection.
- **Game Statistics**: At the end of each session, a summary of wins, losses, and ties is displayed.
- **Error Handling**: Prompts users until they enter a valid choice.
- **Automated Testing**: Tests for each primary function to validate functionality.

## How It Works

The game operates in a continuous loop, where the player can repeatedly select between `rock`, `paper`, or `scissors`. The computer then randomly selects one of the three options, and the result is evaluated as either a win, loss, or tie based on traditional Rock, Paper, Scissors rules:

- **Rock beats Scissors**
- **Scissors beat Paper**
- **Paper beats Rock**

The player can choose to quit at any time, upon which the game will exit the loop and display a summary of the player’s statistics for that session.

## Project Structure

The project consists of the following files:

- **`project.py`**: Contains the main game logic, including the game loop, user input handling, computer choice generation, and winner determination.
- **`test_project.py`**: Contains unit tests written in `pytest` to validate that each function performs as expected.

## Getting Started

### Prerequisites

- **Python 3.x**: Ensure you have Python 3.x installed on your machine. Check your Python version by running:
  ```bash
  python --version
