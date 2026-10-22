# SauceDemo Automation Framework (Selenium + PyTest)

A robust UI test automation framework implementing the **Page Object Model (POM)** pattern in Python using **Selenium WebDriver** and **PyTest**.

## Architecture
- **Page Object Model:** Strict separation between locators, page actions, and test assertions.
- **Explicit Waits:** Stable locator resolution using `WebDriverWait` and `expected_conditions`.
- **Automated Driver Management:** Powered by `webdriver-manager`.
- **PyTest Fixtures:** Clean browser lifecycle and headless runtime execution in `conftest.py`.

## Test Execution
1. Install dependencies:
   ```bash
   pip install selenium pytest webdriver-manager
   ```
2. Run all tests:
   ```bash
   python -m pytest tests/ -v
   ```