import unittest
from unittest.mock import patch, mock_open
from rpg.io_utils import Saver, Scanner


class TestSaver(unittest.TestCase):
    @patch("os.makedirs")
    @patch("os.path.isdir", return_value=False)
    def test_ensure_save_directory(self, mock_makedirs):
        """Test that the save directory is created if it doesn't exist"""
        Saver.ensure_save_directory()
        mock_makedirs.assert_called_once_with(Saver.SAVE_DIR)

    @patch("builtins.open", new_callable=mock_open)
    @patch("json.dump")
    @patch("os.makedirs")
    @patch("os.path.isdir", return_value=True)
    def test_quick_save(
        self, mock_isdir, mock_makedirs, mock_json_dump, mock_open_file
    ):
        """Test that quick_save writes data to a file"""
        game_data = {"player": "test_player"}
        Saver.quick_save(game_data)
        mock_open_file.assert_called_once_with(Saver.SAVE_FILE, "w")
        mock_json_dump.assert_called_once_with(game_data, mock_open_file())

    @patch("os.path.exists", return_value=True)
    @patch(
        "builtins.open", new_callable=mock_open,
        read_data='{"player": "test_player"}'
    )
    def test_quick_load(self, mock_open_file, mock_exists):
        """Test that quick_load loads data from a file"""
        data = Saver.quick_load()
        self.assertEqual(data, {"player": "test_player"})
        mock_open_file.assert_called_once_with(Saver.SAVE_FILE, "r")

    @patch("os.path.exists", return_value=False)
    def test_quick_load_no_file(self, mock_exists):
        """Test that quick_load returns None when no save file is found"""
        data = Saver.quick_load()
        self.assertIsNone(data)


class TestScanner(unittest.TestCase):
    def test_read_int_valid(self):
        """Test that read_int returns the correct integer within valid range"""
        scanner = Scanner()
        self.assertEqual(scanner.read_int("2", 5), 2)

    def test_read_int_negative(self):
        """Test that read_int raises InputError for invalid
        negative integers"""
        scanner = Scanner()
        with self.assertRaises(Scanner.InputError):
            scanner.read_int("-5", 5)

    def test_read_int_invalid_input(self):
        """Test that read_int raises InputError for non-integer inputs"""
        scanner = Scanner()
        with self.assertRaises(Scanner.InputError):
            scanner.read_int("abc", 5)

    def test_read_int_out_of_range(self):
        """Test that read_int raises InputError for out-of-range integers"""
        scanner = Scanner()
        with self.assertRaises(Scanner.InputError):
            scanner.read_int("6", 5)


if __name__ == "__main__":
    unittest.main()
