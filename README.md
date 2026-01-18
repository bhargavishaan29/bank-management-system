# bank-management-system


---

### **Bank Management System (Python)**

This project is a **console-based Bank Management System** developed in Python with the primary goal of strengthening core programming fundamentals and object-oriented design skills. The project focuses on **logic, structure, and real-world system modeling**, rather than external libraries, databases, or graphical interfaces.

The system allows users to **create and manage multiple bank accounts** within a single application. Each account is represented as an object and stored in a dictionary using the account number as a unique identifier. This approach simulates how real-world systems manage multiple users and ensures a single source of truth for account data.

Security is handled through **PIN-based authentication**, where users must enter a valid account number followed by a correct PIN to access account-specific operations. Login attempts are limited, reflecting real banking security practices. Once authenticated, users can perform actions such as viewing account details, depositing money, withdrawing money, and logging out safely.

A key feature of this project is **transaction history tracking**. Each account maintains its own list of transactions, which records every credit and withdrawal operation. This demonstrates state persistence within objects and reinforces encapsulation by keeping transaction data tied directly to the account it belongs to.

The project is structured around a **two-level menu system**:

* A **system menu** for creating accounts, logging in, and exiting the program.
* An **account menu** that becomes available after successful login, allowing users to perform account operations.

Through this project, key concepts such as object-oriented programming, authentication flow, dictionary-based data management, and menu-driven system design were applied in a practical context. The project serves as a strong foundational exercise for backend development, data structures, and more advanced system design in future projects.



