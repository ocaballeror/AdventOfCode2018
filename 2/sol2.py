def close(a, b):
    """Check if strings differ only by one character."""
    diff = False
    for c, d in zip(a, b):
        if c != d:
            if diff:
                return False
            diff = True
    return diff

# will contain all pairs of strings that differ only by one character.
close_words = set()
words = set(map(str.strip, open('input')))
for v in words:
    for u in words:
        if close(u, v):
            close_words.add((u, v))

solutions = set()
for a, b in close_words:
    # Keep only the common characters of two "close" strings
    solutions.add(''.join(c for c, d in zip(a, b) if c == d))

print(solutions)
