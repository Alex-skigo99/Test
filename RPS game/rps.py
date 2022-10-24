from getpass import getpass
def your_move(text):
  m = getpass(text)
  while not (m == 'r' or m =='p' or m =='s'):
    print('Wrong move')
    m = getpass(text)
  return m
n_game = 1
is_game = True
while is_game:
  print(f"Game - {n_game}")
  print('Your move - r, p, s')
  m1 = your_move('Player 1 -')
  m2 = your_move('Player 2 -')
  m1_2 = m1 + m2
  if m1 == m2:
    print(f"Player1 and Player2 choose {m1} it's drow")
  if m1_2 == 'rp' or m1_2 == 'ps' or m1_2 == 'sr':
      print(f"Player1 - {m1} Player2 - {m2} Win Player2")
  if m1_2 == 'rs' or m1_2 == 'sp' or m1_2 == 'pr':
      print(f"Player1 - {m1} Player2 - {m2} Win Player1")
  if input('Next? (y,n)') == 'n': 
    is_game = False
  n_game = n_game + 1