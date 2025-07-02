
from setuptools import setup, find_packages

setup(
    name="sleep-detector",
    version="0.1.0",
    description="Detects sleep() calls in your codebase",
    author="Mor Dabastany",
    author_email='morpci@gmail.com',
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "sleep-detector=sleep_detector.cli:main",
        ],
    },
    install_requires=["toml"],
    python_requires=">=3.7",
)
