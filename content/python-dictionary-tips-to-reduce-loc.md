title: Python dictionary tips and tricks that reduce your lines of code
date: 2019-05-31 02:27
category: Python
tags: Python
slug: python-dictionary-tips-to-reduce-loc
summary: Couple of tips and tricks that help you code faster and reduce your lines of code when you playing with Python dictionary.

## Constructs a dict

There are many ways to create a dictionary, from easy to fancy ... 

* Vanilla style (the curly bracket)

```python
>>> {"key1": 1, "key2": 2, "key3": {"value": 3}}
{"key1": 1, "key2": 2, "key3": {"value": 3}}
```

* a mapping object (dict itself is a mapping object)

```python
>>> dict1 = {"key1": 1, "key2": 2, "key3": {"value": 3}}
>>> dict(dict1)
{"key1": 1, "key2": 2, "key3": {"value": 3}}
```

However, this only creates a shallow copy of dict1. Any mutation to objects within dict1 affects on the new dict.

* an iterable object (such as a list)

```python
>>> list1 = [("key1", 1), ("key2", 2), ("key3", {"value": 3})]
>>> dict(list)
{"key1": 1, "key2": 2, "key3": {"value": 3}}
```

Items within the list must be able to break up to a key-value pair, which means items should be iterable having two and only two values. The first will be the key, and the second will be the value.

* keyword arguments

```python
>>> dict1 = {"key1": 1, "key2": 2}
>>> dict2 = {"key4": 4}
>>> dict(**dict1, key3={"value": 3}, **dict2)
{'key1': 1, 'key2': 2, 'key3': {'value': 3}, 'key4': 4}
```

This is my favorite usage of dict constructor. It extremely helpful when you need to merges many dictionaries into one. Comparing to dict.update(), it merges as many as dictionaries you want and doesn't alter the original dictionary.

*\* Note: The \*\* syntax unpacks a dictionary as keyword arguments that passing to a function.*

## Update a dict

It's unavoidable to update their values when you are playing around with dict. There are couple tips might saving you a couple lines of code when you updating a dict.

* The no-surprise style

```python
>>> dict1 = {"key1": 1, "key2": 2, "key3": {"value": 3}}
>>> dict1["key1"] = 10
>>> dict1
{"key1": 10, "key2": 2, "key3": {"value": 3}}
```

However, if you try to update a key where it doesn't exist in the dict, KeyError will be thrown.

* Update many keys at once

```python
>>> dict1 = {"key1": 1, "key2": 2, "key3": {"value": 3}}
>>> dict1.update({"key1": 10, "key4": 40})
>>> dict1
{"key1": 10, "key2": 2, "key3": {"value": 3}, "key4": 40}
```

Worth to notice that you can update values even not yet existing in the origin dict.

* Update a key based on its current value

For a word counting program, you need to increment a word's occurrence based on its current value. However, the value might be not even existed yet. Normally, you would need to set up a temporary value and assign the incremented value back to the dict. But there is an easier way to achieve that,

```python
>>> dict1 = {"hello": 1}
>>> dict1["hello"] += 1
>>> dict1["world"] = dict1.get("world", 0) + 1
{"hello": 2, "world": 1}
```

On Line-3, we get its current value first using get("world", 0), which sets a default value when the key is not yet in the dict. 
