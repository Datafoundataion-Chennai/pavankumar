# README: SQL Training Guide

## 📌 Introduction to SQL

SQL (Structured Query Language) is a powerful and standardized programming language used to create, manipulate, and manage relational databases. It is widely used across various applications, from small-scale projects to enterprise-level systems.

---

## 1️⃣ **What is SQL?**

SQL is a domain-specific language used for managing and querying relational databases. It allows users to:

- Define database structures (DDL)
- Insert, update, and delete records (DML)
- Retrieve data efficiently (DQL)
- Control access to data (DCL)
- Manage transactions (TCL)

SQL is the foundation of modern data management systems, including MySQL, PostgreSQL, Oracle, and SQL Server.

---

## 2️⃣ **Introduction to RDBMS**

A **Relational Database Management System (RDBMS)** is software that stores data in a structured format using tables. It maintains relationships between data entities and enforces integrity constraints.

### **Key Features of RDBMS:**

- Uses tables to store data
- Supports ACID (Atomicity, Consistency, Isolation, Durability) properties
- Enables indexing for faster queries
- Provides multi-user access with security mechanisms

Examples: MySQL, PostgreSQL, Microsoft SQL Server, Oracle DB.

---

## 3️⃣ **Schema**

A **schema** represents the logical design of a database. It defines tables, columns, constraints, indexes, and relationships.

A schema includes:

- Tables and their structures
- Relationships between tables (Primary Key, Foreign Key)
- Views and stored procedures
- User permissions and constraints

---

## 4️⃣ **Table Structure**

A **table** is the core component of a relational database, storing records in a structured way.

Each table consists of:

- **Columns** (fields) defining data attributes
- **Rows** (records) representing individual data entries
- **Primary Key** for unique identification
- **Foreign Key** to establish relationships between tables

Example Table Structure:

```sql
CREATE TABLE Employees (
    EmployeeID INT PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Age INT CHECK (Age >= 18),
    Salary DECIMAL(10,2),
    DepartmentID INT,
    FOREIGN KEY (DepartmentID) REFERENCES Departments(DepartmentID)
);
```

---

## 5️⃣ **SQL Data Types**

SQL supports various data types to store different kinds of information.

### **Common SQL Data Types:**

- **Integer Types**: INT, SMALLINT, BIGINT
- **Floating-Point Types**: FLOAT, DOUBLE, DECIMAL
- **String Types**: CHAR, VARCHAR, TEXT
- **Date/Time Types**: DATE, TIME, TIMESTAMP
- **Boolean Type**: BOOLEAN

Choosing the right data type ensures optimized storage and efficient querying.

---

## 6️⃣ **What is a Database?**

A **database** is an organized collection of data that allows efficient retrieval, insertion, and updating.

Databases can be:

- **Relational (RDBMS)**: MySQL, PostgreSQL
- **NoSQL**: MongoDB, Cassandra
- **In-Memory**: Redis

A well-designed database ensures data consistency, integrity, and performance optimization.

---

## 7️⃣ **Defining Schema**

A schema defines how data is structured and related in a database.

### **Types of Schemas:**

- **Physical Schema**: Defines actual data storage
- **Logical Schema**: Defines data relationships and constraints
- **View Schema**: Defines user-accessible views

Example:

```sql
CREATE SCHEMA CompanyDB;
```

---

## 8️⃣ **Data Modeling & ERD (Entity Relationship Diagram)**

**Data Modeling** is the process of designing a database structure.

### **ERD Components:**

- **Entities**: Objects in the database (e.g., Employees, Departments)
- **Attributes**: Properties of entities (e.g., Name, Age, Salary)
- **Relationships**: Connections between entities (e.g., One-to-Many, Many-to-Many)

ERDs help visualize database structures before implementation.

---

## 9️⃣ **Overview of SQL Sublanguages**

SQL is divided into five sublanguages:

- **DDL (Data Definition Language)** - Defines database structure
- **DML (Data Manipulation Language)** - Modifies data records
- **DQL (Data Query Language)** - Retrieves data
- **DCL (Data Control Language)** - Manages access control
- **TCL (Transaction Control Language)** - Controls transactions

---

## 🔹 **DDL (Data Definition Language)**

DDL manages database structure.

### **Key Commands:**

- `CREATE` - Creates database objects
- `ALTER` - Modifies table structure
- `DROP` - Deletes tables or databases

Example:

```sql
CREATE TABLE Departments (
    DepartmentID INT PRIMARY KEY,
    DepartmentName VARCHAR(50) NOT NULL
);
```

---

## 🔹 **DML (Data Manipulation Language)**

DML handles data modification.

### **Key Commands:**

- `INSERT` - Adds new records
- `UPDATE` - Modifies existing records
- `DELETE` - Removes records

Example:

```sql
INSERT INTO Employees (EmployeeID, Name, Salary) 
VALUES (101, 'Alice', 75000);
```

---

## 🔹 **DQL (Data Query Language)**

DQL retrieves data from tables.

### **Key Command:**

- `SELECT` - Fetches data

Example:

```sql
SELECT Name, Salary FROM Employees WHERE Salary > 50000;
```

---

## 🔹 **DCL (Data Control Language)**

DCL controls access to database resources.

### **Key Commands:**

- `GRANT` - Provides user permissions
- `REVOKE` - Removes permissions

Example:

```sql
GRANT SELECT ON Employees TO user1;
```

---

## 🔹 **TCL (Transaction Control Language)**

TCL manages database transactions.

### **Key Commands:**

- `COMMIT` - Saves changes permanently
- `ROLLBACK` - Undoes changes
- `SAVEPOINT` - Creates checkpoints

Example:

```sql
BEGIN TRANSACTION;
UPDATE Employees SET Salary = 80000 WHERE EmployeeID = 101;
ROLLBACK;
```

---

## 📌 **Queries and Advanced Operations**

### **Sorting and Filtering**

```sql
SELECT * FROM Employees ORDER BY Salary DESC;
```

### **Joins (Combining Tables)**

```sql
SELECT Employees.Name, Departments.DepartmentName
FROM Employees
INNER JOIN Departments ON Employees.DepartmentID = Departments.DepartmentID;
```

### **Grouping and Aggregation**

```sql
SELECT DepartmentID, AVG(Salary) FROM Employees GROUP BY DepartmentID;
```

---

## 🎯 **Conclusion**

SQL is an essential skill for database management, allowing efficient data handling, security, and transactions. Mastering SQL enhances the ability to work with structured data effectively across various domains.

