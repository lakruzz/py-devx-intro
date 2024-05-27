# tests/test_rps_game.py
import pytest
from unittest.mock import patch
from src.rps_game import parse_arguments  # Ensure this import is correct

@patch('argparse.ArgumentParser')
def test_argparse_switches_valid(mock_argparse):
    """
    Test that argparse switches are valid.
    """
    # Setup the mock to return a specific value when parse_args is called
    mock_instance = mock_argparse.return_value
    mock_instance.parse_args.return_value = {'hand': 'paper'}
    
    # Call your function
    result = parse_arguments()
    
    # Assertions
    assert result['hand'] == 'paper', "Expected 'hand' to be 'paper'"
    mock_instance.parse_args.assert_called_once_with()

@pytest.mark.parametrize(
    "input_string,expected",
    [
        ("--hand scissors", {"hand": "scissors"}),
        ("--hand rock", {"hand": "rock"}),
        ("--hand paper", {"hand": "paper"})
    ],
    ids=["scissors", "rock", "paper"]
)
@patch('argparse.ArgumentParser')
def test_argparse_switches_valid_examples(mock_argparse, input_string, expected):
    """
    Test that argparse switches are valid with various examples.
    """
    # Setup the mock to return the expected arguments
    mock_instance = mock_argparse.return_value
    mock_instance.parse_args.return_value = expected
    
    # Call your function
    result = parse_arguments()
    
    # Assertions
    assert result == expected, f"Expected {result} to match {expected}"
    mock_instance.parse_args.assert_called_once_with()

@patch('argparse.ArgumentParser')
def test_argparse_switches_invalid(mock_argparse):
    """
    Test that argparse raises an error for invalid switches.
    """
    # Setup the mock to simulate an error when parse_args is called
    mock_instance = mock_argparse.return_value
    mock_instance.parse_args.side_effect = SystemExit(2)  # Simulate an error
    
    # Attempt to parse an invalid switch
    with pytest.raises(SystemExit):
        parse_arguments()