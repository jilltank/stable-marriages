roc# python 2
import time
"""
This is a program which takes user imputs 
and prints the results for the "Stable Marriages" equation
which you can find out more about at
https://www.youtube.com/watch?v=Qcv1IqHWAzg
"""

def start():
  """
  This is going to encompass the entire equation.
  It will explain the parameters and then ask for user input. 
  Then it will spit out the results. 
  """
  print 'This code is based on an algorithym called the stable marriages problem.'
  time.sleep(2.5)
  print ' '
  print 'It was used hypothetically to create the best versions of heterosexual marriages'
  print 'between an equal number of men and women.'
  time.sleep(2.5)
  print ' '
  print 'It can also be used to match, for example, interns with businesses.'
  time.sleep(2.5)
  print ' '
  print 'Each person creates a list of their preferences,'
  print 'with the first preference listed first, then ranked down from there.'
  time.sleep(2.5)
  print ' '
  print 'Let\'s begin.'
  print ' '
  time.sleep(2.5)
  total = raw_input('How man total participants will there be?')
  total = int(total)
  half = total/2
  if total > 0 and total%2 == 0:
    """
    print ' '
    print 'I will now ask for the name of each participant.'
    print 'Be sure to enter their names correctly, exactly the same as you will every time.'
    print 'This program is case sensitive.'
    print 'this will be used to test errors throughout the program.'
    """
    masterList = makeMasterList(total, [])
    """
    print: 'Now we will enter the preferences of all the participants.'
    print 'All of the women's preferences will need to be entered first, one by one.'
    print 'Then all of the men can enter their preferences.'
    """
  else:
    print 'That is not a valid number. Remember that it must be even and nonnegative.'
    return
  theWholeShebang = runIt(total, half, [], masterList)
  """
  time.sleep(1.5)
  print 'Well, here is a fancy list that comprises all the ranked information you\'ve given me.'
  print theWholeShebang
  time.sleep(1.0)
  """
  print 'Here is a list of all the women\'s preferences:'
  women = theWholeShebang[:half]
  print women
  time.sleep(1.0)
  print 'And here\'s a list of all the men\'s preferences:'
  men = theWholeShebang[half:]
  print men
  """
  time.sleep(1.0)
  print 'Next, we basically go through cycles until everyone is matched to the best possible person for them.'
  time.sleep(1.5)
  print 'We accomplish this by having all the women propose to the first man on their list. This means that some men may have multiple offers while others have none.'
  time.sleep(1.0)
  print 'If a man has multiple offers of marriage, he looks at all the women who proposed and chooses the one that\'s ranked highest on his list.'
  time.sleep(1.0)
  print 'If a man only has one offer of marriage, he accepts.'
  time.sleep(1.0)
  print 'If a man has no offers, he has to wait until the next round, for all engagements are tentative and subject to change.'
  """
  roundOne = theWomenPropose(women, half, [])
  multiple = repeats(breakItDown(roundOne, []), [])
  if multiple != []:
    print multiple, 'had multiple marriage proposals!'
    theWomenWhoProposed = listOfProposers(roundOne, multiple, [])
    print theWomenWhoProposed
      # make sure to create a check in case more than one man was proposed to multiple times
      # then we need to make a function that takes the list plus bingley's list
      # finds the first person to be listed.






def makeMasterList(n, e):
  """
  this list takes a nonnegative number > 0 that is equal to the number of participants
  in the stable marriage project.
  it creates a master list of all the names of the participants.
  this will be used to check for errors throughout the alogrithym.
  """
  if n > 0:
    participant = raw_input('Name of participant?')
    if participant in e:
      print 'ERROR: This name has already been entered. Try again.'
      return masterList(n, e)
    else:
      e = e + [participant]
      return makeMasterList(n-1, e)
  else:
    return e


def listCountdown(n, L, m):
  """
  takes one nonnegative number and counts it down to zero
  """
  if n < 0:
    print 'There is a problem with the countdown number. Check the input number.'
  elif n > 0:
    newName = raw_input("Next name on list?")
    if newName not in m:
      print 'ERROR: That is not one of the names of the participants.'
      print 'Remember to enter the name with the correct spelling.'
      print 'Capitalization matters.'
      return listCountdown(n, L, m)
    L = L + [newName]
    n = n-1
    return listCountdown(n, L, m)
  else:
    return L
    

def userInput(t, m):
  """
  this is going to take one "person's" marriage preferences
  and place them in an array that will be automatically as long as their list
  with index 0 being the person's name
  """
  name = raw_input("What is the list owner\'s name?")
  if name not in m:
    print 'ERROR: That is not one of the names of the participants.'
    print 'Remember to enter the name with correct spelling.'
    print 'Capitialization matters.'
    return userInput(t, m)
  firstName = raw_input("What is the first name on your list?")
  if firstName not in m:
    print 'ERROR: That is not one of the names of the participants.'
    print 'Remember to enter the name with correct spelling.'
    print 'Capitalization matters.'
    print 'We are going to back up one step. You need to enter the list owner\'s name again.'
    print 'Then we can enter the first name on the list again.'
    return userInput(t, m)
  list = [name] + [firstName]
  length = t-1
  completeList = listCountdown(length, list, m)
  time.sleep(1.5)
  print completeList
  return completeList


