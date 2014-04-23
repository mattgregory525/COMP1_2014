# Skeleton Program code for the AQA COMP1 Summer 2014 examination
# this code should be used in conjunction with the Preliminary Material
# written by the AQA Programmer Team
# developed in the Python 3.2 programming environment
# version 2 edited 06/03/2014

import random

NO_OF_RECENT_SCORES = 3

class TCard():
  def __init__(self):
    self.Suit = 0
    self.Rank = 0

class TRecentScore():
  def __init__(self):
    self.Name = ''
    self.Score = 0

Deck = [None]
RecentScores = [None]
Choice = ''

def GetRank(RankNo,AceHigh):
  
  Rank = ''
  if RankNo == 1 and AceHigh == False:
    Rank = "Ace"
  elif RankNo == 1 and AceHigh == True:
    RankNo == 14
    Rank = "Ace"
  elif RankNo == 2:
    Rank = 'Two'
  elif RankNo == 3:
    Rank = 'Three'
  elif RankNo == 4:
    Rank = 'Four'
  elif RankNo == 5:
    Rank = 'Five'
  elif RankNo == 6:
    Rank = 'Six'
  elif RankNo == 7:
    Rank = 'Seven'
  elif RankNo == 8:
    Rank = 'Eight'
  elif RankNo == 9:
    Rank = 'Nine'
  elif RankNo == 10:
    Rank = 'Ten'
  elif RankNo == 11:
    Rank = 'Jack'
  elif RankNo == 12:
    Rank = 'Queen'
  elif RankNo == 13:
    Rank = 'King'
  return Rank
 
    

def DisplayOptions():
  print("Option menu")
  print("")
  print("1. Set Ace to be high/low")
  print("")
  GetOptionChoice()
  
  
def GetOptionChoice():
  Option = int(input(("Please enter your option: ")))
  if Option == 1:
    SetOptionsHighOrLow()
  else:
    print("error")
  
def SetOptionsHighOrLow():
  Value = input("Set Ace (h)igh or (l)ow: ")
  high = ["H","h","High","high"]
  low = ["L","l","Low","low"]
  done = False
  while done == False:
    if Value in high:
      AceHigh = True
      done = True
    
    elif Value in low:
      AceHigh = False
      done = True
    
    else:
      print("Error")
  return AceHigh


def GetSuit(SuitNo):
  Suit = ''
  if SuitNo == 1:
    Suit = 'Clubs'
  elif SuitNo == 2:
    Suit = 'Diamonds'
  elif SuitNo == 3:
    Suit = 'Hearts'
  elif SuitNo == 4:
    Suit = 'Spades'
  return Suit

def DisplayMenu():
  print()
  print('MAIN MENU')
  print()
  print('1. Play game (with shuffle)')
  print('2. Play game (without shuffle)')
  print('3. Display recent scores')
  print('4. Reset recent scores')
  print("5. Options")
  print()
  print('Select an option from the menu (or enter q to quit): ', end='')

def GetMenuChoice():

  print()
  Choice = input()
  Choices = ["Q","Quit","quit"]
  if Choice in Choices:
    Choice = "q"
  return Choice


def LoadDeck(Deck):
  CurrentFile = open('deck.txt', 'r')
  Count = 1
  while True:
    LineFromFile = CurrentFile.readline()
    if not LineFromFile:
      CurrentFile.close()
      break
    Deck[Count].Suit = int(LineFromFile)
    LineFromFile = CurrentFile.readline()
    Deck[Count].Rank = int(LineFromFile)
    Count = Count + 1
 
def ShuffleDeck(Deck):
  SwapSpace = TCard()
  NoOfSwaps = 1000
  for NoOfSwapsMadeSoFar in range(1, NoOfSwaps + 1):
    Position1 = random.randint(1, 52)
    Position2 = random.randint(1, 52)
    SwapSpace.Rank = Deck[Position1].Rank
    SwapSpace.Suit = Deck[Position1].Suit
    Deck[Position1].Rank = Deck[Position2].Rank
    Deck[Position1].Suit = Deck[Position2].Suit
    Deck[Position2].Rank = SwapSpace.Rank
    Deck[Position2].Suit = SwapSpace.Suit

def DisplayCard(ThisCard,AceHigh):
  print()
  print('Card is the', GetRank(ThisCard.Rank,AceHigh), 'of', GetSuit(ThisCard.Suit))
  print()

def GetCard(ThisCard, Deck, NoOfCardsTurnedOver):
  ThisCard.Rank = Deck[1].Rank
  ThisCard.Suit = Deck[1].Suit
  for Count in range(1, 52 - NoOfCardsTurnedOver):
    Deck[Count].Rank = Deck[Count + 1].Rank
    Deck[Count].Suit = Deck[Count + 1].Suit
  Deck[52 - NoOfCardsTurnedOver].Suit = 0
  Deck[52 - NoOfCardsTurnedOver].Rank = 0

