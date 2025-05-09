import unittest
from unittest.mock import MagicMock
from rpg.door import Door


class TestDoor(unittest.TestCase):
    def test_inspect(self):
        """Test inspect method"""
        mock_room = MagicMock()
        mock_room.description = "a dark hallway"
        door = Door("wooden door", mock_room)
        with unittest.mock.patch("builtins.print") as mocked_print:
            door.inspect()
            mocked_print.assert_called_with(
                "There is a wooden door leading to a dark hallway."
            )

    def test_interact(self):
        """Test interact method for the door"""
        mock_room = MagicMock()
        mock_player = MagicMock()
        mock_player.room = "some room"
        door = Door("wooden door", mock_room)
        door.interact(mock_player)
        self.assertEqual(mock_player.room, mock_room)


if __name__ == "__main__":
    unittest.main()