def runIt(n, t, u, m):
  """
  this function runs the userInput() function the specified number of times.
  n is a tally of how many more times it needs to run
  t is the total number of times.
  the other function has already checked to make sure that the number is an even,
  nonnegative number.
  """
  if n > 0:
    n = n-1
    u += [userInput(t, m)]
    return runIt(n, t, u, m)
  else:
    return u


def theWomenPropose(w, t, u):
  """
  This function takes the master list of all the women's preferences (w)
  and returns all the women's first preference.
  """
  if t > 0:
    subjectMatter = w[t-1]
    bride = subjectMatter[0]
    groom = subjectMatter[1]
    print bride, 'proposes to', groom
    u += [[bride, groom]]
    t -= 1
    return theWomenPropose(w, t, u)
  else:
    return u




def breakItDown(L, e):
  """
  this is going to take a list of a lot of other lists (L)
  and break it down into one big list (e, which starts out as an empty list) 
  so we can run it through a repeating function
  and check to see if there are any repeats.
  Sigh.
  """
  if L == []:
    return e
  else:
    e = e + L[0]
    L = L[1:]
    return breakItDown(L, e)
  
  
def repeats(L, e):
  """
  L is a list of people who were involved in the proposals
  e is an empty list
  this function checks to see if anybody had multiple proposals.
  If so, it returns their name in an empty list.
  note to self: a simple function will only find the name.
  it won't check to see if the name has already been found.
  Make sure you check that.
  """
  if L == []:
    return e
  elif L[0] in L[1:]:
    if L[0] not in e:
      e = L[0]
      return repeats(L[1:], e)
    else:
      return repeats(L[1:], e)
  else:
    return repeats(L[1:], e)
    



"""
w = [['Elizabeth', 'Wickham', 'Darcy', 'Bingley', 'Collins'], ['Jane', 'Bingley', 'Wickham', 'Darcy', 'Collins'], ['Charlotte', 'Bingley', 'Darcy', 'Collins', 'Wickham'], ['Lydia', 'Bingley', 'Wickham', 'Darcy', 'Collins']]
m = [['Darcy', 'Elizabeth', 'Jane', 'Charlotte', 'Lydia'], ['Bingley', 'Jane', 'Elizabeth', 'Lydia', 'Charlotte'], ['Collins', 'Jane', 'Elizabeth', 'Lydia', 'Charlotte'], ['Wickham', 'Lydia', 'Jane', 'Elizabeth', 'Charlotte']]

list = theWomenPropose(w, 4, [])
list = breakItDown(list, [])
print repeats(list, [])
"""


def listOfProposers(L, M, e):
  """
  this function takes the master list of all the proposals submitted for the specific round
  defined as L
  and a string of a man who was proposed to multiple times
  that's M
  and then there's e, another special snowflake empty list that will be filled by the time the function ends
  the function returns a list of just the women who proposed to the man in m.
  it returns that list in e
  """
  if L == []:
    return e
  else:
    if M in L[0]:
      n = L[0]
      e = e + [n[0]]
      return listOfProposers(L[1:], M, e)
    else:
      return listOfProposers(L[1:], M, e)

"""
w = [['Elizabeth', 'Wickham'], ['Jane', 'Bingley'], ['Charlotte', 'Bingley'], ['Lydia', 'Bingley']]
m = 'Bingley'
print listOfProposers(w, m, [])
"""  
start()

"""
Now I need to define a function (repeats) for when someone has multiple proposals.
So I need the computer to look at my list and see if any names are repeated in there.
This will require recursion and a function or two.


If a name is repeated (multiple offers) it would need to 
1. make a list of all the people who proposed to him.
2. search the master list for the specific person's list
so if the 0 index is that person's name
3. Choose the highest-ranked person from the list created in number 1.
4. If he rejects people, then they must be literally struck from the list, methinks.
If they are literally struck from the list, then I guess the best way to check to see
whether the algorithym can stop running is when every individual is paired
with the top person on their list. Though this won't always be true.
I may need to do something with an 'or' or something. hmmmm.....
Well, it may be the case that all but one person go with the top person on their list.
In that case, it would still be considered stable, even if the last couple isn't the happiest,
because there's literally nobody else to go to.
OR OR OR OR....I guess the marriages are considered stable when all the WOMEN
are engaged to their top choice (as they would have had the other crossed off their list)
The men might prefer somone else, but the woman clearly wouldn't, so tough luck!


From the video:
Day 1: Each woman proposes to her first choice.
Each man rejects all but his top suitor.
Day 2: Each rejected woman proposes to her next choice.
Each man rejects all but his top suitor. Some tentative engagements may change.
Day 3, 4, 5.... Repeat until the alogrithym stops.
"""
