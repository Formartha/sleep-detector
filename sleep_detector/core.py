import os
import re

def find_sleep_calls(project_root, excluded_dirs, file_extensions, sleep_pattern):
    pattern = re.compile(sleep_pattern)
    results = []

    def should_exclude(dirpath):
        return any(part in excluded_dirs for part in dirpath.split(os.sep))

    for root, dirs, files in os.walk(project_root):
        dirs[:] = [d for d in dirs if d not in excluded_dirs]
        if should_exclude(root):
            continue

        for file in files:
            if any(file.endswith(ext) for ext in file_extensions):
                filepath = os.path.join(root, file)
                try:
                    with open(filepath, "r", encoding="utf-8") as f:
                        for lineno, line in enumerate(f, start=1):
                            match = pattern.search(line)
                            if match:
                                results.append((filepath, lineno, line.strip()))
                except Exception as e:
                    results.append((filepath, -1, f"ERROR: {e}"))

    return results
