import os

import allure
import pytest
from playwright.sync_api import sync_playwright


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name",
        action="store",
        default="chrome",
        choices=["chrome", "firefox"],
        help="browser to use",
    )

@pytest.fixture()
def browser_invoke(playwright, request):
    browser_name = request.config.getoption("browser_name")
    headless = not request.config.getoption("headed")

    if browser_name == "chrome":
        browser = playwright.chromium.launch(headless=headless)
    elif browser_name == "firefox":
        browser = playwright.firefox.launch(headless=headless)

    context = browser.new_context()

    # Start Playwright tracing
    context.tracing.start(
        screenshots=True,
        snapshots=True,
        sources=True
    )

    page = context.new_page()
    page.goto("https://eventhub.rahulshettyacademy.com")

    yield page

    # Teardown
    if getattr(request.node, "test_failed", False):

        os.makedirs("allure-results", exist_ok=True)

        # Capture screenshot
        screenshot_path = os.path.join(
            "allure-results",
            f"{request.node.name}-failure.png"
        )

        page.screenshot(path=screenshot_path)

        allure.attach.file(
            screenshot_path,
            name="Failure Screenshot",
            attachment_type=allure.attachment_type.PNG
        )

        # Save Playwright trace
        trace_path = os.path.join(
            "allure-results",
            f"{request.node.name}-trace.zip"
        )

        context.tracing.stop(path=trace_path)

        # Attach trace to Allure
        allure.attach.file(
            trace_path,
            name="Playwright Trace",
            attachment_type="application/zip"
        )

    else:
        # Test passed - discard the trace
        context.tracing.stop()

    context.close()
    browser.close()


@pytest.fixture
def api_request():
    with sync_playwright() as playwright:
        request = playwright.request.new_context()
        yield request
        request.dispose()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call":
        item.test_failed = report.failed
