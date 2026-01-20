# Day 8 – Python Basics (Lists – Advanced Operations) 🐍

---

## 📥 Input a List Using `split()` and Loop
A list can be accepted from the user using the `split()` method along with a loop.

### Using `split()`
```python
numbers = input("Enter numbers separated by space: ").split()
````

* Returns a list of strings

### Using `split()` with Loop & Type Casting

```python
numbers = []
values = input("Enter numbers separated by space: ").split()

for value in values:
    numbers.append(int(value))
```

---

## ✏️ Changing List Items in Python

To change a list item, refer to its **index**.

```python
fruits = ["apple", "banana", "orange"]
fruits[1] = "mango"
```

---

## 🔁 Changing Multiple Items

Multiple items can be changed by assigning a **range of values**.

```python
numbers = [1, 2, 3, 4, 5]
numbers[1:4] = [20, 30, 40]
```

---

## ➕ Inserting a New Item

The `insert()` method is used to add an item at a specific index.

```python
fruits.insert(1, "grape")
```

**Syntax:**

```python
list.insert(index, item)
```

---

## ❌ Removing List Items in Python

### 1️⃣ Remove by Value – `remove()`

Removes the **specified item**.

```python
fruits.remove("apple")
```

---

### 2️⃣ Remove by Index – `pop()`

Removes the item at the **specified index**.
If no index is provided, removes the **last item**.

```python
fruits.pop(1)
fruits.pop()
```

---

### 3️⃣ Remove Using `del`

Removes the item at a **specific index** or deletes the entire list.

```python
del fruits[0]
```

---

### 4️⃣ Clear the List – `clear()`

Removes **all elements** from the list.

```python
fruits.clear()
```

---

## ⚡ List Comprehension

List comprehension provides a **shorter and cleaner syntax** for creating a new list from an existing iterable.

### Syntax

```python
new_list = [expression for item in iterable if condition]
```

> The `if` condition is **optional**

### Example

```python
even_numbers = [x for x in range(10) if x % 2 == 0]
```

---

## 🧠 Important Notes

* List indexing starts from `0`
* Be careful when removing items inside loops
* List comprehension improves **readability and performance**

---

## ✅ Day 8 Summary

✔ Took list input using `split()` and loops
✔ Modified single and multiple list items
✔ Inserted new elements using `insert()`
✔ Removed elements using `remove()`, `pop()`, `del`, and `clear()`
✔ Learned list comprehension

---

📅 **Progress:** Day 8 / 90
🔥 **Status:** Completed

```

---
```
