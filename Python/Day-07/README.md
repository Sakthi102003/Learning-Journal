# Day 7 – Python Basics  
### Adding Elements to List, `input()` Method, Input a List Using Loops 🐍

---

## ➕ Adding Elements to a List
Elements can be added to a list in multiple ways using built-in methods.

---

### 1️⃣ `append()`
The `append()` method is used to add **one item at the end** of a list.

```python
numbers = [1, 2, 3]
numbers.append(4)
````

**Key Points:**

* Adds only **one element at a time**
* Can add **duplicate values**
* Can add a **list as a single element**

```python
numbers.append([5, 6])
```

---

### 2️⃣ `insert()`

The `insert()` method is used to add an element at a **specific position**.

```python
numbers.insert(1, 10)
```

**Syntax:**

```python
list.insert(position, value)
```

---

### 3️⃣ `extend()`

The `extend()` method is used to add **all elements of one list** to another list.

```python
list1 = [1, 2]
list2 = [3, 4]
list1.extend(list2)
```

**Syntax:**

```python
list1.extend(list2)
```

---

## ⌨️ `input()` Method in Python

The `input()` function is used to take input from the user.

* The value returned by `input()` is **always a string**
* A message can be displayed inside `input()`

```python
name = input("Enter your name: ")
```

---

## 🔁 Type Casting User Input

Since `input()` returns a string, **type casting** is required for numerical operations.

```python
age = int(input("Enter your age: "))
```

---

## 📋 Input a List Using Loops

A common issue with `input()` is that it returns a **single string**, not a list.

To accept multiple values, loops or string methods are used.

---

### 🔄 Input a List Using a Loop

```python
numbers = []
n = int(input("How many elements? "))

for i in range(n):
    value = int(input("Enter value: "))
    numbers.append(value)
```

---

## ✂️ Input a List Using `split()`

The `split()` method is used to divide a string into a list of substrings.

**Syntax:**

```python
string.split(separator, maxsplit)
```

### Example:

```python
numbers = list(map(int, input("Enter numbers separated by space: ").split()))
```

**Why `split()` is useful:**

* Faster input
* Cleaner code
* Ideal for competitive programming and real-world scripts

---

## 🧠 Important Notes

* `append()` adds **one element**
* `extend()` adds **multiple elements**
* `insert()` gives position control
* `split()` simplifies list input

---

## ✅ Day 7 Summary

✔ Added elements to a list using `append()`, `insert()`, and `extend()`
✔ Understood how `input()` works
✔ Learned type casting of user input
✔ Took list input using loops and `split()` method

---

📅 **Progress:** Day 7 / 90
🔥 **Status:** Completed

```

---

### Mentor advice (this matters 🧠)
By Day 7, you should comfortably:
- Build a list **from user input**
- Know when to use `append()` vs `extend()`
- Avoid the classic mistake:  
  👉 `numbers = input()` (this is **not** a list 😅)

