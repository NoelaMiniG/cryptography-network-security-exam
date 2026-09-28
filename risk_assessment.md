# Risk Assessment: ULK Student Records Server

## 1. Assets, Vulnerabilities, and Consequences

### Risk 1: Unencrypted Campus File Transfers
* **Asset:** Student Record Data in Transit (files moving between campuses).
* **Vulnerability:** Unencrypted file transfer protocols.
* **Consequence:** Attackers can spy on network traffic and steal or change student data.

### Risk 2: Weak Authentication & Server Exposure
* **Asset:** Central Server (where data is stored).
* **Vulnerability:** Weak staff passwords and exposed services.
* **Consequence:** External attackers can guess passwords and take over the system.

### Risk 3: Open Network Segmenting
* **Asset:** Internal Network Security (access control).
* **Vulnerability:** Guest network users can talk directly to the records server.
* **Consequence:** Unauthorised visitors can try to hack the server directly from the campus Wi-Fi.

---

## 2. Risk Evaluation and Ranking

| Risk Source | Likelihood | Impact | Priority | Reason |
| :--- | :--- | :--- | :--- | :--- |
| **Weak Passwords + Probing** | High | High | **Critical** | Attackers are already actively trying to log in from an external address. |
| **Guest Network Access** | High | Medium | **High** | Guests have an open, unrestricted network path to the server right now. |
| **Unencrypted Transfers** | Medium | High | **High** | Harder to intercept, but leaks private student identities if compromised. |

---

## 3. Recommended Security Controls

* **For Unencrypted Transfers:** Switch to secure connection methods like **HTTPS** or **SFTP** to encrypt data in transit.
* **For Weak Passwords:** Force staff to use **strong passwords** and turn on **Multi-Factor Authentication (MFA)**.
* **For Guest Access:** Configure **firewall rules** to completely block the guest network from reaching the server subnet.
