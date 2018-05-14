# partition
partition a sum

# example
```python
>>> from partition import partition
>>> partition(4,[1,2,3]) # partition 4 into 3 numbers, each of which has respective upper bound, inclusive
<generator object partition at 0x107fd8a98>
>>> list(_)
[(0, 1, 3), (0, 2, 2), (1, 0, 3), (1, 1, 2), (1, 2, 1)] # each tuple is a solution. sum and bound complied.
>>> 
```

# run test
```
python -m pytest tests.py
```

# related question
n-sum, subset sum

### packaging reminder
https://packaging.python.org/tutorials/distributing-packages/
