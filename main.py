def olib_tashlash(tarz):
    return list(set(tarz))

# Test qilish
tarz = [1, 2, 2, 3, 4, 4, 5, 6, 6]
print(olib_tashlash(tarz))  # [1, 2, 3, 4, 5, 6]
```

```python
def olib_tashlash(tarz):
    return list(dict.fromkeys(tarz))

# Test qilish
tarz = [1, 2, 2, 3, 4, 4, 5, 6, 6]
print(olib_tashlash(tarz))  # [1, 2, 3, 4, 5, 6]
