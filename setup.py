import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="TicTacToe",
    version="0.1",
    description="A simple Tic-Tac-Toe game",
    executables=[Executable("tic_tac_toe.py", base=base)]
)
