# Pytest-Selenium Test Template

A comprehensive template for running Selenium tests with pytest, including fixtures, page objects, and best practices.

## Project Structure

```
.
├── conftest.py                  # Pytest fixtures and configuration
├── pytest.ini                   # Pytest settings
├── requirements.txt             # Python dependencies
├── pages.py                     # Page Object Model classes
├── test_example.py              # Example tests
├── test_with_page_objects.py    # Tests using Page Objects
├── reports/                     # HTML test reports (auto-generated)
└── logs/                        # Test logs (auto-generated)
```

## Setup

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Browser Drivers

The template uses `webdriver-manager` which automatically downloads and manages browser drivers. No manual driver installation needed!

## Running Tests

### Basic Usage

```bash
# Run all tests
pytest

# Run specific test file
pytest test_example.py

# Run specific test class
pytest test_example.py::TestExampleWebsite

# Run specific test
pytest test_example.py::TestExampleWebsite::test_page_title
```

### Advanced Options

```bash
# Run with specific browser
pytest --browser=chrome
pytest --browser=firefox
pytest --browser=edge

# Run in headless mode
pytest --headless

# Run tests with markers
pytest -m smoke           # Run only smoke tests
pytest -m "not slow"      # Skip slow tests

# Run tests in parallel (requires pytest-xdist)
pytest -n auto            # Auto-detect CPU count
pytest -n 4               # Use 4 workers

# Rerun failed tests
pytest --reruns 3         # Rerun failed tests 3 times
pytest --reruns-delay 2   # Wait 2 seconds between reruns

# Generate HTML report
pytest --html=reports/report.html --self-contained-html

# With coverage
pytest --cov=. --cov-report=html

# Verbose output
pytest -v

# Show print statements
pytest -s
```

## Writing Tests

### Using Simple Fixtures

```python
def test_example(driver, base_url):
    driver.get(base_url)
    assert "Example" in driver.title
```

### Using Page Objects

```python
from pages import LoginPage

def test_login(driver):
    login_page = LoginPage(driver)
    login_page.navigate()
    home_page = login_page.login("user", "pass")
    assert home_page.is_logged_in()
```

### Using Parameterization

```python
@pytest.mark.parametrize("username,password", [
    ("user1", "pass1"),
    ("user2", "pass2"),
])
def test_login_multiple_users(driver, username, password):
    # Test logic here
    pass
```

## Fixtures Available

- `driver`: Basic Selenium WebDriver (Chrome by default)
- `browser_driver`: Advanced driver with browser selection support
- `wait`: WebDriverWait instance for explicit waits
- `base_url`: Base URL for the application under test

## Test Markers

Use markers to categorize tests:

```python
@pytest.mark.smoke
def test_critical_path(driver):
    pass

@pytest.mark.slow
def test_long_running(driver):
    pass

@pytest.mark.skip(reason="Not ready")
def test_future_feature(driver):
    pass

@pytest.mark.xfail(reason="Known bug")
def test_known_issue(driver):
    pass
```

## Configuration

### conftest.py
- Contains all pytest fixtures
- Configures WebDriver options
- Handles screenshot capture on test failure
- Supports multiple browsers

### pytest.ini
- Test discovery patterns
- Marker definitions
- Output options
- Logging configuration

## Best Practices

1. **Use Page Object Model** for better maintainability
2. **Use explicit waits** instead of implicit waits or sleep
3. **Keep tests independent** - each test should be able to run alone
4. **Use meaningful test names** that describe what is being tested
5. **Use fixtures** for setup and teardown
6. **Use markers** to organize tests
7. **Capture screenshots** on failures for debugging
8. **Run tests in parallel** when possible for faster execution

## Troubleshooting

### Browser driver issues
- The template uses `webdriver-manager` which auto-downloads drivers
- If issues persist, try updating: `pip install --upgrade webdriver-manager`

### Element not found
- Use explicit waits: `wait.until(EC.presence_of_element_located(...))`
- Check if element is in an iframe
- Verify selector is correct

### Tests timing out
- Increase timeout in WebDriverWait
- Check if page is loading correctly
- Use `pytest-timeout` to set global timeout

## Contributing

Feel free to extend this template with:
- Additional page objects
- More fixture configurations
- Custom pytest plugins
- CI/CD integration examples
