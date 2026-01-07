# 🛡️ Day 3 – Networking Devices & Network Protocols (Cybersecurity)

This document contains **refined, corrected, and structured notes** for **Day 3 of cybersecurity learning**.

Focus:

* Networking devices
* Network & application protocols
* HTTP fundamentals
* Email communication

---

## 🔌 Networking Devices

Networking devices help in **transmitting, filtering, and routing data** across networks.

---

### 1️⃣ Repeater

* Operates at the **Physical Layer**
* Regenerates and amplifies signals before they become weak
* Used to extend the length of a network
* Typically a **two-port device**

---

### 2️⃣ Hub

* Acts as a **multiport repeater**
* Commonly used in **star topology**
* Broadcasts data to all connected devices

**Types of Hubs:**

* **Active Hub** – Has its own power supply
* **Passive Hub** – No power supply; relies on active hub

---

### 3️⃣ Bridge

* Operates at the **Data Link Layer**
* Filters traffic using **MAC addresses**

**Types of Bridges:**

* **Transparent Bridge** – Devices are unaware of the bridge
* **Source Routing Bridge** – Source device decides the routing path

---

### 4️⃣ Switch

* A **multiport bridge** with buffering capability
* Operates at the **Data Link Layer**
* Improves network performance by reducing collisions

---

### 5️⃣ Router

* Operates at the **Network Layer**
* Routes data packets based on **IP addresses**
* Connects different networks

---

### 6️⃣ Gateway

* Connects **different networks using different protocols or architectures**
* Acts as an entry/exit point between networks

---

### 7️⃣ Brouter

* Combination of **Bridge + Router**
* Performs routing for routable protocols
* Bridges non-routable traffic

---

## 🌐 Network & Application Protocols

Protocols define **rules for communication** between devices.

### Common Protocols:

* **TCP/IP** – Core Internet protocol suite
* **HTTP / HTTPS** – Web communication
* **FTP** – File transfer
* **SMTP** – Sending emails
* **POP3 / IMAP** – Receiving emails
* **SSH** – Secure remote login
* **Telnet** – Remote terminal access (port 23, insecure)
* **UDP** – Connectionless transport protocol
* **VNC** – Graphical remote desktop access
* **DHCP** – Automatic IP address assignment

---

## 🧵 Process vs Thread

* **Process**: A running instance of an application
* **Thread**: Lightweight unit within a process

**Example:**

* WhatsApp application = process
* Sending messages / recording video simultaneously = multiple threads

---

## 🔌 Sockets & Ephemeral Ports

### Sockets

* Software interface between a process and the network
* Enables communication between applications

### Ephemeral Ports

* Temporary ports assigned on the **client side**
* Used when multiple instances of applications are running
* Typically chosen dynamically by the OS

---

## 🌍 HTTP (Hypertext Transfer Protocol)

* Client–server communication protocol
* Defines how clients request data and servers respond
* Runs on top of **TCP**
* **Stateless** protocol

---

### HTTP Methods

| Method | Purpose                                 |
| ------ | --------------------------------------- |
| GET    | Retrieve data                           |
| POST   | Submit data (e.g., login, registration) |
| PUT    | Update or replace data                  |
| DELETE | Remove data                             |

---

### HTTP Status Codes

Status codes indicate the result of a request.

**Common Codes:**

* **200** – Success
* **400** – Bad request
* **404** – Resource not found
* **500** – Internal server error

**Categories:**

* **1xx** – Informational
* **2xx** – Success
* **3xx** – Redirection
* **4xx** – Client errors
* **5xx** – Server errors

---

## 🍪 Cookies

* Small pieces of data stored in the browser
* Used to maintain session state
* Stored as **key–value pairs**
* Have expiration times

**Security Note:**

* Cookies can be misused for tracking
* **Third-party cookies** are set by domains the user did not directly visit

---

## 📧 How Email Works

### Email Protocols

* **SMTP** – Sending emails
* **POP3 / IMAP** – Receiving emails
* Uses **TCP** at the transport layer

### Email Flow (Simplified)

* Sender sends email to SMTP server
* SMTP server forwards to receiver’s mail server
* If receiver server is offline, sender retries for a limited period

---

### POP3 vs IMAP

**POP3:**

* Downloads emails to a single device
* Sent items & drafts are not synced

**IMAP:**

* Emails stored on server
* Allows access from multiple devices
* Preferred in modern systems

---

## ✅ Day 3 Summary

✔ Understood networking devices and their layers
✔ Learned common network and application protocols
✔ Explored HTTP methods, status codes, and cookies
✔ Understood email communication protocols

---

🧠 *Knowing devices and protocols is essential for both attacking and defending networks.*
