
# 🌐 How IP Address Calculation Works

This README explains **how an IP address is calculated**, focusing mainly on **IPv4**, subnet masks, CIDR notation, and how networks and hosts are derived.

---

## 📌 What is an IP Address?

An **IP (Internet Protocol) address** is a unique identifier assigned to a device on a network.

### IPv4 Format
```

192.168.1.10

```
- Total size: **32 bits**
- Divided into **4 octets**
- Each octet = **8 bits**
- Range per octet: **0 – 255**

Binary example:
```

192 = 11000000
168 = 10101000
1   = 00000001
10  = 00001010

```

---

## 🧮 Binary Calculation Basics

Each octet uses the following bit values:

| Bit Position | Value |
|--------------|-------|
| 1 | 128 |
| 2 | 64 |
| 3 | 32 |
| 4 | 16 |
| 5 | 8 |
| 6 | 4 |
| 7 | 2 |
| 8 | 1 |

Example:
```

11000000 = 128 + 64 = 192

```

---

## 🎭 Classes of IP Addresses (Legacy)

| Class | Range | Default Subnet |
|------|------|---------------|
| A | 1 – 126 | 255.0.0.0 |
| B | 128 – 191 | 255.255.0.0 |
| C | 192 – 223 | 255.255.255.0 |

⚠️ **Note:** Classes are mostly outdated but still useful for learning fundamentals.

---

## 🪙 Subnet Mask Explained

A **subnet mask** separates:
- **Network portion**
- **Host portion**

Example:
```

IP Address   : 192.168.1.10
Subnet Mask  : 255.255.255.0

```

Binary:
```

IP     : 11000000.10101000.00000001.00001010
Mask   : 11111111.11111111.11111111.00000000

```

- `1` → Network bits
- `0` → Host bits

---

## 🔢 CIDR Notation

CIDR shows **how many bits are used for the network**.

Example:
```

192.168.1.10/24

```
- `/24` → 24 network bits
- Remaining bits → host bits

---

## 🧠 How to Calculate Network Address

### Formula
```

Network Address = IP Address AND Subnet Mask

```

Example:
```

IP    : 192.168.1.10
Mask  : 255.255.255.0

```

Result:
```

Network Address = 192.168.1.0

```

---

## 📦 How to Calculate Number of Hosts

### Formula
```

Hosts = 2^(number of host bits) - 2

```

Example (`/24`):
```

Host bits = 8
Hosts = 2^8 - 2 = 254

```

- `-2` removes:
  - Network address
  - Broadcast address

---

## 📢 Broadcast Address Calculation

Broadcast address =  
All **host bits set to 1**

Example:
```

Network: 192.168.1.0/24
Broadcast: 192.168.1.255

```

---

## 🧪 Example Summary

| Item | Value |
|----|------|
| IP Address | 192.168.1.10 |
| Subnet Mask | 255.255.255.0 |
| CIDR | /24 |
| Network Address | 192.168.1.0 |
| Broadcast Address | 192.168.1.255 |
| Usable Hosts | 254 |

---

## ✅ Why This Matters

IP calculation is essential for:
- Networking fundamentals
- Cybersecurity
- Ethical hacking
- Network design
- Cloud & DevOps

---

## 🔚 Conclusion

IP calculation is all about:
- Binary math
- Understanding subnet masks
- Knowing how networks and hosts are divided

Once you master this, networking stops being scary and starts making sense 😎

---

### 🛠️ Future Improvements
- Add IPv6 calculation
- Add subnetting practice problems
- Add Python script for IP calculation

```
