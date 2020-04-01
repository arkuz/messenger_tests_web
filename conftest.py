import os
import pytest
from helpers.tools import prepare_screenshot_name


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):

    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            fn = report.nodeid
            fn = prepare_screenshot_name(fn)
            if fn:
                path = os.path.basename(fn)
                html = f'<div><img src="{path}" alt="screenshot" style="width:600px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>'
                extra.append(pytest_html.extras.html(html))
        report.extra = extra
