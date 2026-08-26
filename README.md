# pyPWForge — Python Playwright Automation Framework

Python-based test automation framework built with **Playwright, Pytest, Page Object Model (POM), API testing, Allure reporting, GitHub Actions CI/CD, GitHub Pages, and Slack notifications**.

The project demonstrates practical SDET concepts including reusable UI/API automation, parameterized tests, external test data, cross-browser execution, failure diagnostics, automated reporting, CI validation, scheduled execution, report publishing, and team notifications.

---

## Tech Stack

- **Language:** Python
- **UI Automation:** Playwright
- **Test Framework:** Pytest
- **API Testing:** Playwright APIRequestContext
- **Design Pattern:** Page Object Model (POM)
- **Reporting:** Allure / allure-pytest
- **CI/CD:** GitHub Actions
- **Report Hosting:** GitHub Pages
- **Notifications:** Slack
- **Test Data:** JSON
- **Version Control:** Git / GitHub

---

## Framework Structure

```text
pyPWForge/
│
├── .github/
│   └── workflows/
│       └── tests.yml
│
├── pages/
│   ├── LoginPage.py
│   ├── MenuBar.py
│   ├── EventPage.py
│   └── CreateNewEventPage.py
│
├── utils/
│   ├── api_base.py
│   └── test_data.py
│
├── tests/
│   ├── ui/
│   │   └── test_web_basic.py
│   │
│   └── api/
│       └── test_map_api.py
│
├── testData/
│   ├── userCredentials.json
│   └── location_data.json
│
├── conftest.py
├── requirements.txt
├── pytest.ini
├── .gitignore
└── README.md
```

Generated files such as `allure-results/`, `allure-report/`, `.venv/`, `__pycache__/`, IDE files, and OS-specific files are excluded through `.gitignore`.

---

# Key Features

### UI Automation

- Playwright UI automation with Pytest
- Page Object Model for maintainability
- Chromium and Firefox support
- Headed and headless execution
- Parameterized UI tests
- Reusable page actions

### API Automation

- Playwright `APIRequestContext`
- CRUD-style API workflow validation
- Response status and body assertions
- Reusable API utilities
- External JSON test data

### Failure Diagnostics

When a UI test fails, the framework captures:

- Failure screenshot
- Playwright trace
- Browser actions
- DOM snapshots
- Timing information
- Source information

This gives the team evidence to investigate the failure instead of relying only on the assertion message.

---

# Test Scenarios

## UI — Create Event

The UI test automates creation and verification of a new event.

```text
Login
  ↓
Navigate to Events
  ↓
Open Create New Event
  ↓
Enter Event Details
  ↓
Create Event
  ↓
Verify Event
```

The test uses:

- Parameterized credentials
- Page Object Model
- Dynamic event names
- Reusable page actions
- Allure feature/story/title metadata
- Failure screenshot and Playwright trace support

## API — Place Management

The API test validates a complete place-management workflow:

```text
Add Location
     ↓
Get Location
     ↓
Verify Location
     ↓
Update Location
     ↓
Verify Updated Address
     ↓
Delete Location
```

The workflow validates response status, response body, location details, update persistence, and deletion.

---

# Test Data Management

Test data is maintained separately from the test implementation using JSON files.

```text
testData/
├── userCredentials.json
└── location_data.json
```

The current `userCredentials.json` contains **dummy training credentials**.

For real environments, credentials should not be committed to source control. Use environment variables or GitHub Actions Secrets instead.

---

# Local Setup

## 1. Clone the repository

```bash
git clone <repository-url>
cd pyPWForge
```

## 2. Create a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

## 4. Install Playwright browsers

```bash
playwright install
```

---

# Running Tests

## Complete test suite

```bash
pytest
```

By default, UI tests run in headless mode.

## UI tests

```bash
pytest tests/ui
```

## UI tests with a visible browser

```bash
pytest tests/ui --headed
```

## API tests

```bash
pytest tests/api
```

## Chrome

