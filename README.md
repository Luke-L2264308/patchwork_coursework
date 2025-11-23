**Project Title and Description**
- **Title:** Patchworks — Interactive Patchwork Designer
- **Description:** A small interactive Python program that opens a graphical window where the user can create, modify, and move decorative patchwork tiles. The script prompts for a canvas size and three colours, then launches an interactive GUI where patches can be selected with the mouse and modified using keyboard controls.

**Installation and Setup Instructions**
- **Prerequisites:**
  - Python 3.8+ (3.11 recommended). Tested on Windows with PowerShell.
  - No external pip packages are required; the project uses a local `graphix` module (included in the repo).
- **Clone the repository:**
  - `git clone https://github.com/Luke-L2264308/patchwork_coursework.git`
  - `cd patchwork_coursework`
- **Run the project:**
  - From the project folder, run:
    - `python "coursework1 complete.py"`
  - The program will prompt for a canvas size and three colours, then open the interactive window.

**Usage Instructions**
- **Startup prompts:**
  - Choose a size from `5`, `7`, or `9` when prompted. The size controls the window grid (each patch is 100×100 pixels).
  - Enter three distinct colours from the allowed list: `red`, `green`, `blue`, `magenta`, `orange`, `purple`.
- **Main interaction:**
  - Click a patch in the window to select it. A highlighted selection square will appear.
  - Keyboard controls when a patch is selected:
    - `x` : Clear the selected patch (removes its contents).
    - `1`, `2`, `3` : Fill the selected patch with a patterned (triangular) design using one of the chosen colours.
    - `4`, `5`, `6` : Fill the selected patch with a line-based pattern.
    - `7`, `8`, `9` : Fill the selected patch with a plain filled square.
    - Arrow keys (`Up`, `Down`, `Left`, `Right`) : Move the selected patch into an adjacent empty patch (if available).
    - `Escape` : Deselect the currently selected patch.
  - Colour mapping: the numeric keys map to the three chosen colours in a cyclic manner; 

**Configuration and Options**
- Acceptable canvas sizes: `5`, `7`, `9`.
- Acceptable colours: `red`, `green`, `blue`, `magenta`, `orange`, `purple`.
- No additional config files are required.

**Project Structure and Technologies Used**
- `coursework1 complete.py`: Main program — handles user input, pattern generation, window creation, and user interactions.
- `graphix.py`: The graphics module used for this program (to be clear, this aspect of the program was not made by me but it seemed easier to include it for ease of testing in this upload)
- Language: Python 3
- Development tools: any text editor or IDE, Python interpreter, and PowerShell (on Windows) for running the program.

**How to Run Tests**
- There are no automated tests included. Manual testing can be performed by running the program and exercising the UI controls described above.



