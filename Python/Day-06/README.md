# Day 6 – Python Basics (Lists) 🐍

## 📋 Lists
A **list** is a collection used to store **multiple items** in a single variable.

- A list can store **similar or different data types**
- Lists are **ordered**
- Lists are **mutable** (values can be changed)
- Lists allow **duplicate values**

---

## 🛠 Creating a List
A list is created by placing items inside square brackets `[]`, separated by commas.

```python
numbers = [1, 2, 3, 4]
mixed = [1, "Python", 3.5, True]
duplicates = [1, 1, 2, 2]
````

### Key Points:

* Lists can contain **numbers, strings, booleans**, or mixed types
* Lists can store **variables**
* Duplicate items are allowed

---

## ⭐ Features of Lists

1. Lists can contain **duplicate elements**
2. List items are **mutable**
3. Lists can store **multiple values**
4. Lists maintain **insertion order**
5. Lists are indexed

---

## 🔍 Accessing Elements of a List

### 1️⃣ One-Dimensional List

A list where elements are stored one after another.

Each element is assigned an **index number**, starting from `0`.

```python
fruits = ["apple", "banana", "orange"]
print(fruits[0])   # apple
print(fruits[2])   # orange
```

---

### 2️⃣ Negative Indexing

Negative indexing is used to access elements **from the end of the list**.

```python
print(fruits[-1])  # orange
print(fruits[-2])  # banana
```

---

### 3️⃣ Multi-Dimensional List

A list that contains **another list** is called a multi-dimensional list.

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

print(matrix[0][1])  # 2
```

---

## 🧠 Important Notes

* Indexing always starts from `0`
* Accessing an invalid index will cause an **IndexError**
* Lists are one of the most commonly used data structures in Python

---

## ✅ Day 6 Summary

✔ Learned what lists are
✔ Created lists with same and different data types
✔ Understood list features
✔ Accessed list elements using indexing
✔ Learned negative and multi-dimensional indexing

---

📅 **Progress:** Day 6 / 90
🔥 **Status:** Completed

```

