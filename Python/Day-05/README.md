# Day 5 – Python Basics (Part 5) 🐍

## ⛔ Loop Control Statements: `break` and `continue`

Loop control statements are used to **change the normal flow of loops**.

### 🔴 `break`
- Used to **immediately terminate** the loop
- Control exits the loop completely

### 🔵 `continue`
- Used to **skip the current iteration**
- Control moves to the next iteration of the loop

---

## 🔁 Nested Loops
A **nested loop** is a loop inside another loop.

- The **outer loop** runs first
- For each iteration of the outer loop, the **inner loop** runs completely

---

## 🔂 Nested `for` Loop
A `for` loop inside another `for` loop.

```python
for i in range(3):
    for j in range(2):
        print(i, j)
````

---

## 🔄 Nested `while` Loop

A `while` loop inside another `while` loop.

```python
i = 1
while i <= 3:
    j = 1
    while j <= 2:
        print(i, j)
        j += 1
    i += 1
```

---

## 🔍 Difference Between `for` Loop and `while` Loop

| Feature         | `for` Loop                    | `while` Loop                       |
| --------------- | ----------------------------- | ---------------------------------- |
| Iteration basis | Iterates over an iterable     | Runs based on a condition          |
| Use case        | When iterations are **known** | When iterations are **unknown**    |
| Control         | Automatic increment           | Manual update required             |
| Risk            | Low risk of infinite loop     | High risk if condition not updated |
| Infinite loop   | Possible                      | Possible                           |

---

## ⚠️ Important Notes

* Always ensure loop conditions eventually become `False`
* Use `break` carefully to avoid skipping important logic
* Avoid infinite loops unless intentionally required

---

## ✅ Day 5 Summary

✔ Learned loop control using `break` and `continue`
✔ Understood nested loops and execution flow
✔ Differentiated between `for` and `while` loops
✔ Improved control over iteration logic

---

📅 **Progress:** Day 5 / 90
🔥 **Status:** Completed

```

---

