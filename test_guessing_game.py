import unittest
from unittest.mock import patch
from refine_ref import play_game, get_attempts_left  # Replace 'your_module' with the actual filename.

class TestGuessingGame(unittest.TestCase):

  def test_get_attempts_left(self):
    self.assertEqual(get_attempts_left(10, 3), 7)
    self.assertEqual(get_attempts_left(5, 0), 5)

  @patch('builtins.input', side_effect=['e', '50', '75', '100', '85'])
  @patch('builtins.print')
  @patch('random.randint', return_value=85)
  def test_game_win(self, mock_randint, mock_print, mock_input):
    play_game()
    mock_print.assert_any_call("You got it! The answer was 85.")

  @patch('builtins.input', side_effect=['h', '50', '75', '100', '85', '90'])
  @patch('builtins.print')
  @patch('random.randint', return_value=70)
  def test_game_lose(self, mock_randint, mock_print, mock_input):
    play_game()
    mock_print.assert_any_call("You've run out of guesses. You lose.")

if __name__ == '__main__':
  unittest.main()