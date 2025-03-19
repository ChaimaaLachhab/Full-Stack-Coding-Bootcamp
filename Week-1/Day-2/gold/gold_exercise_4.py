# Exercise 4: Double Dice

import random

def throw_dice():
    """Simulates rolling a six-sided dice."""
    return random.randint(1, 6)

def throw_until_doubles():
    """Rolls two dice until both land on the same number (doubles)."""
    count = 0
    while True:
        die1 = throw_dice()
        die2 = throw_dice()
        count += 1
        if die1 == die2:
            return count

def main():
    """Simulates throwing doubles 100 times and calculates statistics."""
    results = [throw_until_doubles() for _ in range(100)]

    total_throws = sum(results)
    average_throws = total_throws / len(results)

    print(f"Total throws to reach 100 doubles: {total_throws}")
    print(f"Average throws to reach doubles: {average_throws:.2f}")

# Run the main function
main()
