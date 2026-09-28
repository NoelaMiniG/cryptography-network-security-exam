# Network Traffic Filtering Configuration and Tests

This document contains interface-based Netfilter/iptables firewall rules designed to secure the ULK Student Records Server dynamically, without relying on fixed IP addresses.

## 1. Interface and Variable Mapping
*   **`GUEST_IFACE`** (e.g., `eth2` or `wlan1`): The network interface where campus guest traffic arrives.
*   **`STAFF_IFACE`** (e.g., `eth1`): The network interface where authorized staff traffic arrives.
*   **`PORT_NUMBER`** (`443`): The standard secure port used for protected file transfer services (HTTPS).

---

## 2. Dynamic Firewall Rules (iptables Commands)

These rules filter traffic dynamically based on the entry interface or port variables:

```bash
# a. Block all guest network access to the local student records server
sudo iptables -A INPUT -i $GUEST_IFACE -j DROP

# b. Permit authorized staff network access to the specific secure service port
sudo iptables -A INPUT -i $STAFF_IFACE -p tcp --dport $PORT_NUMBER -j ACCEPT

# c. Block all other inbound access to that specific service port from any other interface
sudo iptables -A INPUT -p tcp --dport $PORT_NUMBER -j DROP
```

---

## 3. Connection Test Log

### Test 1: Permitted Connection (Authorized Staff to Service)
*   **Command executed from a laptop on the Staff interface:**
    ```bash
    curl -I https://records-server.local
    ```
*   **Expected Outcome:** Connection accepted because it originates from the authorized staff zone.
*   **Actual Result:** `HTTP/1.1 200 OK` (Connection Allowed).

### Test 2: Blocked Connection (Guest Network to Server)
*   **Command executed from a device on the Guest interface:**
    ```bash
    ping -c 3 records-server.local
    ```
*   **Expected Outcome:** Traffic arriving on the guest interface is dropped immediately by the firewall.
*   **Actual Result:** `100% packet loss` (Connection Blocked).

### Test 3: Blocked Connection (Other Interface to Protected Service)
*   **Command executed from an unfamiliar external interface address:**
    ```bash
    curl --max-time 5 https://records-server.local
    ```
*   **Expected Outcome:** The firewall blocks unauthorized interface zones, causing the connection to time out.
*   **Actual Result:** `curl: (28) Connection timed out` (Connection Blocked).
