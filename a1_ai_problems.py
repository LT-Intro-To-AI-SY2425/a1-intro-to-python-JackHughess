import string

# Complete your individualized AI problems here

def palchecker(s: str):
    index = 0
    newString = ""
    for i in s:
        if i not in string.punctuation and i!=" ":
            newString+=i
    return newString == newString [::-1]


def longestWord(s: str):
    words = s.split()
    longestWord = ""
    for word in words:
        if len(word) > len(longestWord):
            longestWord = word

    return longestWord


def fizbuzz(input_num):
    if(input_num%3==0):
        if(input_num%5==0):
            return 'FizzBuzz'
        return 'Fizz'
    elif(input_num%5==0):
        return 'Buzz'
    else:
        return input_num

def factorialRecurs(n: int):
    if n == 1:
        return 1
    else:
        return n*(factorialRecurs(n-1))

assert fizbuzz(1) == 1, "fizzbuzz 1 test"
assert fizbuzz(3) == "Fizz", "fizzbuzz 3 test"
assert fizbuzz(4) == 4, "fizzbuzz 4 test"
assert fizbuzz(5) == "Buzz", "fizzbuzz 5 test"
assert fizbuzz(6) == "Fizz", "fizzbuzz 6 test"
assert fizbuzz(15) == "FizzBuzz", "fizzbuzz 15 test"
assert palchecker("ta.co cat") == True, "palchecker test"
assert longestWord("The quick brown fox jumps over the lazy dogwwwwwwwwwwwwwwww") == "dogwwwwwwwwwwwwwwww", "lon word test"
assert factorialRecurs(4) == 24, "fact test"
