# 🛡️ Day 2 – Network Topologies & Network Models (Cybersecurity)

This document contains **cleaned, corrected, and structured notes** for **Day 2 of Cybersecurity learning**.

Focus:

* Network Topologies
* OSI Model
* TCP/IP Model
* Network architectures

---

## 🌐 Network Topologies

A **network topology** defines how computers and devices are **physically or logically connected** in a network.

### 1️⃣ Bus Topology

* All devices are connected using a **single backbone cable**
* Data is broadcast to all devices

**Disadvantages:**

* If the backbone cable fails, the **entire network goes down**
* Only one device can transmit at a time
* Poor scalability

---

### 2️⃣ Ring Topology

* Devices are connected in a **circular (ring) structure**
* Data flows in one direction (usually)

**Disadvantages:**

* Failure of one cable or node can **break the entire network**
* Data passes through unnecessary nodes (latency)

---

### 3️⃣ Star Topology

* All devices connect to a **central device** (hub/switch)

**Advantages:**

* Easy to manage and troubleshoot

**Disadvantages:**

* If the central device fails, **all connected systems fail**

---

### 4️⃣ Tree Topology

* Combination of **Star and Bus** topologies
* Hierarchical structure

**Use Case:**

* Large organizations

---

### 5️⃣ Mesh Topology

* Every device connects to **every other device**

**Advantages:**

* High redundancy and reliability

**Disadvantages:**

* Very expensive
* Poor scalability

---

## 🏗️ Network Models

Network models define **how data is prepared, transmitted, and received** across networks.

---

## 🧱 OSI Model (7 Layers)

The **OSI (Open Systems Interconnection) Model** is a conceptual framework that explains **how data moves through a network**.

### Data Flow Concept:

```
Request → Data Preparation → Transmission → Response
```

### OSI Layers (Top to Bottom)

1. Application
2. Presentation
3. Session
4. Transport
5. Network
6. Data Link
7. Physical

---

### 🧑‍💻 Application Layer

* Implemented in software
* Direct interaction with users
* Examples: HTTP, FTP, SMTP

---

### 🎨 Presentation Layer

* Translates data formats
* Handles:

  * Encoding / decoding
  * Compression
  * Encryption

---

### 🔗 Session Layer

* Establishes, manages, and terminates sessions
* Controls communication synchronization

---

### 🚚 Transport Layer

Ensures reliable data transfer.

**Functions:**

1. **Segmentation** – Divides data and assigns port & sequence numbers
2. **Flow Control** – Controls data transmission rate
3. **Error Control** – Detects and retransmits lost/corrupted data

Protocols: TCP, UDP

---

### 🌍 Network Layer

* Handles data transfer between **different networks**
* Router operates at this layer

**Functions:**

* Logical addressing (IP addresses)
* Packet routing

---

### 🔌 Data Link Layer

* Enables communication between **directly connected nodes**
* Converts packets into frames

**Addressing Types:**

* Logical Addressing (IP)
* Physical Addressing (MAC)

---

### ⚡ Physical Layer

* Concerned with hardware transmission
* Transmits raw bits (0s and 1s)
* Uses electrical, optical, or radio signals

---

## 🌐 TCP/IP Model

Also known as the **Internet Protocol Suite**.

### Layers:

1. Application
2. Transport
3. Internet (Network)
4. Network Access (Data Link + Physical)

> OSI layers are **merged** in TCP/IP for practical implementation.

---

### Application Layer (TCP/IP)

* User interaction
* Client–server communication
* Protocols: HTTP, HTTPS, FTP, DNS

Example:

```bash
ping google.com
```

This command resolves the domain to an IP address of the nearest Google server.

---

## 🔄 Peer-to-Peer (P2P) Architecture

* Devices communicate **directly** with each other
* No dedicated server
* Decentralized architecture

**Examples:**

* File sharing networks
* Blockchain-based systems

---

## ✅ Day 2 Summary

✔ Learned network topologies
✔ Understood OSI layers and functions
✔ Compared OSI vs TCP/IP models
✔ Explored peer-to-peer architecture

---
🧠 *Understanding network models helps analyze both attacks and defenses.*
