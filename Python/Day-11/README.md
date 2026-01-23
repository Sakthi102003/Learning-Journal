# Day 11 – Python Basics (Tuples) 🐍

---

## 📦 Tuples
A **tuple** is a collection of items that is:

- **Ordered**
- **Indexed**
- **Immutable** (cannot be changed after creation)

Tuples are used when data should **not be modified**.

---

## 🛠 Tuple Syntax
```python
tuple_name = (item1, item2, item3)
````

---

## 1️⃣ Tuple with One Item

To create a tuple with a single item, a **comma is mandatory**.

```python
single_item = ("Python",)
```

> Without the comma, Python treats it as a string, not a tuple.

---

## 📏 Length of a Tuple

The `len()` function returns the number of elements in a tuple.

```python
print(len(tuple_name))
```

---

## 🏗 Tuple Constructor

An alternative way to create a tuple using the `tuple()` constructor.

```python
numbers = tuple([1, 2, 3])
```

---

## 🔍 Accessing Tuple Items

---

### 1️⃣ Positive Indexing

Each item in a tuple can be accessed using its **index number** (starting from `0`).

```python
fruits = ("apple", "banana", "orange")
print(fruits[1])   # banana
```

⚠️ Accessing an invalid index raises an `IndexError`
⚠️ Using non-integer index raises a `TypeError`

---

### 2️⃣ Negative Indexing

Negative indexing starts from the **end of the tuple**.

* `-1` → last item
* `-2` → second last item

```python
print(fruits[-1])  # orange
```

---

### 3️⃣ Tuple Slicing

Slicing allows access to a **range of items**.

```python
print(fruits[0:2])   # ('apple', 'banana')
```

**Syntax:**

```python
tuple_name[start_index : end_index]
```

> End index is **exclusive**

---

## 🧠 Important Notes

* Tuples cannot be modified after creation
* Faster than lists in read-only operations
* Can contain duplicate values
* Can store mixed data types

---

## ✅ Day 11 Summary

✔ Learned what tuples are
✔ Created tuples with multiple and single items
✔ Found tuple length
✔ Accessed tuple elements using indexing
✔ Used slicing on tuples

---

📅 **Progress:** Day 11 / 90
🔥 **Status:** Completed

```

---
```
