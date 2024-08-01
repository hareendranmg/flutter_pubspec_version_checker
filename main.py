import sys
from typing import Any, Dict, List, Optional, Tuple

import requests
import yaml
from packaging import version


# Function to load and parse the pubspec.yaml file
def load_pubspec(file_path: str) -> Dict[str, Any]:
    """
    Load and parse a pubspec.yaml file.

    Args:
        file_path (str): Path to the pubspec.yaml file.

    Returns:
        Dict[str, Any]: Parsed contents of the pubspec.yaml file.
    """
    with open(file_path, "r") as file:
        return yaml.safe_load(file)


# Function to fetch the latest version of a package from pub.dev
def get_latest_version(package_name: str) -> Optional[str]:
    """
    Fetch the latest version of a package from pub.dev.

    Args:
        package_name (str): Name of the package to check.

    Returns:
        Optional[str]: The latest version of the package, or None if not found.
    """
    url: str = f"https://pub.dev/api/packages/{package_name}"
    response: requests.Response = requests.get(url)
    if response.status_code == 200:
        data: Dict[str, Any] = response.json()
        return data["latest"]["version"]
    return None


# Function to check package versions against the latest available versions
def check_package_versions(pubspec: Dict[str, Any]) -> List[Tuple[str, str, str]]:
    """
    Check package versions against the latest available versions.

    Args:
        pubspec (Dict[str, Any]): Parsed pubspec.yaml contents.

    Returns:
        List[Tuple[str, str, str]]: List of tuples containing (package_name, current_version, latest_version)
        for outdated packages.
    """
    dependencies: Dict[str, Any] = pubspec.get("dependencies", {})
    outdated_packages: List[Tuple[str, str, str]] = []

    for package, value in dependencies.items():
        if isinstance(value, str):
            # Remove the caret (^) from the version string if present
            current_version: str = value.lstrip("^")
            latest_version: Optional[str] = get_latest_version(package)
            if latest_version and version.parse(current_version) < version.parse(
                latest_version
            ):
                outdated_packages.append((package, current_version, latest_version))
        elif isinstance(value, dict):
            # Skip git repositories and other complex dependencies
            if "git" in value:
                print(f"Skipping git repository: {package}")
            else:
                print(f"Skipping complex dependency: {package}")

    return outdated_packages


# Main function to orchestrate the version checking process
def main(file_path: str) -> None:
    """
    Main function to check package versions in a pubspec.yaml file.

    Args:
        file_path (str): Path to the pubspec.yaml file.
    """
    pubspec: Dict[str, Any] = load_pubspec(file_path)
    outdated_packages: List[Tuple[str, str, str]] = check_package_versions(pubspec)

    if outdated_packages:
        print("Outdated packages:")
        for package, current_version, latest_version in outdated_packages:
            print(f"{package}: {current_version} -> {latest_version}")
    else:
        print("All packages are up to date!")


# Script entry point
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <path_to_pubspec.yaml>")
    else:
        main(sys.argv[1])
