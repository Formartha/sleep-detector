import os
import json
import toml

def load_config(config_path):
    if not config_path or not os.path.exists(config_path):
        raise FileNotFoundError("Configuration file is required via --config")

    if config_path.endswith(".toml"):
        return toml.load(config_path)
    elif config_path.endswith(".json"):
        with open(config_path, "r", encoding="utf-8") as f:
            return json.load(f)
    else:
        raise ValueError("Unsupported config format. Use TOML or JSON.")
