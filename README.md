# Cellular Genesis

## A Grid-Based Cellular Life Simulation

![Game Screenshot](https://via.placeholder.com/600x300/444444/FFFFFF?text=Cellular+Genesis+Screenshot)

*Placeholder: Replace the above link with a link to an actual screenshot of your game.*

**Cellular Genesis** is a simple yet captivating simulation of cellular life on a 2D grid. Inspired by the principles of cellular automata, it allows you to witness the birth, growth, and death of cell populations, guided by simple rules of life and competition.

## Core Concepts

### Cellular Automata
The game utilizes a grid system where each cell interacts with its neighbors to determine its next state. These interactions are governed by straightforward yet surprisingly dynamic rules.

### The Rules of Life

-   **Loneliness:** If a cell has fewer than two live neighbors, it dies from loneliness.
-   **Survival:** If a cell has two or three live neighbors, it survives.
-   **Overcrowding:** If a cell has more than three live neighbors, it dies due to overcrowding.
-   **Reproduction:** If an empty space has exactly three live neighbors, a new cell is born.

## How to Play

### Getting Started
1.  **Download:** Clone or download the project files.
2.  **Install Pygame:** Ensure you have Pygame installed:
   ```bash
    pip install pygame
   ```
3.  **Run the Game:** Execute the Python file (e.g., `grid_cellular_genesis.py`):
   ```bash
    python grid_cellular_genesis.py
   ```

### Gameplay Controls

-   **Mouse Click:** Click on the grid to add or remove cells.
-   **Spacebar:** Pause or resume the simulation.
-  **R Key:** Reset the grid to blank.

### Game Objectives

-   **Experiment:** Explore the dynamic patterns created by the simple rules of cell interaction.
-   **Observe:** Witness how initial cell populations evolve and adapt over time.
-   **Create:** Build intricate cellular structures and patterns by strategically placing the initial cells.

## Features

*   **Grid-Based Simulation:** Cells live and interact on a structured grid.
*   **Customizable Start:** The game starts with a blank grid, ready for your input.
*   **Pause/Play:** Freeze the simulation to observe patterns or to manually adjust the cell arrangement.
*   **Toggle Cells**: Simple click and toggle cells onto and off of the grid.
*   **Reset Grid**: Simple press of the 'R' key to clear the grid and start again.
*   **Simple and Intuitive Controls:**  Easy to pick up and play.

## Future Enhancements

-   **Multiple Cell Types:** Different cell types with unique survival rules and interactions.
-   **Mutations:** Introduce mutations that alter cell characteristics.
-   **Advanced UI:** A more sophisticated user interface with settings and data visualization.
-   **Save/Load:** Save and load custom cell arrangements and patterns.

## Contribute

Contributions are welcome! If you have suggestions or enhancements, feel free to submit pull requests or open issues on the project's repository.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgements

This project is inspired by the concept of cellular automata and Conway's Game of Life.

---

**Created by Devlop Rishi**
