English | [Polski](README_PL.md) | [Français](README_FR.md)
# Postman Echo API Tests

[![Python application](https://github.com/dariamikitaninets-web/postman-echo-tests/actions/workflows/python-app.yml/badge.svg)](https://github.com/dariamikitaninets-web/postman-echo-tests/actions/workflows/python-app.yml)
[![Tests + Allure report](https://github.com/dariamikitaninets-web/postman-echo-tests/actions/workflows/allure.yml/badge.svg)](https://github.com/dariamikitaninets-web/postman-echo-tests/actions/workflows/allure.yml)

Automated API test suite for the public **Postman Echo** service, implemented with Python, `requests`, and `pytest`. The project verifies how GET and POST requests are reflected in JSON responses and demonstrates a complete QA workflow: API exploration, automated assertions, CI execution, intentional failure validation, recovery, and Allure reporting.

## Project purpose

The project was created to practise and demonstrate:

- REST API testing with different request types and payload formats;
- verification of HTTP status codes and JSON response content;
- automated API testing with `pytest` and `requests`;
- dependency management through `requirements.txt`;
- CI execution with GitHub Actions;
- controlled CI validation using a successful–failed–successful sequence;
- generation and publication of an Allure test report.

Before automation, the behaviour of the `/get` and `/post` endpoints was explored in Postman. The observed responses were then converted into automated checks.

## Test coverage

The suite currently contains **6 automated tests**.

| Test | Request | Main validations |
|---|---|---|
| `test_get_no_params_status_and_url` | `GET /get` without parameters | Status `200`, expected URL, empty `args` object |
| `test_get_with_query_params_echoed_in_args` | `GET /get` with query parameters | Status `200`, echoed parameters, query string in the returned URL |
| `test_get_with_headers_echoed` | `GET /get` with a custom header | Status `200`, custom header returned in the response headers |
| `test_post_json_body_echoed_in_json_field` | `POST /post` with JSON | Status `200`, JSON payload echoed in the `json` field, non-empty `data` |
| `test_post_form_urlencoded_echoed_in_form` | `POST /post` with form data | Status `200`, form payload echoed in the `form` field |
| `test_post_raw_text_echoed_in_data` | `POST /post` with raw text | Status `200`, raw text echoed in the `data` field |

Every HTTP request uses a timeout to prevent the test run from waiting indefinitely for the external service.

## Technology stack

- Python
- Pytest
- Requests
- Postman
- Allure Pytest
- Git and GitHub
- GitHub Actions
- GitHub Pages
- Flake8

## Project structure

```text
postman-echo-tests/
├── .github/
│   └── workflows/
│       ├── allure.yml
│       └── python-app.yml
├── pytest.ini
├── requirements.txt
├── test_echo.py
├── README.md
├── README_PL.md
└── README_FR.md
```

### Main files

- `test_echo.py` — automated GET and POST API tests with Allure titles, descriptions, and steps.
- `requirements.txt` — pinned Python dependencies required by the project.
- `pytest.ini` — pytest discovery and execution configuration.
- `.github/workflows/python-app.yml` — standard CI workflow with dependency installation, Flake8 checks, and pytest execution.
- `.github/workflows/allure.yml` — test execution, Allure report generation, and deployment to GitHub Pages.

## Installation

Python 3.10 or newer is required.

```bash
git clone https://github.com/dariamikitaninets-web/postman-echo-tests.git
cd postman-echo-tests

python -m venv .venv
source .venv/bin/activate
```

On Windows:

```powershell
.venv\Scripts\activate
```

Install the dependencies:

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Running the tests

Run the complete suite:

```bash
pytest
```

Run it in quiet mode:

```bash
pytest -q
```

Run a single test:

```bash
pytest test_echo.py::test_post_json_body_echoed_in_json_field
```

## Allure report

Generate Allure result files locally:

```bash
pytest -q --alluredir=allure-results
```

After installing the Allure command-line tool, open the report locally:

```bash
allure serve allure-results
```

The report published by GitHub Actions is available here:

[Open the Allure report](https://dariamikitaninets-web.github.io/postman-echo-tests/)

## Continuous Integration

Two GitHub Actions workflows are configured.

### Python application

Triggered on:

- pushes to `main`;
- pull requests targeting `main`.

The workflow:

1. checks out the repository;
2. configures Python 3.10;
3. installs project dependencies;
4. runs Flake8 checks;
5. executes the test suite with pytest.

### Tests + Allure report

Triggered on:

- pushes to `main`;
- manual workflow dispatch.

The workflow:

1. configures Python 3.12;
2. installs the dependencies;
3. runs pytest and generates Allure results;
4. configures Java 17 and the Allure CLI;
5. generates the HTML report;
6. publishes the report through GitHub Pages.

## CI failure and recovery demonstration

The repository contains a deliberate CI experiment required by the assignment:

1. [Successful CI run](https://github.com/dariamikitaninets-web/postman-echo-tests/actions/runs/25228565312) — the initial workflow executed successfully.
2. [Intentional failure](https://github.com/dariamikitaninets-web/postman-echo-tests/actions/runs/25228805351) — an assertion was deliberately broken and the workflow failed.
3. [Successful recovery](https://github.com/dariamikitaninets-web/postman-echo-tests/actions/runs/25228850108) — the test was corrected and CI returned to a successful state.

This sequence demonstrates that the pipeline detects a real regression and confirms the fix after correction.

## Skills demonstrated

- API request analysis in Postman;
- GET and POST request automation;
- query parameter, header, JSON, form, and raw body validation;
- HTTP status and response body assertions;
- test structuring with pytest;
- timeout handling for external API calls;
- CI configuration and troubleshooting;
- deliberate failure injection and regression recovery;
- Allure reporting and GitHub Pages deployment;
- basic static analysis with Flake8.

## Limitations

The tests depend on the availability and behaviour of the public Postman Echo service. They validate the response fields used by the current scenarios but do not yet include JSON Schema validation, retries, or mocked responses.

## Author

**Daria Mikitaninets**

QA portfolio project focused on API test automation and Continuous Integration.
