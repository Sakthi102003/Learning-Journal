# Day 4 – Python Basics (Part 4) 🐍

## 🧭 Control Flow Overview
Python chooses paths with conditionals and repeats actions with loops. This day strengthens decision-making and iteration concepts without showing code.

---

## 🧩 Key Terms
- **Condition** – An expression that evaluates to `True` or `False`
- **Branch** – A path of execution chosen by a condition
- **Loop** – A repeated execution of a block while a rule holds
- **Iteration** – One pass through a loop
- **Counter** – A variable that tracks progress in a loop
- **Range** – A sequence of integers used to control iteration

---

## 🔀 If / Elif / Else
- Use `if` for an initial decision
- Add `elif` for additional mutually exclusive checks
- Use `else` as a final fallback when previous checks fail
- Keep checks simple and ordered from most specific/likely to least
- Prefer clear comparisons; avoid deeply nested logic

---

## 🔁 For Loop
- Best when the number of iterations is known or you’re iterating a collection
- Works naturally with `range()` to define start, stop (exclusive), and step
- Predictable termination; lower risk of infinite loops

---

## ⏳ While Loop
- Repeat while a condition stays `True`; ideal when iteration count is unknown
- Always update the loop state to ensure progress
- Stops when the condition becomes `False`; execution continues after the loop

---

## 📏 `range()`
- `range(stop)` – counts from `0` up to `stop` (exclusive)
- `range(start, stop)` – counts from `start` up to `stop` (exclusive)
- `range(start, stop, step)` – counts by `step` (positive or negative)
- Works with integers only; `step` cannot be `0`

---

## ⚠️ Common Pitfalls
- Off‑by‑one boundaries: remember `stop` is exclusive
- Overlapping conditions: can make branches unreachable
- Infinite loops: missing or incorrect state updates in `while`
- Misused `range()`: forgetting `step` rules or negative steps

---

## ✅ Day 4 Summary
✔ Understood conditional branching (`if / elif / else`)
✔ Differentiated `for` vs `while` loop use cases
✔ Practiced iteration thinking with `range()`
✔ Identified and avoided common loop pitfalls

---

📅 **Progress:** Day 4 / 90  
🔥 **Status:** Completed

---

### 📚 See Also (Workspace Files)
- Decision making: [Python/Day-04/ifelseelif.py](Python/Day-04/ifelseelif.py)
- Looping basics: [Python/Day-04/for.py](Python/Day-04/for.py), [Python/Day-04/while.py](Python/Day-04/while.py)
- Range variants: [Python/Day-04/startstop.py](Python/Day-04/startstop.py), [Python/Day-04/startstopstep.py](Python/Day-04/startstopstep.py)
- Practice ideas: [Python/Day-04/divisibility.py](Python/Day-04/divisibility.py), [Python/Day-04/sum-of-n.py](Python/Day-04/sum-of-n.py)