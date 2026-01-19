# 🛡️ Day 7 – CIDR, Routing & Routing Protocols, NAT (Cybersecurity)

This document contains **refined, corrected, and structured notes** for **Day 7 of Cybersecurity learning**.

Focus:

* CIDR & subnetting basics
* Routing & routing protocols
* NAT and its types
* Port forwarding

---

## 📐 CIDR (Classless Inter-Domain Routing)

**CIDR** is a method for allocating IP addresses and routing IP packets more efficiently than the traditional class-based system.

### Why CIDR Exists

* Reduces the growth of routing tables
* Slows IPv4 address exhaustion
* Allows flexible subnet sizes

---

### CIDR Basics

* IPv4 address = **32 bits**
* CIDR notation: `IP_address/prefix_length`

### CIDR Calculation

Number of IP addresses in a subnet:

```
2^(32 − prefix_length)
```

**Example:**

```
11.0.0.0/24
32 − 24 = 8
2^8 = 256 IP addresses
```

> Smaller CIDR prefix → larger IP range

---

## 🧭 Routing & Routing Protocols

**Routing** is the process of selecting paths for data packets to travel across networks.

### Why Routing Is Important

* Finds optimal paths
* Minimizes delays
* Ensures scalability and reliability

---

### Types of Routing

1. **Static Routing**

   * Manually configured
   * Simple but not scalable

2. **Dynamic Routing**

   * Automatically updates routes
   * Uses routing protocols

---

## 🔁 Dynamic Routing Protocols

---

### 1️⃣ RIP (Routing Information Protocol)

* Distance-vector protocol
* Metric: hop count
* Maximum hop count: **15**

#### How RIP Works

* Routers share entire routing tables every 30 seconds
* Suitable only for small networks

#### Versions

* **RIP v1** – Classful routing (no subnetting)
* **RIP v2** – Classless routing (supports CIDR)

**Real-world Use:**

* Small offices and simple networks

---

### 2️⃣ OSPF (Open Shortest Path First)

* Link-state routing protocol
* Metric based on **cost (link speed)**
* Fast convergence

#### How OSPF Works

* Routers share link-state information
* Uses **Dijkstra’s shortest path algorithm**

#### OSPF Areas

* **Area 0** – Backbone area
* Other areas connect to Area 0 for scalability

**Real-world Use:**

* Medium to large enterprise networks

---

### 3️⃣ BGP (Border Gateway Protocol)

* Path-vector routing protocol
* Routes traffic between **Autonomous Systems (AS)**
* Core protocol of the global Internet

#### How BGP Works

* Selects routes based on policies
* Tracks AS-path, next-hop, and other attributes

#### Key Attributes

* **AS-PATH** – Prevents routing loops
* **NEXT-HOP** – Determines next router
* **MED (Multi-Exit Discriminator)** – Influences route selection

**Real-world Use:**

* ISPs, governments, and large-scale networks

---

## 📊 Comparison: RIP vs OSPF vs BGP

| Protocol | Network Size | Metric           | Use Case         |
| -------- | ------------ | ---------------- | ---------------- |
| RIP      | Small        | Hop count (≤15)  | Small offices    |
| OSPF     | Medium–Large | Cost (bandwidth) | Enterprises      |
| BGP      | Very Large   | Policy-based     | Internet routing |

---

## 🔁 Network Address Translation (NAT)

**NAT** allows multiple devices in a private network to access the Internet using a **single public IP address**.

### Benefits of NAT

* Conserves IPv4 addresses
* Hides internal network structure
* Adds a basic layer of security

---

### Types of NAT

### 1️⃣ Static NAT (SNAT)

* One-to-one mapping between private and public IP
* Mapping does not change
* Suitable for servers requiring inbound access

---

### 2️⃣ Dynamic NAT

* Maps private IPs to a pool of public IPs dynamically
* Public IP may change per session
* Also called **IP masquerading**

---

### 3️⃣ Port Address Translation (PAT)

* Multiple private hosts share one public IP
* Differentiation based on **port numbers**
* Most common NAT type used today

---

## 🔓 Port Forwarding

* Allows external users to access internal services
* Maps public IP:port → private IP:port
* Common when hosting services behind a NAT

---

## ✅ Day 7 Summary

✔ Learned CIDR and subnet calculation
✔ Understood routing and routing protocols
✔ Compared RIP, OSPF, and BGP
✔ Learned NAT types and port forwarding

---

🧠 *Routing decides the path, NAT hides the network, and CIDR makes IP allocation efficient.*
