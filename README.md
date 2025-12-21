# Pytest-Selenium Test Template

A comprehensive template for running Selenium tests with pytest, including fixtures, page objects, and best practices.

## Project Structure

```
.
├── conftest.py                         # Pytest fixtures and configuration
├── pytest.ini                          # Pytest settings
├── requirements.txt                    # Python dependencies
├── pages.py                            # Page Object Model classes (deprecated)
├── home_page.py                        # WstyleHomePage page object
├── login_page.py                       # WstyleLoginPage page object
├── test_wstyle_login.py                # Login and navigation tests
├── test_wstyle_with_page_objects.py    # Additional real-world test examples
├── reports/                            # HTML test reports (auto-generated)
├── logs/                               # Test logs (auto-generated)
└── screenshot_*.png                    # Test failure screenshots (auto-captured)
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
pytest test_wstyle_with_page_objects.py

# Run specific test class
pytest test_wstyle_with_page_objects.py::TestWstyleLoginWithPageObjects

# Run specific test
pytest test_wstyle_with_page_objects.py::TestWstyleLoginWithPageObjects::test_successful_login_and_logout
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
pytest -m ui              # Run only UI tests
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

The repository includes both example page objects (LoginPage, HomePage, SearchPage) and real-world implementations (WstyleHomePage, WstyleLoginPage).

#### Generic Example

```python
from pages import LoginPage

def test_login(driver):
    login_page = LoginPage(driver)
    login_page.navigate()
    home_page = login_page.login("user", "pass")
    assert home_page.is_logged_in()
```

#### Real-World Example

```python
from pages import WstyleHomePage

@pytest.mark.ui
def test_login_flow(browser_driver):
    # Navigate and handle popups
    home_page = WstyleHomePage(browser_driver)
    home_page.navigate().close_popup()

    # Verify elements and perform login
    assert home_page.is_login_button_present()
    login_page = home_page.click_login()
    home_page = login_page.login("username", "password")

    # Verify successful login
    assert home_page.is_login_button_present()
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

## Page Objects Available

The `pages.py` file contains several page object classes demonstrating different patterns:

### Example Page Objects (Generic Templates)
- **BasePage**: Base class with common methods (find_element, click_element, enter_text, etc.)
- **LoginPage**: Generic login page example
- **HomePage**: Generic home page example
- **SearchPage**: Generic search page example

### Real-World Page Objects (Wstyle.com.tw)
- **WstyleHomePage**: Home page with popup handling, navigation buttons
- **WstyleLoginPage**: Login page with form validation and authentication

These serve as both working examples and templates for creating your own page objects.

## Example Tests Included

The repository includes real-world test examples for Wstyle.com.tw:

### test_wstyle_login.py

#### TestWstyleLogin
- **test_successful_login_and_logout**: Complete authentication flow testing
  - Popup handling
  - Element verification (login button, form labels)
  - Login/logout functionality
  - Multi-language support validation
  - Screenshot: `screenshot_test_successful_login_and_logout.png`

#### TestWstyleHomePage
- **test_navigation_elements_present**: Navigation element verification
  - Checks for login, member, order, and cart buttons
  - Demonstrates assertion patterns
  - Screenshot: `screenshot_test_navigation_elements_present.png`

### test_wstyle_with_page_objects.py
Additional test examples demonstrating various Page Object Model patterns.

These tests serve as practical examples of implementing Page Object Model with pytest.

## Test Markers

Use markers to categorize tests:

```python
@pytest.mark.ui
def test_user_interface(driver):
    """Test UI interactions."""
    pass

@pytest.mark.smoke
def test_critical_path(driver):
    """Test critical user paths."""
    pass

@pytest.mark.slow
def test_long_running(driver):
    """Test that takes longer to complete."""
    pass

@pytest.mark.skip(reason="Not ready")
def test_future_feature(driver):
    """Skip this test for now."""
    pass

@pytest.mark.xfail(reason="Known bug")
def test_known_issue(driver):
    """Expected to fail due to known issue."""
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

## Test Reports and Screenshots

### HTML Reports

After running tests with the `--html` option, view the detailed report:

```bash
open reports/report.html  # macOS
xdg-open reports/report.html  # Linux
start reports/report.html  # Windows
```

The report includes:
- Test execution summary
- Pass/fail status for each test
- Execution time
- Environment details
- Test logs and outputs

### Screenshots

Screenshots are automatically captured on test failures (configured in `conftest.py`). Screenshots are also manually captured during test execution for documentation purposes:

- `screenshot_test_successful_login_and_logout.png` - Login flow verification
- `screenshot_test_navigation_elements_present.png` - Navigation elements check

Screenshots help with:
- Debugging test failures
- Visual documentation of test scenarios
- Understanding application state at failure point

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
