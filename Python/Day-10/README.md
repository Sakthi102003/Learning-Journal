# Day 10 – Python Basics  
### Changing, Adding, Removing & Copying Dictionaries 🐍

---

## ✏️ Changing & Adding Dictionary Items

### 1️⃣ Change Value Using Key Name
```python
student["age"] = 22
````

**Syntax:**

```python
dict_name[key] = value
```

---

### 2️⃣ Change Value Using `update()` Method

```python
student.update({"age": 23})
```

**Syntax:**

```python
dict_name.update(dictionary)
```

---

### 3️⃣ Add New Item Using Key Name

```python
student["city"] = "Coimbatore"
```

**Syntax:**

```python
dict_name[new_key] = new_value
```

---

### 4️⃣ Add New Item Using `update()` Method

```python
student.update({"course": "Python"})
```

---

## ❌ Removing Dictionary Items

---

### 1️⃣ Remove Item Using `pop()`

Removes an item using its **key** and returns the removed value.

```python
age = student.pop("age")
```

**Syntax:**

```python
dict_name.pop(key)
```

---

### 2️⃣ Remove Last Item Using `popitem()`

Removes the **last inserted item** and returns it as a **tuple**.

```python
item = student.popitem()
```

---

### 3️⃣ Remove Item Using `del`

```python
del student["city"]
```

---

### 4️⃣ Delete Entire Dictionary Using `del`

```python
del student
```

> ⚠️ Dictionary will no longer exist after this

---

### 5️⃣ Empty Dictionary Using `clear()`

Removes all items but keeps the dictionary object.

```python
student.clear()
```

---

## 📋 Copying a Dictionary

Copying is important to avoid **unexpected changes** when working with dictionaries.

> ❌ Assignment (`=`) does NOT create a copy — it creates a reference

---

### 1️⃣ Copy Using `copy()` Method

```python
dict2 = dict1.copy()
```

---

### 2️⃣ Copy Using `dict()` Constructor

```python
dict2 = dict(dict1)
```

---

## 🧠 Important Notes

* `update()` can be used to **add or modify** items
* `pop()` needs a key; `popitem()` removes the last item
* `clear()` empties dictionary but keeps it usable
* Always copy dictionaries when working with multiple references

---

## ✅ Day 10 Summary

✔ Changed dictionary values
✔ Added new key–value pairs
✔ Removed dictionary items safely
✔ Deleted and cleared dictionaries
✔ Copied dictionaries correctly

---

📅 **Progress:** Day 10 / 90
🔥 **Status:** Completed

```

---

```
