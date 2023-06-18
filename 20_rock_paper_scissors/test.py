from main import *

assert find_winner('rock', 'paper') == 'player two'
assert find_winner('rock', 'scissors') == 'player one'
assert find_winner('paper', 'scissors') == 'player two'
assert find_winner('paper', 'rock') == 'player one'
assert find_winner('scissors', 'rock') == 'player two'
assert find_winner('scissors', 'paper') == 'player one'
assert find_winner('rock', 'rock') == 'tie'
assert find_winner('paper', 'paper') == 'tie'
assert find_winner('scissors', 'scissors') == 'tie'