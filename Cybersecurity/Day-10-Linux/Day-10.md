# 🐧 Day 10 – Essential Linux Commands (Cybersecurity)

This document contains a **clean, organized, and security-focused reference** of essential Linux commands learned on **Day 10**.

Focus:

* File & directory operations
* User and permission management
* Package management
* Networking & system monitoring
* Helpful utilities for daily Linux usage

---

## 🔐 Remote Access

### SSH

```bash
ssh user@server
```

Connects to a remote Linux machine securely using SSH.

---

## 📁 File & Directory Navigation

### ls

```bash
ls
ls -l
ls -a
```

Lists files and directories (long view, hidden files).

### pwd

```bash
pwd
```

Prints the current working directory.

### cd

```bash
cd path
cd ..
cd ~
```

Changes the current directory.

---

## 📄 File Operations

### touch

```bash
touch filename
```

Creates an empty file or updates timestamps.

### echo

```bash
echo "text" > file
```

Prints text or writes it to a file.

### cat

```bash
cat filename
```

Displays file content.

### less

```bash
less filename
```

Views file content page by page.

### head / tail

```bash
head filename
tail filename
```

Shows first or last lines of a file.

---

## ✏️ Text Editors

### nano

```bash
nano filename
```

Simple terminal-based text editor.

### vim

```bash
vim filename
```

Advanced text editor for power users.

---

## 🗂️ File & Directory Management

### mkdir

```bash
mkdir directoryname
```

Creates a directory.

### cp

```bash
cp file destination
```

Copies files or directories.

### mv

```bash
mv file destination
```

Moves or renames files.

### rm

```bash
rm file
rm -r directory
```

Deletes files or directories (use with caution).

### ln

```bash
ln -s file link
```

Creates a symbolic link.

### shred

```bash
shred filename
```

Overwrites a file to make recovery difficult.

---

## 👤 User & Permission Management

### whoami

```bash
whoami
```

Shows current user.

### adduser

```bash
sudo adduser username
```

Adds a new user.

### passwd

```bash
passwd username
```

Changes a user password.

### su

```bash
su username
```

Switches user.

### sudo

```bash
sudo command
```

Runs command with superuser privileges.

### chmod

```bash
chmod +x filename
```

Changes file permissions.

### chown

```bash
chown user filename
```

Changes file owner.

---

## 📦 Package Management (Debian-based)

### apt

```bash
sudo apt update
sudo apt install package
```

Manages package installation and updates.

---

## 📖 Help & Discovery

### man

```bash
man command
```

Displays manual pages.

### whatis

```bash
whatis command
```

Shows a brief description of a command.

### which

```bash
which command
```

Displays the path of an executable.

---

## 🌐 Networking Commands

### ifconfig

```bash
ifconfig
```

Displays network interface information (legacy).

### ip

```bash
ip address
```

Modern tool to view and manage network interfaces.

### ping

```bash
ping hostname
```

Checks host reachability.

### traceroute

```bash
traceroute hostname
```

Displays packet path to destination.

### netstat

```bash
netstat -tulpen
```

Shows network connections and listening ports.

### ss

```bash
ss -tulpen
```

Modern replacement for netstat.

### resolveconf

```bash
resolveconf status
```

Displays DNS resolver status.

---

## 🔥 Firewall Management

### ufw

```bash
ufw allow port
ufw status
ufw enable
```

Manages firewall rules using Uncomplicated Firewall.

---

## 📊 System Monitoring & Info

### uname

```bash
uname
uname -a
```

Displays system information.

### neofetch

```bash
neofetch
```

Shows system information visually.

### free

```bash
free
```

Displays memory usage.

### df

```bash
df -h
```

Shows disk usage.

### ps

```bash
ps aux
```

Displays running processes.

### top

```bash
top
```

Interactive process viewer.

### systemctl

```bash
systemctl status service
```

Controls system services.

---

## 🧮 Utilities

### wget

```bash
wget URL
```

Downloads files from the internet.

### curl

```bash
curl URL > file
```

Transfers data from/to servers.

### zip / unzip

```bash
zip file.zip file
unzip file.zip
```

Compresses and extracts files.

### sort

```bash
sort filename
```

Sorts file content.

### diff / cmp

```bash
diff file1 file2
cmp file1 file2
```

Compares files.

### grep

```bash
grep pattern file
```

Searches for text patterns.

### awk

```bash
awk '{print $1}' file
```

Processes and analyzes text data.

---

## ⏱️ Miscellaneous

### history

```bash
history
```

Shows command history.

### kill

```bash
kill PID
```

Terminates a process.

### clear

```bash
clear
```

Clears the terminal screen.

### exit

```bash
exit
```

Exits the shell session.

---

## ✅ Day 10 Summary

✔ Learned essential Linux commands
✔ Covered file, user, network, and system management
✔ Built a strong command-line foundation for cybersecurity

---

🧠 *Mastering Linux commands is about understanding what happens behind the scenes, not memorizing flags.*
