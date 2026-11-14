
"""Read KEY=value settings from a .env file."""

def load_env(path=".env"):
    settings = {}

<<<<<<< HEAD
    with open(path) as handle:
        for line in handle:
            line = line.strip()

            if not line or line.startswith("#"):
                continue

            key, _, value = line.partition("=")
            settings[key.strip()] = value.strip()

    return settings
=======
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
>>>>>>> f04097acf2f955f0a76336be8735549f5b425677
