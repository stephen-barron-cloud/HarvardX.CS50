# Loops

## work files
- [cat.py](cat.py)
- [cat2.py](cat2.py)
- [hogwarts](./hogwarts.py)
- [mario.py](./mario.py)

## While loop
'''
while i < m:
        action
        i += 1 # shortened
'''

## New Variable type list
'''
for i in [0, 1, 2]:
    print("meow")
'''

## New Variable type dict (Dictionary)
key value stores

'''
for i in [0, 1, 2]:
    print("meow")
'''

## new function range
for placeholder value use "_" **underscore**

    ```
    for _ in range(100):
        action
    ```

## new function len (length)
returns the length of a list or other variable types

    ```
    x = len(var_list)

    for i in range(len(var_list)):
        print(var_list[i])
    ```

#

## New keywords Continue, Break
The benefit here is that we can repeatedly ask a quesiton until we get a value we deem appropriate.  this appears to only work ofr integers at this point, so input validation needs work.  if I put in anything other than a number I get a value error

## New keyword None
Must be capitalized

```
def main5():
    while True:
        n = int(input("What is n?"))
        if n < 0:
            continue
        else:
            break
```

## Problem Submission
