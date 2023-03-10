from setuptools import find_packages, setup

setup(
    name="my_fun_service",
    version="4.20",
    description="This is a description of my fun service.",
    author="Data Technology",
    maintainer="Data Technology",
    maintainer_email="data_technology@esgbook.com",
    license="Arabesque S-Ray GmbH",
    packages=find_packages(),
    extras_require={
        "test": [
            "pre-commit",
            "pre-commit-hooks",
            "black",
            "flake8",
            "isort",
            "pytest",
            "coverage",
        ]
    },
)
