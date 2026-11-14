
"""Read KEY=value settings from a .env file."""

def load_env(path=".env"):
    settings = {}

    try:
        with open(path, "r", encoding="utf-8") as handle:
            for line in handle:
                line = line.strip()

                # Skip empty lines and comments
                if not line or line.startswith("#"):
                    continue

                # Skip lines without an equals sign
                if "=" not in line:
                    continue

                key, value = line.split("=", 1)

                key = key.strip()
                value = value.strip()

                # Skip empty keys
                if not key:
                    continue

                # Remove surrounding quotes
                if (
                    len(value) >= 2
                    and value[0] == value[-1]
                    and value[0] in ("'", '"')
                ):
                    value = value[1:-1]

                settings[key] = value

    except FileNotFoundError:
        print(f"Warning: {path} file not found.")

    return settings


# Example usage
config = load_env()
print(config)

=
