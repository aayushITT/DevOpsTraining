from setuptools import setup, find_packages

setup(
    name="disk-usage-checker",
    version="0.1",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "diskcheck=disk_checker.cli:main",
        ],
    },
    author="Aayush Sharma",
    description="CLI tool to check disk usage and print if usage exceeds a given threshold.",
)