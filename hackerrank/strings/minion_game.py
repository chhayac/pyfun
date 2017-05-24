# Kevin and Stuart want to play the 'The Minion Game'.
# Game Rules

# Both players are given the same string,S.
# Both players have to make substrings using the letters of the string S.
# Stuart has to make words starting with consonants.
# Kevin has to make words starting with vowels. 
# The game ends when both players have made all possible substrings. 

# Scoring
# A player gets +1 point for each occurrence of the substring in the string S.

# For Example:
# String S = BANANA
# Kevin's vowel beginning word = ANA
# Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points. 

# Input Format
# A single line of input containing the string S. 
# Note: The string S will contain only uppercase letters:[A - Z].

# Output Format
# Print one line: the name of the winner and their score separated by a space.
# If the game is a draw, print Draw.

# Sample Input
# BANANA

# Sample Output
# Stuart 12

def minion_game(string):
    vowels = 'AEIOU'
    kevin_score = 0
    stuart_score = 0
    for i in range(len(s)):
        if s[i] in vowels:
            kevin_score += (len(s) - i)  # Number of possible words left to right from a word of length n is always 
                                         # n + (n-1) + (n-2) +..1
        else:
            stuart_score += (len(s) - i)
    if kevin_score > stuart_score:
        print("Kevin", kevin_score)
    elif stuart_score > kevin_score:
        print("Stuart", stuart_score)
    else:
        print("Draw")
       
    
if __name__ == '__main__':
    s = input()
    minion_game(s)
