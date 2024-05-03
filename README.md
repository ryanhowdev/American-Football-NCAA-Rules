# American-Football-NCAA-Rules

Here's a comprehensive README for the NCAA Football Game Simulation application. This document will outline the application's purpose, describe its architecture, and provide guidance on how to use it.

---

# NCAA Football Game Simulation

## Overview

The NCAA Football Game Simulation is a Python-based application designed to simulate various scenarios in an NCAA football game. This application models the essential components of a football game including game clock management, scoring, field positioning, and basic play execution. It is intended as a tool for understanding the dynamics of football games and for strategizing.

## Objectives

- **Simulate Game Dynamics**: Understand how different plays affect the game's outcome.
- **Teach Rules**: Help users learn NCAA football rules, particularly around clock management and scoring.
- **Strategize**: Allow users to test football strategies and see potential outcomes.

## Architecture

This application consists of several classes each responsible for handling different aspects of the football game:

### Classes

#### 1. **Clock**
   - **Purpose**: Manages the game clock, including counting down the game time and stopping/starting the clock based on game events.
   - **Methods**:
     - `update_status()`: Check and return the special timing rules based on the remaining time.
     - `start()`: Starts the game clock.
     - `stop()`: Stops the game clock.
     - `update(seconds_passed)`: Updates the game time by decreasing the remaining time.
     - `handle_event(event_type)`: Handles specific events that affect the clock (e.g., incomplete passes, scoring plays).

#### 2. **Scoreboard**
   - **Purpose**: Keeps track of the scoring between two teams.
   - **Methods**:
     - `update_score(team, points)`: Updates the score for a specified team.

#### 3. **Field**
   - **Purpose**: Manages the field positioning of the ball.
   - **Methods**:
     - `move_ball(yards)`: Updates the position of the ball on the field based on the yards gained or lost.

#### 4. **Player**
   - **Purpose**: Represents a player with unique identifiers and statistics.
   - **Methods**:
     - None specific beyond initialization.

#### 5. **Team**
   - **Purpose**: Represents a team, holding details like team name, roster, and timeouts.
   - **Methods**:
     - `add_player(player)`: Adds a player to the team's roster.

#### 6. **Event**
   - **Purpose**: Base class for game events.
   - **Methods**:
     - `trigger()`: A method to be overridden by subclasses to trigger specific events.

#### 7. **Play**
   - **Purpose**: Represents a football play.
   - **Methods**:
     - `trigger()`: Executes the play, affecting the game state such as the clock and the scoreboard.

#### 8. **Game**
   - **Purpose**: Manages the overall gameplay.
   - **Methods**:
     - `start_game()`: Initializes and starts the game.
     - `execute_play(play)`: Executes a given play.
     - `update_game_state()`: Updates the game state after a play.
     - `possession_change()`: Changes the possession of the ball to the opposite team.

## How to Use the Application

1. **Setup**: Ensure Python is installed on your system.
2. **Running the Application**:
   - Clone or download the application files to your local machine.
   - Open a terminal or command prompt.
   - Navigate to the directory containing the application.
   - Run the command `python <filename>.py` to start the simulation.
3. **Simulating a Game**:
   - The `main()` function in the script can be modified to simulate different game scenarios by creating different instances of `Play` and executing them through the `Game` instance.
   - Users can modify the `main()` function to simulate different plays, change the teams, or adjust the game settings.

## Conclusion

This application provides a basic framework for simulating an NCAA football game, with potential for expansion and further customization. Users can learn from and modify the simulation to better understand the complexities of football game management and strategy.