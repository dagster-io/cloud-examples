from setuptools import find_packages, setup

setup(
    name="location1",
    packages=find_packages(exclude=["location1_tests"]),
    install_requires=[
        "dagster",
        "dagster-cloud",
        "cowsay==5.0",
    ],
    extras_require={"dev": ["dagster-webserver", "pytest"]},
)
