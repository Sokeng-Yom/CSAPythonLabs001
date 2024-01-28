# Application 1
# Given a string, you have to return a string in which each character (case-sensitive) is repeated once.

# Examples (Input -> Output):
# * "String"      -> "SSttrriinngg"
# * "Hello World" -> "HHeelllloo  WWoorrlldd"
# * "1234!_ "     -> "11223344!!__  "

user = input("Enter a word: ")
def double(str):
  all_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
  new_str = ''
  for b in str:
    if b.lower() in all_letters:
      new_str += b
    new_str += b
  return new_str
print(double(user))

# Application 2
#  Given a string indicating a range of letters, return a string which includes all the letters in that range, including the last letter. Note that if the range is given in capital letters, return the string in capitals also!

# Examples
# "a-z" ➞ "abcdefghijklmnopqrstuvwxyz"
# "h-o" ➞ "hijklmno"
# "Q-Z" ➞ "QRSTUVWXYZ"
# "J-J" ➞ "J"
# Notes A hyphen will separate the two letters in the string.

user_range1st = input("Enter the First letter: ")
user_range2nd = input("Enter the Second letter: ")
alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
start = user_range1st.split('-')
end = user_range2nd.split('-')
firstLetter = alphabet.index(user_range1st[0])
lastLetter = alphabet.index(user_range2nd[0])
final_result = alphabet[firstLetter : lastLetter + 1]
print(final_result)




