import re
import string
from common import react_polymer, read_input


results = {}
content = read_input()
for letter in string.ascii_lowercase:
    regex = '[{}{}]'.format(letter, letter.upper())
    polymer = re.sub(regex, '', content)
    results[letter] = react_polymer(polymer)

best = min(results, key=lambda x: results[x])
print(best, results[best])
