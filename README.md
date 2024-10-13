# Scrabble Word Score

Scrabble is a popular spelling board game. Players get points for spelling words, based on the value of the letters in the word. In this task, you won't build all of scrabble - just a part of the scoring. If you're not familiar with Scrabble, see the "Scrabble scoring" section below for an explanation.

In this assignment, you'll write a program that calculates the score for a word.

## Your Task

The starter code prints out a greeting, gets a word from the user using `input`, and sets the starting score to zero. You need to add the code to add up the letter values in the word.

Follow the instructions in the comments:
- use a loop to go through the letters in the word
- use `if` and `elif` statements to determine what to add to the score for each letter
- use `in` to check whether the letter is a member of a particular group of letters for scoring.

Below, you'll find an explanation for how to use the `in` keyword in loops and conditions, as well as a table of the scrabble letter values.

## Expected Results

Run the tests to check if your solution is correct.

When it's working, the program should look like this when it's run:

```
Generate the scrabble score for a word.
Enter a word: amorphous
amorphous has a scrabble score of 16
```

```
Generate the scrabble score for a word.
Enter a word: jezebel
jezebel has a scrabble score of 25
```

## Looping over the letters in a string

A `for` loop can loop through the letters in a string. Here's what it looks like to print out each letter in the string `"kibo"`:

```python
for letter in "kibo":
  print(letter)
```

You use the syntax `for x in the_string`. `x` will take on each letter's value in the loop.

## The `in` keyword

The `in` keyword can also test if a letter is inside of a string. If the letter is in the string, `in` returns `True`, otherwise, it returns `False`.

```python
'k' in "kibo" # True
'm' in "kibo" # False
letter = "i"
word = "kibo"
letter in word # True
```

You'll need to use the `for ... in` loop as well as the `letter in word` comparison to solve this challenge.

## Scrabble letter values

Each letter tile in scrabble has a point value. Here are the point values and the letters that have that value:

| Value | Letters    |
|-------|------------|
| 1     | aeilnorstu |
| 2     | dg         |
| 3     | bcmp       |
| 4     | fhvwy      |
| 5     | k          |
| 8     | jx         |
| 10    | qz         |


## Scrabble Scoring

A word score in Scrabble is the value of each of the letters, added up. So, the score for "apple" is 9:

```
a + p + p + l + e
1 + 3 + 3 + 1 + 1 = 9
```

The score for "quixotic" is

```
q  + u + i + x + o + t + i + c
10 + 1 + 1 + 8 + 1 + 1 + 1 + 3 = 26
```

In the actual game of Scrabble, there's also rules about where the word is played on the board, but we're skipping those for this assignment.

## Testing

First, test your program yourself in the terminal. (Try "apple" and "quixotic"
to start, plus some other scrabble words where you know the correct score)

Then, run the automated tests to confirm that your solution works. Run `python3 test_main.py` to run the tests.
