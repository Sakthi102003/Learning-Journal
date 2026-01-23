# 🐧 Day 11 – Linux File Permissions & Ownership (Cybersecurity)

This document contains **refined, corrected, and security-focused notes** for **Day 11 of Linux learning**, covering **file permissions and ownership**, which are critical for cybersecurity.

Focus:

* Linux permission model
* chmod (symbolic & numeric)
* Recursive permissions
* File ownership (chown)

---

## 🔐 Linux File Permission Model

A typical Linux permission string looks like:

```
drwxrwxrwx
```

### Permission Breakdown

| Position | Meaning                            |
| -------- | ---------------------------------- |
| `d`      | Directory (`-` means regular file) |
| `r`      | Read permission                    |
| `w`      | Write permission                   |
| `x`      | Execute permission                 |

> ⚠️ Note: `d` means **directory**, not DNS.

---

### Permission Groups

```
drwxrwxrwx
 ||| ||| |||
  |   |   └── Others
  |   └────── Group
  └────────── User (Owner)
```

* **User (owner)** – File creator/owner
* **Group** – Group assigned to file
* **Others** – Everyone else

---

## 🧩 Permission Meanings

| Permission | Meaning                                        |
| ---------- | ---------------------------------------------- |
| `r`        | Read file / list directory                     |
| `w`        | Modify file / create-delete files in directory |
| `x`        | Execute file / enter directory                 |

If **execute (`x`) is missing**, a file **cannot be run**, even if read permission exists.

---

## 🛠️ chmod – Change File Permissions

### Symbolic Mode

```bash
chmod +x filename
```

* Adds execute permission for all users
* Executable files often appear **green** in terminal

```bash
chmod u-x filename
```

* Removes execute permission from **user (owner)**

```bash
chmod u+x filename
```

* Adds execute permission only for the user

Other symbols:

* `u` → user
* `g` → group
* `o` → others
* `a` → all

---

### Numeric (Octal) Mode

Each permission has a numeric value:

* Read (`r`) = **4**
* Write (`w`) = **2**
* Execute (`x`) = **1**

### Example

```bash
chmod 770 filename
```

| Value | Permissions |
| ----- | ----------- |
| 7     | rwx         |
| 7     | rwx         |
| 0     | ---         |

Meaning:

* User → full permissions
* Group → full permissions
* Others → no access

---

## 🔁 Recursive Permissions

```bash
chmod -R 755 directory/
```

* `-R` applies permission changes to **all files and subdirectories**
* Use carefully — recursive permissions can break systems

---

## 👤 chown – Change Ownership

```bash
chown user filename
```

Changes file owner.

```bash
sudo chown -R user2 folder/
```

* Recursively changes ownership of folder
* Requires `sudo`

Ownership control is critical for **privilege separation and system security**.

---

## 🛡️ Security Perspective

Many real-world vulnerabilities occur due to:

* Over-permissive files (`777`)
* Wrong ownership
* Executable permission on untrusted files

Understanding permissions is essential for **hardening systems and detecting misconfigurations**.

---

## ✅ Day 11 Summary

✔ Understood Linux permission structure
✔ Learned symbolic and numeric chmod usage
✔ Used recursive permission changes
✔ Managed file ownership with chown

---

🧠 *Permissions decide who can read, write, execute — and who can break the system.*