def IsNextCardHigher(LastCard, NextCard):
  Higher = False
  if NextCard.Rank > LastCard.Rank:
    Higher = True
  return Higher

def GetPlayerName():

  Valid = False
  while Valid == False:
    PlayerName = input('Please enter your name: ')
    if PlayerName == "":
       print()
       print("You must enter a name:" )
       print()
    else:
      Valid = True
      return PlayerName

  
def GetChoiceFromUser():
  Yes = ["y","Y","Yes","yes"]
  No = ["n","N","No","no"]
  Choice = input('Do you think the next card will be higher than the last card (enter y or n)? ')
  if Choice in Yes:
    Choice = "y"
    return Choice
  elif Choice in No:
    Choice = "n"
    return Choice

def DisplayEndOfGameMessage(Score):
  print()
  print('GAME OVER!')
  print('Your score was', Score)
  if Score == 51:
    print('WOW! You completed a perfect game.')
  print()

def DisplayCorrectGuessMessage(Score):
  print()
  print('Well done! You guessed correctly.')
  print('Your score is now ', Score, '.', sep='')
  print()

def ResetRecentScores(RecentScores):
  for Count in range(1, NO_OF_RECENT_SCORES + 1):
    RecentScores[Count].Name = ''
    RecentScores[Count].Score = 0

def Date():
  import datetime
  today = datetime.date.today()
  return today
 
def DisplayRecentScores(RecentScores,today):
  print("")
  print('Recent Scores: ')
  print("")
  print("Name     Score".format(today))
  for Count in range(1, NO_OF_RECENT_SCORES + 1):
    print("{0:<10}{1:<10}".format(RecentScores[Count].Name, RecentScores[Count].Score))
    print ("Date saved:{:%d/%m/%y}".format(today))
    print()
  print('Press the Enter key to return to the main menu')
  
  

def UpdateRecentScores(RecentScores, Score):
  AddScore = input("Add name to scores? (Y/N):")
  Yes = ["Y","y","Yes","yes"]
  No = ["N","n","no","No"]
  if AddScore in Yes:
    PlayerName = GetPlayerName()
    FoundSpace = False
    Count = 1
    while (not FoundSpace) and (Count <= NO_OF_RECENT_SCORES):
      if RecentScores[Count].Name == '':
        FoundSpace = True
      else:
        Count = Count + 1
    if not FoundSpace:
      for Count in range(1, NO_OF_RECENT_SCORES):
        RecentScores[Count].Name = RecentScores[Count + 1].Name
        RecentScores[Count].Score = RecentScores[Count + 1].Score
      Count = NO_OF_RECENT_SCORES
    RecentScores[Count].Name = PlayerName
    RecentScores[Count].Score = Score
  elif AddScore in No:
    print("")
    print("Score ignored")
    print("")
    
    
def PlayGame(Deck, RecentScores,AceHigh):
  LastCard = TCard()
  NextCard = TCard()
  GameOver = False
  GetCard(LastCard, Deck, 0)
  DisplayCard(LastCard,AceHigh)
  NoOfCardsTurnedOver = 1
  while (NoOfCardsTurnedOver < 52) and (not GameOver):
    GetCard(NextCard, Deck, NoOfCardsTurnedOver)
    Choice = ''
    while (Choice != 'y') and (Choice != 'n'):
      Choice = GetChoiceFromUser()
    DisplayCard(NextCard)
    NoOfCardsTurnedOver = NoOfCardsTurnedOver + 1
    Higher = IsNextCardHigher(LastCard, NextCard)
    if (Higher and Choice == 'y') or (not Higher and Choice == 'n'):
      DisplayCorrectGuessMessage(NoOfCardsTurnedOver - 1)
      LastCard.Rank = NextCard.Rank
      LastCard.Suit = NextCard.Suit
    else:
      GameOver = True
  if GameOver:
    DisplayEndOfGameMessage(NoOfCardsTurnedOver - 2)
    UpdateRecentScores(RecentScores, NoOfCardsTurnedOver - 2)
  else:
    DisplayEndOfGameMessage(51)
    UpdateRecentScores(RecentScores, 51)

if __name__ == '__main__':
  for Count in range(1, 53):
    Deck.append(TCard())
  for Count in range(1, NO_OF_RECENT_SCORES + 1):
    RecentScores.append(TRecentScore())
  Choice = ''
  while Choice != 'q':
    DisplayMenu()
    Choice = GetMenuChoice()
    if Choice == '1':
      LoadDeck(Deck)
      ShuffleDeck(Deck)
      AceHigh = SetOptionsHighOrLow()
      PlayGame(Deck, RecentScores,AceHigh)
    elif Choice == '2':
      LoadDeck(Deck)
      PlayGame(Deck, RecentScores)
    elif Choice == '3':
      today = Date()
      DisplayRecentScores(RecentScores,today)
    elif Choice == '4':
      ResetRecentScores(RecentScores)
    elif Choice == "5":
      DisplayOptions()
