# 🛡️ Day 4 – DNS & Transport Layer (TCP/IP)

This document contains **refined, corrected, and structured notes** for **Day 4 of Cybersecurity learning**.

Focus:

* Domain Name System (DNS)
* TCP/IP Transport Layer concepts

---

## 🌐 Domain Name System (DNS)

The **Domain Name System (DNS)** acts as the **phonebook of the Internet**, translating human-readable domain names into machine-readable IP addresses.

### Purpose of DNS

* Maps domain names (e.g., `google.com`) to IP addresses
* Enables browsers to locate and connect to servers

---

### Domain Structure

Example: `mail.google.com`

* **mail** → Subdomain
* **google** → Second-level domain
* **.com** → Top-level domain (TLD)

### Top-Level Domains (TLDs)

* Common TLDs: `.com`, `.org`, `.net`, `.io`
* Managed at the root level of DNS hierarchy

Root DNS infrastructure is coordinated by **entity["organization","ICANN","internet domain authority"]**.

Information about root servers can be viewed at:
[https://root-servers.org](https://root-servers.org)

---

### DNS Resolution Process

When a user types a website URL in the browser:

1. Browser checks **local cache** on the system
2. Query goes to **Local DNS Resolver** (usually ISP)
3. Resolver contacts **Root DNS Server**
4. Root server directs to **TLD server**
5. TLD server points to **Authoritative DNS Server**
6. IP address is returned to the browser

This process allows fast and reliable domain resolution.

---

### DNS Tools

```bash
dig google.com
```

* `dig` (Domain Information Groper) is a DNS lookup utility
* Used to query DNS servers directly
* Displays detailed DNS response data

---

## 🚚 TCP/IP – Transport Layer

The **Transport Layer** ensures **end-to-end communication** between applications running on different hosts.

It works **above the Network Layer** and is responsible for delivering data to the correct application using port numbers.

---

### Key Transport Layer Concepts

#### 🔀 Multiplexing & Demultiplexing

* **Multiplexing**: Multiple applications send data simultaneously over a single network interface
* **Demultiplexing**: Transport layer delivers received data to the correct application using port numbers

---

#### 📦 Data Transmission

* Data is sent in the form of **segments**
* Each segment contains:

  * Source port
  * Destination port
  * Sequence number

---

#### 🚦 Congestion Control

* Prevents network overload
* Implemented in **TCP** using built-in congestion control algorithms
* Adjusts transmission rate based on network conditions

---

#### 🧮 Checksums

* Small data value derived from the original data
* Used to detect errors during transmission
* If checksum mismatch occurs, data is retransmitted

---

#### ⏱️ Timers

* Sender starts a timer when data is transmitted
* If acknowledgment is not received within a time limit, data is retransmitted

---

#### 🔢 Sequence Numbers

* Ensures data is reassembled in the correct order
* Detects duplicate packets
* Critical for reliable communication

---

## ✅ Day 4 Summary

✔ Understood DNS hierarchy and resolution process
✔ Learned the role of ICANN and root servers
✔ Explored transport layer responsibilities
✔ Understood multiplexing, congestion control, and reliability mechanisms

---

🧠 *DNS tells you **where** to go. Transport layer ensures **how** data gets there safely.*
