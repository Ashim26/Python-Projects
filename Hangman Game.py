#!/usr/bin/env python
# coding: utf-8

# ### Hangman Game
# 1.computer has a list
# 2.computer will choose a random word form the list .
# the dplayer 10 wrong guesses (10 turns)
# The game follows this loop:-
#    .computer prints the word character by charector replacing with underscore          those not gussed yet (initial to charactors has been gussed)
#    .player guesses  a charector
#    .if character is no t in word , a turn is wihdrawn 
#    .if no turen lest , computer wins
#    .if player hass guessed all character , player wins 
#     

# In[17]:


my_list = [ 'father', 'enterprice', 'science',  'programming', 'resistance', 'fiction', 'condition','reverse', ' computer','python']


# In[ ]:


import random
s = random.choice(my_list)
s
print(s)
guesses =''
turns  = 1

while turns<= 10:
    for c in my_list:
        if c in guesses:
            print(c, end=' ')
        else:
            print('_', end=' ')
    print()
    guess = input("Guess a char:")
    guesses = guesses + guess    
    
print(guesses)
# if (guesses == s)
#     print('Player wins ')
# else
#     pass
    


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




