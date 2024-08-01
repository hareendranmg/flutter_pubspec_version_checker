# Flutter Pubspec Version Checker

This Python script helps Flutter developers keep their projects up-to-date by checking if the packages listed in the `pubspec.yaml` file are using the latest available versions from pub.dev.

## Features

- Parses `pubspec.yaml` files
- Fetches the latest version information from pub.dev
- Compares current package versions with the latest available versions
- Identifies and reports outdated packages
- Skips git repository dependencies and other complex dependencies
- Provides clear output of packages that need updating

## Requirements

- Python 3.7+
- `pyyaml`
- `requests`
- `packaging`

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/hareendranmg/flutter_pubspec_version_checker.git
   cd flutter_pubspec_version_checker
   ```

2. Install the required packages:
   ```
   pip install pyyaml requests packaging
   ```

## Usage

Run the script from the command line, providing the path to your `pubspec.yaml` file as an argument:

```
python main.py path/to/your/pubspec.yaml
```

The script will output a list of outdated packages along with their current and latest versions.

## Example Output

```
Outdated packages:
http: 0.13.3 -> 0.13.4
intl: 0.17.0 -> 0.17.1
```

## Limitations

- The script only checks direct dependencies listed in the `pubspec.yaml` file.
- It does not check transitive dependencies or `dev_dependencies`.
- The script may be subject to rate limiting if too many requests are made to pub.dev in a short period.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).
