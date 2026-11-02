# Flipkart Login Automation Test

A basic Python Selenium example that opens Flipkart and starts its login flow.

> For safety, credentials are read from environment variables and are never committed. Flipkart may require an OTP, CAPTCHA, or UI-selector updates. This example intentionally does not bypass those controls.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

Set your test mobile number or email:

```bash
export FLIPKART_USERNAME="your-test-account"
```

Windows PowerShell:

```powershell
$env:FLIPKART_USERNAME="your-test-account"
```

## Run

```bash
pytest -v
```

The browser opens Flipkart, attempts to display the login form, enters the configured username, and stops before OTP/CAPTCHA verification.
