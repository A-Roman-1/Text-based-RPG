import os
import json
from typing import Any, Dict, Optional


class Saver:
    """Handles game saving and loading operations."""
    SAVE_DIR: str = "savedgames"
    SAVE_FILE: str = os.path.join(SAVE_DIR, "quicksave.json")

    @staticmethod
    def ensure_save_directory() -> None:
        """Ensure the save directory exists, creating it if necessary."""
        if not os.path.isdir(Saver.SAVE_DIR):
            os.makedirs(Saver.SAVE_DIR)

    @staticmethod
    def quick_save(game_data: Dict[str, Any]) -> None:
        """Save the game data to a file."""
        try:
            Saver.ensure_save_directory()
            with open(Saver.SAVE_FILE, "w") as save_file:
                json.dump(game_data, save_file)
            print("Game saved successfully.")
        except Exception as e:
            print(f"Failed to save the game: {e}")

    @staticmethod
    def quick_load() -> Optional[Dict[str, Any]]:
        """Load the game data from the save file, if available."""
        try:
            if os.path.exists(Saver.SAVE_FILE):
                with open(Saver.SAVE_FILE, "r") as save_file:
                    return json.load(save_file)
            else:
                print("No save file found.")
        except Exception as e:
            print(f"Failed to load the game: {e}")
        return None


class Scanner:
    """Utility class for reading and validating user input."""
    class InputError(Exception):
        """Exception raised for invalid input."""
        pass

    def read_int(self, inp: str, possible_answers: int) -> int:
        """Read and validate an integer input from the user."""
        try:
            value: int = int(inp)
            if value < 0 and value != -1:
                raise self.InputError(
                    "No negative integers allowed! (Except -1 to quit)"
                )
            elif value not in range(0, possible_answers) and value != -1:
                raise self.InputError("Please input a valid integer")
        except ValueError:
            raise self.InputError("Please input a valid integer!")
        return value
