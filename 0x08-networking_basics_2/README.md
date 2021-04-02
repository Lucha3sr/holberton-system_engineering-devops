B# Networking basics #1

## Learning Objectives

**General**

- What is localhost/127.0.0.1
- What is 0.0.0.0
- What is /etc/hosts
- How to display your machines active network interfaces

### Tasks

**0. Change your home IP**

Write a Bash script that configures an Ubuntu server with the below requirements.

Requirements:

- localhost resolves to 127.0.0.2
- facebook.com resolves to 8.8.8.8.
- The checker is running on Docker, so make sure to read this

```
cp /etc/hosts ~/hosts.new
sed ... ~/hosts.new
cp -f ~/hosts.new /etc/hosts
```

You can change the sed command with that you want.

- Example sed to add 127.0.0.1 `hostname` to your /etc/hosts.
   - sed -i s/^172.*$// ~/hosts.new


**1. Show attached IPs**

Write a Bash script that displays all active IPv4 IPs on the machine its executed on.

