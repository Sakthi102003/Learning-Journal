# 🛡️ Day 6 – Packets, IPv6, Data Link Layer, Middleboxes & Physical Layer (TCP/IP)

This document contains **refined, corrected, and structured notes** for **Day 6 of Cybersecurity learning**.

Focus:

* Packets & TTL
* IPv6 basics
* Middleboxes (firewalls, NAT)
* Data Link Layer
* Physical Layer

---

## 📦 Packets

A **packet** is a small unit of data into which a large message is divided before being sent over a network. Packets are transmitted independently and **reassembled at the destination**.

### Typical Packet Fields (IPv4)

* IP Version
* Header Length
* Total Length
* Identification
* Flags
* Protocol
* Checksum
* **TTL (Time To Live)**

Packetization improves reliability, routing efficiency, and error handling.

---

## ⏳ Time To Live (TTL)

**TTL** limits the lifespan of a packet in a network to prevent infinite looping.

* Implemented as a **hop counter**
* Decremented by 1 at each router
* Packet is discarded when TTL reaches zero

This protects networks from routing loops.

---

## 🌐 IPv6 (Internet Protocol Version 6)

IPv6 was introduced to overcome **IPv4 address exhaustion**.

### Key Points

* **128-bit address space** (much larger than IPv4)
* Written in hexadecimal
* Supports a vast number of unique addresses

> IPv6 address space is vastly larger than IPv4 (not just four times).

### Limitations

* Not backward compatible with IPv4
* Requires infrastructure and hardware upgrades by ISPs

---

## 🧱 Middleboxes

**Middleboxes** are network devices that inspect, modify, or manage packets beyond basic routing.

### 1️⃣ Firewalls

Used to separate **trusted networks** from untrusted networks (e.g., Internet).

**Firewall filtering can be based on:**

* Source/Destination IP address
* Port numbers
* Protocols
* TCP flags
* Packet state

**Types:**

* **Stateless Firewall** – Does not track connection state
* **Stateful Firewall** – Tracks active connections using state tables (more secure)

---

### 2️⃣ Network Address Translation (NAT)

**NAT** modifies IP address information in packet headers while packets are in transit.

### Purpose of NAT

* Conserves public IPv4 addresses
* Hides internal network structure
* Enables multiple devices to share a single public IP

---

## 🔗 Data Link Layer

The **Data Link Layer** is responsible for **node-to-node data delivery** within the same local network.

### Responsibilities

* Framing
* Physical (MAC) addressing
* Error detection

---

### DHCP (Dynamic Host Configuration Protocol)

* Automatically assigns IP addresses to devices
* Uses an IP address pool
* Operates at the application layer

---

### Address Resolution Protocol (ARP)

* Maps **IPv4 addresses (32-bit)** to **MAC addresses (48-bit)**
* Uses an **ARP cache** to store mappings

---

### Frames

* A **frame** is the Data Link Layer data unit
* Encapsulates an IP packet
* Contains source and destination MAC addresses

---

## ⚡ Physical Layer

The **Physical Layer** transmits raw bits over the physical medium.

### Characteristics

* Electrical, optical, or radio signals
* Includes cables, connectors, and transmission media
* Represents data as 0s and 1s

---

## ✅ Day 6 Summary

✔ Understood packet structure and TTL
✔ Learned IPv6 basics and limitations
✔ Explored middleboxes (firewalls & NAT)
✔ Understood Data Link Layer functions
✔ Learned role of the Physical Layer

---

🧠 *Packets move the data, middleboxes control it, and layers define how it travels.*
