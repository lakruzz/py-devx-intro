# tests/test_rps_game.py
from unittest.mock import patch
import pytest
from src.rps_game import parse_arguments  # Assuming you have a function to parse arguments

def test_argparse_switches_valid():
    """
    Test that argparse switches are valid.
    """
    # Mock the argparse.parse_args() call to return valid arguments
    with patch('argparse.ArgumentParser().parse_args') as mock_parse_args:
        mock_parse_args.return_value = {'hand': 'paper'}
        result = parse_arguments()  # Assuming parse_arguments() is your function to parse args
        
        assert result['hand'] == 'paper', "Expected 'hand' to be 'paper'"
        mock_parse_args.assert_called_once_with()

@pytest.mark.parametrize(
    "input_string,expected",
    [
        ("--hand scissors", {"hand": "scissors"}),
        ("--hand rock", {"hand": "rock"}),
        ("--hand paper", {"hand": "paper"})
    ],
    ids=["scissors", "rock", "paper"]
)
def test_argparse_switches_valid_examples(input_string, expected):
    """
    Test that argparse switches are valid with various examples.
    """
    # Mock the argparse.parse_args() call to return the expected arguments
    with patch('argparse.ArgumentParser().parse_args') as mock_parse_args:
        mock_parse_args.return_value = expected
        result = parse_arguments()  # Assuming parse_arguments() is your function to parse args
        
        assert result == expected, f"Expected {result} to match {expected}"
        mock_parse_args.assert_called_once_with()

def test_argparse_switches_invalid():
    """
    Test that argparse raises an error for invalid switches.
    """
    # Attempt to parse an invalid switch
    with pytest.raises(SystemExit):  # SystemExit is raised when argparse encounters an error
        parse_arguments(['--invalid_switch'])  # Assuming parse_arguments() is your function to parse args