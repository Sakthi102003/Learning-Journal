# 🛡️ Day 1 – Networking Basics (Cybersecurity)

This document contains **clean, corrected, and interview‑ready notes** for **Day 1 of Cybersecurity learning**.
Focus: **Networking Fundamentals** — the backbone of cybersecurity.

---

## 🌐 Internet – Origin & Purpose

The **Internet** originated from **ARPANET**, a research network developed by the **entity["organization","ARPA","us defense research agency"]** (Advanced Research Projects Agency) under the U.S. Department of Defense in the late 1960s.

### Purpose:

* Reliable communication during failures
* Research & military data exchange
* Later evolved into public global connectivity

> ⚠️ Internet was **not** created during World War II — it came later.

---

## 🌍 World Wide Web (WWW)

The **World Wide Web** is a system of **interlinked hypertext documents** accessed over the Internet using **HTTP/HTTPS**.

* Internet = infrastructure
* Web = service running on top of the Internet

🔗 **First website ever:**
[https://info.cern.ch/hypertext/WWW/TheProject.html](https://info.cern.ch/hypertext/WWW/TheProject.html)

> Internet ≠ Web (important interview distinction)

---

## 🖥️ Client–Server Architecture

A **client** sends a request to a **server**, and the server processes the request and sends back a response.

### Flow:

```
Client → Request → Server → Response → Client
```

* A single system can act as **both client and server** (e.g., localhost, self‑hosted apps).

---

## 📜 Protocols

**Protocols** are standardized rules that define:

* How data is formatted
* How it is transmitted
* How it is received and acknowledged

### Examples:

* **TCP** – Reliable data delivery
* **HTTP** – Web communication
* **DNS** – Domain name resolution

---

## 🔐 TCP vs HTTP

### TCP (Transmission Control Protocol)

* Reliable delivery
* Packet ordering
* Error detection & retransmission

### HTTP (Hypertext Transfer Protocol)

* Application‑layer protocol
* Used by web browsers
* Runs **on top of TCP**
* Stateless

> TCP handles reliability, HTTP handles communication logic.

---

## 🆔 IP Address

An **IP address** is a numerical identifier assigned to a device on a network using Internet Protocol.

Example (IPv4):

```
192.168.1.1
```

### Purpose:

* Identifies **network** and **host**
* Determines where data should be sent

### Check public IP:

```bash
curl ifconfig.me
```

---

## 🚪 Ports

A **port** is a **16‑bit number** that identifies a specific service running on a device.

### Port Ranges:

* **0–1023** → Well‑known / Reserved ports
* **1024–49151** → Registered ports
* **49152–65535** → Dynamic / Ephemeral ports

### Common Ports:

* HTTP → 80
* HTTPS → 443
* SSH → 22

> IP decides **which device**, port decides **which application**.

---

## 📶 Bandwidth Units

Networking uses **decimal values**:

* 1 kbps = 1,000 bits/sec
* 1 Mbps = 1,000,000 bits/sec
* 1 Gbps = 1,000,000,000 bits/sec (10⁹)

---

## 🏠 Area Networks

### Types:

1. **LAN (Local Area Network)** – Homes, offices (Ethernet, Wi‑Fi)
2. **MAN (Metropolitan Area Network)** – City‑wide interconnection of LANs
3. **WAN (Wide Area Network)** – Country/global networks using fiber

🌐 The Internet is a **global interconnection of LANs via WANs**.

---

## 🔌 Networking Technologies

### Optical Networking:

* **SONET** – High‑speed optical transmission over long distances

### WAN Technologies:

* **Frame Relay** – Packet‑switched WAN technology (legacy)

---

## 📡 Networking Devices

### Modem

* Converts **digital ↔ analog signals**
* Used by ISPs

### Router

* Routes data based on **IP addresses**
* Operates at **Network Layer (Layer 3)**

---

## ✅ Day 1 Summary

✔ Understood Internet vs Web
✔ Learned client–server communication
✔ Identified role of protocols, IPs, and ports
✔ Built solid networking foundation

---

📌 **Next:** Day 2 – TCP vs UDP & Packet Flow

> *Strong networking knowledge = strong cybersecurity mindset.*
