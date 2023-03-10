# Developer

## Table of Contents

* [Installation](#installation)
    * [Pre-requisites](#pre-requisites)
    * [Repository](#repository)
    * [Environment](#environment)
    * [Hooks](#hooks)
* [Linting](#linting)
* [Testing](#testing)
* [Builds](#builds)

---

## Installation

### Pre-requisites

Please install the following:

1. [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
2. [Python 3.11](https://www.python.org/downloads/)

### Repository

Clone the repository:

```bash
git clone https://github.com/arabesque-sray/test-template
cd test-template
```

### Environment

Create and activate a virtual environment:

```bash
# Make sure you are using Python 3.11!
python -m venv .env
source .env/bin/activate
```

Install the requirements:

```bash
python -m pip install -r requirements.txt
python -m pip install my_fun_service/.[test]
```

### Hooks

Install the hooks:

```bash
pre-commit install
```

## Linting

To lint the project:

```bash
python -m black .
python -m flake8 .
python -m isort .
```

## Testing

To test the project:

```bash
python -m pytest -v tests
coverage run -m pytest -v tests
coverage report --omit="tests/*"
```

## Builds

To create a build for this repository you must [connect cloud build to your repository](https://cloud.google.com/build/docs/automate-builds#connect_to_your_repository) and then [create a trigger](https://cloud.google.com/build/docs/automate-builds#create_a_trigger) to let GCP know when to trigger a new build. You can [view the build](https://cloud.google.com/build/docs/automate-builds#view_build_details) as it's being created and monitor its progress.

To run a trigger manually:

```bash
# Note: This requires installing the gcloud beta component "builds"
gcloud beta builds triggers run test-template --branch=<BRANCH-NAME>
```

## Workflows

Our workflows are managed by the [data-technology-infrastructure repository](https://github.com/arabesque-sray/data-technology-infrastructure), see their explanation for how workflows are executed.
