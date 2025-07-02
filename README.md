<p align="center"><img src=".readme/sleeper.png" alt="cover" width="220"></p>

A CLI tool that scans your source code project for calls to `sleep(...)`, aimed to find hidden bottlenecks.

## Installation

```bash
pip install sleep-detector
```

## Usage

```bash
sleep-detector /path/to/your/codebase --config sleep_detector.toml
```

## Configuration

You must supply a configuration file to specify:

- Which directories to exclude
- Which file extensions to scan
- What regex pattern to match

### Example: `sleep_detector.toml`

```toml
excluded_dirs = ["venv", ".git", "build", "__pycache__"]
file_extensions = [".py"]
sleep_pattern = "\\b(?:time\\.)?sleep\\s*\\(\\s*(\\d+(?:\\.\\d+)?)\\s*\\)"
```

Run the tool:

```bash
sleep-detector . --config sleep_detector.toml
```
