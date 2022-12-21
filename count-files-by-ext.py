"""
List all extensions found in a given directory and report how many files were found for each extension
"""
import sys
from pathlib import Path
from collections import Counter
from pprint import pprint

top = sys.argv[1]
counter = Counter()

for f in Path(top).glob('**/*'):
  if f.is_file() and f.suffix:
    counter[f.suffix] += 1
  
pprint(counter)
total = sum(counter.values())
print(f'Total: {total}')
