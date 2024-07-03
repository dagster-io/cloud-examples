from setuptools import find_packages, setup

setup(
    name="location2",
    packages=find_packages(exclude=["location2_tests"]),
    install_requires=[
        "dagster",
        "dagster-cloud",
        "cowsay==4.0",
    ],
    extras_require={"dev": ["dagster-webserver", "pytest"]},
)
