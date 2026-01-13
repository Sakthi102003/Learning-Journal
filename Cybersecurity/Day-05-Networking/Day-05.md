# 🛡️ Day 5 – UDP, TCP, Network Layer & IP Address (TCP/IP)

This document contains **refined, corrected, and structured notes** for **Day 5 of Cybersecurity learning**.

Focus:

* UDP vs TCP
* Three-Way Handshake
* Network Layer concepts
* IP addressing & subnetting basics

---

## 🚀 User Datagram Protocol (UDP)

**UDP (User Datagram Protocol)** is a **connectionless transport-layer protocol** used to send messages between hosts over an IP network **without prior connection setup**.

### Characteristics

* No guarantee of delivery
* Data may arrive **out of order**
* No retransmission mechanism
* Low latency

UDP uses **checksums** to detect data corruption but does not correct errors.

---

### UDP Packet Structure

A UDP packet (datagram) contains:

1. Source Port (2 bytes)
2. Destination Port (2 bytes)
3. Length (2 bytes)
4. Checksum (2 bytes)

> The complete UDP packet is called a **datagram**.

---

### UDP Use Cases

* Real-time video/audio calls
* Online gaming
* DNS queries
* Live streaming

Speed is preferred over reliability in these cases.

---

## 🔒 Transmission Control Protocol (TCP)

**TCP (Transmission Control Protocol)** is a **connection-oriented transport-layer protocol** that works alongside IP. Together they form the **TCP/IP protocol suite**.

### Key Responsibilities

* Segmentation of data
* Reliable delivery
* Error detection & retransmission
* Congestion control
* Ordered data delivery using sequence numbers

---

### TCP Features

* Connection-oriented
* Full-duplex communication
* Flow control
* Error control

TCP ensures data integrity even in unreliable networks.

---

## 🤝 Three-Way Handshake (TCP)

The **Three-Way Handshake** is used by TCP to establish a **reliable connection** between a client and a server before data transfer begins.

### Handshake Steps

```
Client                      Server
  | -------- SYN --------> |
  | <----- SYN + ACK ----- |
  | -------- ACK --------> |
```

### Explanation

1. **SYN** – Client requests a connection
2. **SYN-ACK** – Server acknowledges and agrees
3. **ACK** – Client confirms; connection established

This process synchronizes sequence numbers on both sides.

---

## 🌐 Network Layer

The **Network Layer** is responsible for **routing packets across different networks**.

### Functions

* Logical addressing (IP addresses)
* Routing & forwarding
* Path selection

Routers operate at this layer.

---

### Routing Concepts

* **Hop-by-Hop Forwarding** – Packets are forwarded from one router to the next
* **Routing Table** – Stores destination networks and next-hop information
* **Forwarding Table** – Used for fast packet forwarding

---

## 🧠 Control Plane

* Responsible for **building and updating routing tables**
* Determines the best path for data packets

---

## 🧭 Routers

Routers act as **nodes** in a network graph, where:

* Nodes = routers
* Edges = links between routers

### Types of Routing

1. **Static Routing**

   * Manually configured
   * Time-consuming

2. **Dynamic Routing**

   * Automatically adapts to network changes
   * Uses routing protocols

---

## 🆔 IP Addressing

An **IP address** uniquely identifies a device on a network.

### IPv4

* 32-bit address
* Written in dotted decimal format

### IPv6

* 128-bit address
* Designed to overcome IPv4 exhaustion

---

### IPv4 Address Classes

| Class | Range                       | Purpose         |
| ----- | --------------------------- | --------------- |
| A     | 0.0.0.0 – 127.255.255.255   | Large networks  |
| B     | 128.0.0.0 – 191.255.255.255 | Medium networks |
| C     | 192.0.0.0 – 223.255.255.255 | Small networks  |
| D     | 224.0.0.0 – 239.255.255.255 | Multicast       |
| E     | 240.0.0.0 – 255.255.255.255 | Experimental    |

---

### Subnet Mask

A **subnet mask** separates:

* Network portion
* Host portion

**Variable Length Subnet Masking (VLSM)** allows flexible subnet sizes based on requirements.

---

### Reserved & Loopback Addresses

* **Reserved Range:** `127.0.0.0/8`
* **Loopback Address:** `127.0.0.1`

Used for local system testing.

---

## ✅ Day 5 Summary

✔ Understood UDP vs TCP differences
✔ Learned TCP reliability mechanisms
✔ Visualized the three-way handshake
✔ Explored routing and IP addressing basics

---

🧠 *Transport layer decides reliability; Network layer decides direction.*
