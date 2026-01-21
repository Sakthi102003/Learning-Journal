# Day 9 – Python Basics (Dictionaries & Accessing Dictionary Items) 🐍

---

## 📘 Dictionaries
A **dictionary** is a collection of **key–value pairs**.

### Key Characteristics:
- Each key must be **unique**
- Values can be of any data type
- Dictionaries are **mutable** (values can be changed)
- Dictionaries are **unordered** (before Python 3.7; insertion-ordered after)

---

## 🛠 Dictionary Syntax
```python
student = {
    "name": "Sakthi",
    "age": 21,
    "is_student": True
}
````

## 📏 Length of a Dictionary

The `len()` function returns the **number of key–value pairs** in a dictionary.

```python
print(len(student))
```

---

## 🏗 Creating Dictionary Using `dict()` Constructor

An alternative way to create a dictionary.

### Syntax:

```python
dict_name = dict(key1=value1, key2=value2)
```

### Example:

```python
person = dict(name="User", age=23, city="Coimbatore")
```

> ⚠️ Keys must be valid identifiers (no spaces or special characters)

---

## 🔍 Accessing Dictionary Items

---

### 1️⃣ Access Value Using Key Name

```python
print(student["name"])
```

> ⚠️ Raises `KeyError` if the key does not exist

---

### 2️⃣ Access Value Using `get()` Method

```python
print(student.get("age"))
```

✔ Safer than direct access
✔ Returns `None` if key does not exist (instead of error)

---

### 3️⃣ Access All Keys – `keys()`

Returns a **view object** containing all keys.

```python
print(student.keys())
```

---

### 4️⃣ Access All Values – `values()`

Returns a **view object** containing all values.

```python
print(student.values())
```

---

### 5️⃣ Access All Items – `items()`

Returns a **view object** containing key–value pairs as tuples.

```python
print(student.items())
```

---

## 🧠 Important Notes

* Keys are usually **strings or numbers**
* Values can be **any data type**
* Dictionary view objects update dynamically
* Use `get()` to avoid runtime errors

---

## ✅ Day 9 Summary

✔ Learned what dictionaries are
✔ Created dictionaries using literals and `dict()` constructor
✔ Found dictionary length using `len()`
✔ Accessed values using keys and `get()`
✔ Retrieved keys, values, and items

---

📅 **Progress:** Day 9 / 90
🔥 **Status:** Completed

```

---
```