```bash
pytest --browser_name=chrome
```

## Firefox

```bash
pytest --browser_name=firefox
```

## Firefox with headed mode

```bash
pytest --browser_name=firefox --headed
```

---

# Allure Reporting

Allure is integrated with Pytest through `allure-pytest`.

Run tests with:

```bash
pytest --alluredir=allure-results
```

This creates the raw Allure execution data:

```text
allure-results/
├── result files
├── container files
└── attachments
```

`allure-results` is **not the dashboard**. It is the raw test data consumed by the Allure CLI.

To generate a report locally:

```bash
allure generate allure-results -o allure-report --clean
```

To serve it locally:

```bash
python3 -m http.server 8000 --directory allure-report
```

Then open:

```text
http://localhost:8000
```

Using a local HTTP server is preferable to opening `index.html` directly because the Allure report uses browser-side resources.

---

# Failure Screenshots and Playwright Traces

The framework starts Playwright tracing when the browser context is created.

For a failed UI test:

```text
Test Failure
     │
     ├── Failure Screenshot
     │
     └── Playwright Trace
           ├── Actions
           ├── Screenshots
           ├── DOM snapshots
           ├── Source information
           └── Timing
```

The trace is attached to the Allure result as a ZIP file.

### View the trace locally

Using the Playwright CLI:

```bash
playwright show-trace <trace-file>.zip
```

### View the trace in a browser

You can also use the **Playwright Trace Viewer**:

**https://trace.playwright.dev/**

Download the `.zip` trace attachment from Allure or GitHub Actions and drag and drop it into the Trace Viewer.

The Trace Viewer provides a detailed view of browser actions, screenshots, DOM snapshots, source information, network activity, and timing, making it easier to investigate why a test failed.

---

# CI/CD — GitHub Actions

The workflow is located at:

```text
.github/
└── workflows/
    └── tests.yml
```

The CI pipeline supports:

- Push to `main`
- Pull requests targeting `main`
- Manual execution through **Run workflow**
- Scheduled execution using cron

The CI pipeline runs on a fresh Ubuntu runner.

## CI Flow

```text
Push / Pull Request / Manual / Schedule
                  ↓
          GitHub Actions
                  ↓
          Slack: CI Started
                  ↓
           Ubuntu Runner
                  ↓
          Setup Python 3.12
                  ↓
        Install Dependencies
                  ↓
      Install Playwright Browsers
                  ↓
          Install Allure CLI
                  ↓
             Run Pytest
                  ↓
          Allure Results
                  ↓
          Generate Report
                  ↓
        Upload CI Artifacts
                  ↓
      ┌───────────┴───────────┐
      │                       │
     PR                     main
      │                       │
      ▼                       ▼
No Pages deployment      GitHub Pages
      │                       │
      ▼                       ▼
CI Artifacts             Allure Dashboard
      │                       │
      └───────────┬───────────┘
                  ▼
          Slack: CI Completed
```

---

# Workflow Triggers

### Push

A push to `main` triggers the workflow.

### Pull Request

A pull request targeting `main` triggers CI validation.

PRs run the tests and generate Allure artifacts, but **do not publish the report to the shared GitHub Pages dashboard**.

This prevents different pull requests from overwriting the same shared dashboard.

### Manual

The workflow can be started manually from:

```text
GitHub
 → Actions
 → Automated Tests
 → Run workflow
```

### Scheduled

The workflow also runs automatically using a cron schedule configured in `tests.yml`.

The schedule uses the configured timezone:

```yaml
timezone: "Europe/Berlin"
```

---

# Allure Artifacts in CI

The CI workflow preserves two artifacts:

### `allure-results`

Raw Allure execution data, including test metadata and attachments.

### `allure-report`

The generated HTML Allure report.

These artifacts remain useful for investigating failed CI executions.

For pull requests, the Allure report is **not deployed to GitHub Pages**, but the generated report remains available through the specific GitHub Actions run.

The Slack completion notification provides a direct link to that workflow run so the team can access the artifacts.

