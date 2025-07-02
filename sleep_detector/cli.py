import argparse
import os
from sleep_detector.core import find_sleep_calls
from sleep_detector.config import load_config

def main():
    parser = argparse.ArgumentParser(description="Detect sleep() calls in a codebase.")
    parser.add_argument("path", help="Root directory of the project")
    parser.add_argument("--config", help="Path to config file (TOML or JSON)", required=True)
    args = parser.parse_args()

    abs_path = os.path.abspath(args.path)
    config = load_config(args.config)

    results = find_sleep_calls(
        project_root=abs_path,
        excluded_dirs=set(config.get("excluded_dirs", [])),
        file_extensions=config.get("file_extensions", [".py"]),
        sleep_pattern=config.get("sleep_pattern", r"\b(?:time\.)?sleep\s*\(\s*(\d+(?:\.\d+)?)\s*\)")
    )

    for filepath, lineno, line in results:
        print(f"{filepath}:{lineno} => {line}")