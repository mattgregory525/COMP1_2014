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
SetAceHigh = False

def BubbleSortScores(RecentScores):
  ##RecentScores is a record, so use attributes somehow 
  Swapped = True
  while Swapped:
    Swapped = False
    for count in range(len(RecentScores)-1):
      if RecentScores[count] > RecentScores[count+1]:
        temp = RecentScores[count]
        RecentScores[count] = RecentScores[count+1]
        RecentScores[count+1] = temp
        Swapped = True
  return RecentScores


def GetRank(RankNo):
  
  Rank = ''
  if RankNo == 1:
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
 
    
def GetOptionChoice():
  Option = input("Please enter your option: ")
  return Option


def SetOptions(Option):
  if Option == 1:
    SetAceHigh = SetAceHighOrLow()
    return SeAceHigh
  elif Option == 2:
    print("Option 2 ")
  
    
def SetAceHighOrLow():
  Choice = input("Set ace (h)igh or (l)ow? :")
  if Choice == "h":
    SetAceHigh = True
    done = True
    print("Ace set to high")
  elif Choice == "l":
    SetAceHigh = False
    done = True
    print("Ace set to low")
  return SetAceHigh

  
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

def DisplayCard(ThisCard):
  print()
  print('Card is the', GetRank(ThisCard.Rank), 'of', GetSuit(ThisCard.Suit))
  print()

def GetCard(ThisCard, Deck, NoOfCardsTurnedOver):
  ThisCard.Rank = Deck[1].Rank
  ThisCard.Suit = Deck[1].Suit
  for Count in range(1, 52 - NoOfCardsTurnedOver):
    Deck[Count].Rank = Deck[Count + 1].Rank
    Deck[Count].Suit = Deck[Count + 1].Suit
  Deck[52 - NoOfCardsTurnedOver].Suit = 0
  Deck[52 - NoOfCardsTurnedOver].Rank = 0

def IsNextCardHigher(LastCard, NextCard,SetAceHigh):
  Higher = False

  if SetAceHigh == False:
    if NextCard.Rank > LastCard.Rank:
      Higher = True
  
  elif SetAceHigh == True:
    if NextCard.Rank == 1:
      Higher = True
    elif LastCard.Rank == 1:
      Higher = False
    elif NextCard.Rank > LastCard.Rank:
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
  today = today.strftime("%d/%m/%y")
  return today
 
def DisplayRecentScores(RecentScores,today):
  today = Date()
  print("")
  print('Recent Scores: ')
  print("")
  print("{0:<10}{1:<10}{2:<10}".format("Name","Score","Date"))
  for Count in range(1, NO_OF_RECENT_SCORES + 1):
    if len(RecentScores[Count].Name)>=1:
      print("---------------------------")
      print("{0:<10}{1:<9}{2:<10}".format(RecentScores[Count].Name, RecentScores[Count].Score,today))
      print("---------------------------")
 
  
  

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
    

def PlayGame(Deck, RecentScores):
  LastCard = TCard()
  NextCard = TCard()
  GameOver = False
  GetCard(LastCard, Deck, 0)
  DisplayCard(LastCard)
  NoOfCardsTurnedOver = 1
  while (NoOfCardsTurnedOver < 52) and (not GameOver):
    GetCard(NextCard, Deck, NoOfCardsTurnedOver)
    Choice = ''
    while (Choice != 'y') and (Choice != 'n'):
      Choice = GetChoiceFromUser()
    DisplayCard(NextCard)
    NoOfCardsTurnedOver = NoOfCardsTurnedOver + 1
    Higher = IsNextCardHigher(LastCard, NextCard,SetAceHigh)
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
      PlayGame(Deck, RecentScores)
    elif Choice == '2':
      LoadDeck(Deck)
      PlayGame(Deck, RecentScores)
    elif Choice == '3':
      today = Date()
      BubbleSortScores(RecentScores)
      DisplayRecentScores(RecentScores,today)
    elif Choice == '4':
      ResetRecentScores(RecentScores)
    elif Choice == "5":
      DisplayOptions()
      Option = GetOptionChoice()
      SetOptions(Option)
      SetAceHigh = SetAceHighOrLow()

      
     
      
        
      