---

# GitHub Pages — Allure Dashboard

For executions on the `main` branch:

```text
Test
 ↓
Allure Results
 ↓
Allure Report
 ↓
GitHub Pages
 ↓
Allure Dashboard
```

The deployment job downloads the generated Allure report, packages it for GitHub Pages, and deploys it.

The workflow is configured with:

```yaml
if: always() && github.ref == 'refs/heads/main'
```

This means a failed `main` test can still produce and publish the failure report.

The workflow remains **failed** because the test job failed, but the report is still available for investigation.

---

# Slack CI Notifications

GitHub Actions sends CI notifications to a dedicated Slack channel.

The webhook is stored securely as:

```text
SLACK_WEBHOOK_URL
```

in GitHub Actions repository secrets.

The webhook URL is **never stored in the repository**.

## CI Started

When a workflow begins, Slack receives information such as:

```text
🔵 CI Started

Repository: kavin-crypto/pyPWForge
Branch: main
Triggered by: kavin-crypto
Workflow: Automated Tests
Commit: <commit-sha>
```

This is useful when multiple QA/SDET engineers or other team members are working on the repository because the team can immediately see who triggered the CI run.

## CI Completed — main

After testing and deployment:

```text
✅ CI Completed

Repository: kavin-crypto/pyPWForge
Branch: main
Triggered by: kavin-crypto
Status: success
Workflow: Automated Tests

📊 Allure Report:
<GitHub Pages URL>
```

The Allure URL is obtained dynamically from the GitHub Pages deployment rather than hard-coded.

## CI Completed — Pull Request

For pull requests:

```text
✅ CI Completed

Repository: kavin-crypto/pyPWForge
Branch: <PR branch>
Triggered by: <user>
Status: success
Workflow: Automated Tests

📦 Allure Report:
Not deployed for pull requests.

🔎 View CI Artifacts:
<GitHub Actions run URL>
```

The team member can open the specific workflow run and download the Allure report artifact for debugging.

---

# Debugging a Failed CI Test

Recommended debugging flow:

```text
GitHub Actions
      ↓
Check failed step
      ↓
Open Allure Report
      ↓
Inspect assertion / logs
      ↓
Open failure screenshot
      ↓
Download Playwright trace
      ↓
Open Trace Viewer
      ↓
Investigate browser actions and DOM state
```

This separates:

- **CI execution information** — GitHub Actions
- **Test execution details** — Allure
- **Visual evidence** — Screenshot
- **Detailed browser execution** — Playwright Trace Viewer
- **Team notification** — Slack

---

# CI Design Principles

The pipeline separates different responsibilities:

```text
TESTING
Playwright + Pytest
        ↓
EVIDENCE
Screenshot + Trace + Logs
        ↓
REPORTING
Allure
        ↓
CI/CD
GitHub Actions
        ↓
PUBLISHING
GitHub Pages
        ↓
NOTIFICATION
Slack
```

The goal is not only to execute tests, but also to:

1. Validate changes automatically.
2. Preserve evidence when tests fail.
3. Generate an understandable test report.
4. Publish the report when appropriate.
5. Notify the team about the execution.
6. Make failures easier to investigate.

---

# Project Focus

This project focuses on practical **SDET and QA automation engineering** concepts:

- UI automation
- API automation
- Page Object Model
- Pytest fixtures
- Parameterization
- Test data management
- Cross-browser testing
- Headed/headless execution
- API response validation
- End-to-end API workflows
- Allure reporting
- Failure screenshots
- Playwright tracing
- GitHub Actions CI/CD
- Scheduled test execution
- GitHub Pages
- Slack CI notifications
- CI failure diagnostics

---

# CI/CD Summary

> **pyPWForge is a Python Playwright automation framework using Pytest for UI and API testing. It integrates Allure for test reporting, captures failure screenshots and Playwright traces, and uses GitHub Actions to automatically validate changes, generate reports, publish the latest `main` report through GitHub Pages, and notify the team through Slack.**