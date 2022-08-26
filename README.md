<!-- vscode-markdown-toc -->

# Table of Contents

- [Binary search](#Binarysearch)
- [A Better way to search](#ABetterwaytosearch)
- [Example](#Example)

<!-- vscode-markdown-toc-config
	numbering=true
	autoSave=true
	/vscode-markdown-toc-config -->
<!-- /vscode-markdown-toc -->

## <a name='Binarysearch'></a>Binary search

Binary search is an algorithm; its input is a sorted list of elements. If an element you are looking for is in that list, binary search returns the position where it's located. Otherwise, binary search returns `null`.

Here's is how it works. I'm thinking of a number between 1 and 100.

![](/static/1-100.PNG)

You have to try guess my number in the fewest tries possible. With every guess, I'll tell you if your guess is too low, too high, or correct.

Suppose you start guessing like this 1, 2, 3, 4 .... If the number I am thinking of is 99 you'll have 99 tries.

![](/static/simple_search.PNG)

This is _simple search_, and it is not effective.

### <a name='ABetterwaytosearch'></a>A Better way to search

A better technique. Start with 50. If the number I am thinking of is 99, 50 is too low. But you just eliminated nos 1-50 (50 tries) in 1 try.

![](/static/binary_search.PNG)

Next guess - 75. I tell you, still low. You've now eliminated another 25 nos (75 tries) in 2 tries.
Again, cut down the remaining nos (76 - 100) by half, and suggest 88. But still low. Repeat the process again, next try is 94, still low.

And again, next try is 97, still low.

Now you have 3 nos remaining. You'll have gotten the number I'm thinking of in 6 - 7 tries out of 99.

![](/static/7_steps.PNG)

### <a name='Example'></a>Example

Let's take a look at how to write a binary search in Python. To fully understand the code below you'll need some understanding of how arrays work.

We'll write a function, `binary_search`, that takes a sorted array and an item (that we'll search for). If the item is in the array, the function returns the item's position. The function will keep track of what part of the array has been searched through.

The first execution of the array will assign two variables as below:

```python
low = 0
high = len(list) - 1
```

These two will help us keep track of what part of the list to search. The function will loop while checking for a new middle element that'll either be higher, lower or equal to the item we are searching for.

Here is how the function checks for the middle element:

> NB: `mid` is the position of the middle element within the array, not the actual element. Python rounds it down automatically if `(low+high)` is not an even number. The actual element is retrieved as follows `guess = list[mid]`

```python
mid = (low + high) / 2
guess = list[mid]
```

If the `guess` is too low, the `low` variable is updated:

```python
if guess < item:
    low = mid + 1
```

And if the `guess` is too high, we update the `high` variable.

```python
if guess > item:
    high = mid + 1
```

If the `guess` is equal to `item` it means we've found the item. So we return its position.

```python
if guess == item:
    return mid
```

Here's the full code:

```python
def binary_search(list, item):
    """
    This function takes a sorted array and an item.
    If the item is in the array, the function returns its position.
    """
    # high & low check what part of the list to search
    low = 0
    high = len(list) - 1

    # if remaining elements is more than one
    while low <= high:
        # get the middle element as the guess
        mid = (low+high)/2
        guess = list[mid]

        # if guess is equal item
        if guess == item:
            return mid

        # if guess is too high else is too low
        if guess > item:
            # update new high
            high = mid - 1
        else:
            # update new low
            low = mid - 1
    return None
```
