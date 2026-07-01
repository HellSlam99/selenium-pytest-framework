# Selenium Pytest Automation Framework

A production-ready UI Automation Framework built using **Python**, **Selenium**, and **Pytest** following the **Page Object Model (POM)** design pattern.

The framework demonstrates best practices for scalable UI automation including reusable page objects, explicit waits, logging, screenshots, HTML reporting, and data-driven testing.

---

## Tech Stack

- Python 3.11+
- Selenium WebDriver
- Pytest
- Page Object Model (POM)
- WebDriver Manager
- Pytest HTML Reports
- Logging
- CSV Data-Driven Testing

---

## Project Structure

```
selenium-pytest-framework
│
├── main
│   └── src
│       ├── config
│       ├── data
│       ├── pages
│       ├── reports
│       ├── screenshots
│       └── utils
│
├── tests
│
├── conftest.py
├── pytest.ini
├── requirements.txt
├── run.py
├── README.md
└── .gitignore
```

---

## Framework Features

- Page Object Model (POM)
- Explicit Waits
- Cross Browser Support
- Configurable Browser Selection
- Headless Execution
- HTML Test Reports
- Automatic Screenshot Capture
- Logging Support
- CSV Data-Driven Testing
- Reusable Base Page
- Pytest Fixtures
- Modular Folder Structure
- Easy to Extend

---

## Test Scenarios

### Scenario 1

- Login with valid credentials
- Validate successful login

---

### Scenario 2

- Login with invalid username/password
- Validate error message

---

### Scenario 3

- Login
- Add four products
- Navigate to cart
- Remove one product
- Validate only three products remain

---

### Scenario 4

- Complete checkout flow
- Validate successful order placement

---

### Scenario 5

- Data Driven Login using CSV
- Validate successful and unsuccessful login scenarios

---

## Data Driven Testing

CSV File

```
user,password,result

standard_user,secret_sauce,pass
standard_user,secrt_sauce,fail
problem_user,secret_sauce,pass
```

---

## Reports

HTML report is generated after execution.

```
main/src/reports/report.html
```

---

## Screenshots

Screenshots are automatically captured during execution and on test failures.

```
main/src/screenshots/
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/HellSlam99/selenium-pytest-framework.git
```

Move into project

```bash
cd selenium-pytest-framework
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Running Tests

Run all tests

```bash
pytest
```

Run a single test

```bash
pytest tests/test_login.py
```

Run in headless mode

```bash
pytest --headless
```

Generate HTML Report

```bash
pytest --html=main/src/reports/report.html --self-contained-html
```

---

## Framework Architecture

```
Tests
    │
    ▼
Page Objects
    │
    ▼
Base Page
    │
    ▼
Driver Factory
    │
    ▼
Selenium WebDriver
```

---

## Design Patterns Used

- Page Object Model (POM)
- Factory Pattern
- Fixture-based Test Setup
- Data-Driven Testing
- Reusable Utility Classes

---

## Future Enhancements

- Allure Reports
- Jenkins Integration
- GitHub Actions CI/CD
- Docker Execution
- Parallel Test Execution
- Excel Data Provider
- JSON/YAML Data Provider
- Database Validation
- API Testing Integration
- Retry Mechanism
- Environment Profiles

---

## Author

**Ansh**

Automation QA | Python | Selenium | Pytest
