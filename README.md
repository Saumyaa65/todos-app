# Simple To-Do List Application (CLI & GUI)

This project provides a basic yet functional **To-Do List application** implemented in Python. It offers two distinct interfaces for user interaction: a **command-line interface (CLI)** for quick terminal-based management and a **Graphical User Interface (GUI)** for a more visual and interactive experience. All tasks are persistently stored in a plain text file.

## Overview

The application allows users to manage their daily tasks efficiently. Whether you prefer typing commands in a terminal or clicking buttons in a window, this To-Do app ensures your tasks are saved and accessible across sessions. It's a great example of modular Python programming and building simple user interfaces.

## Features

* **Add Tasks:** Easily add new to-do items to your list.
* **View Tasks:** Display all current to-do items with their corresponding numbers.
* **Edit Tasks:** Modify existing to-do items by their number.
* **Complete/Delete Tasks:** Mark tasks as complete by removing them from the list.
* **Persistent Storage:** All to-do items are saved to a `todos.txt` file, ensuring your list is preserved even after closing the application.
* **Command-Line Interface (CLI):** Interact with the app directly from your terminal.
* **Graphical User Interface (GUI):** A user-friendly window-based interface for visual task management, powered by `PySimpleGUI`.
* **Real-time Clock:** Both interfaces display the current date and time.

## Technologies Used

* Python
* `PySimpleGUI` (for the GUI version)
* Standard Python modules (`time`, `os`)

## How It Works

The project is structured into three main Python files to ensure modularity and separation of concerns:

1.  **`functions.py`:**
    * This module contains the core logic for reading from and writing to the `todos.txt` file.
    * `open_read()`: Reads all to-do items from `todos.txt`.
    * `open_write()`: Writes a list of to-do items back to `todos.txt`.

2.  **`todos.py` (Command-Line Interface):**
    * This script provides the terminal-based interaction.
    * It imports functions from `functions.py`.
    * It continuously prompts the user for actions (add, show, edit, complete, exit).
    * Based on user input, it calls the appropriate functions to modify the `todos.txt` file and displays the updated list.

3.  **`gui.py` (Graphical User Interface):**
    * This script creates the interactive window application using `PySimpleGUI`.
    * It imports functions from `functions.py`.
    * It initializes the `todos.txt` file if it doesn't exist.
    * It defines the layout of the GUI window, including text labels, input box, buttons (Add, Edit, Complete, Exit), and a listbox to display tasks.
    * It handles events triggered by button clicks or listbox selections, updating the `todos.txt` file and the GUI elements accordingly.
    * It includes basic error handling for common user mistakes (e.g., trying to edit/complete without selecting an item).

## File Structure
├── todos-app/
│   ├── functions.py
│   ├── todos.py
│   ├── gui.py
│   ├── todos.txt  (automatically created/used by the app)
│   └── Images/
│       ├── add.png
│       ├── edit.png
│       ├── complete.png
│       └── exit.png

**Note:** For the GUI (`gui.py`) to display correctly, the `Images/` directory containing `add.png`, `edit.png`, `complete.png`, and `exit.png` must be present in the same directory as `gui.py`.
