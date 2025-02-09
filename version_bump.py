import re
from pathlib import Path
from typing import Union


def bump_version(pyproject_path: Union[str, Path]) -> int:
    """Bump the patch version in pyproject.toml.

    Args:
        pyproject_path: Path to pyproject.toml file

    Returns:
        0 if successful, 1 if error
    """
    pyproject = Path(pyproject_path)
    if not pyproject.exists():
        return 1

    content = pyproject.read_text()
    version_pattern = r'(version\s*=\s*["\'])(\d+\.\d+\.)(\d+)(["\'])'

    def increment_version(match: re.Match) -> str:
        prefix, major_minor, patch, suffix = match.groups()
        new_patch = int(patch) + 1
        return f"{prefix}{major_minor}{new_patch}{suffix}"

    new_content = re.sub(version_pattern, increment_version, content)
    pyproject.write_text(new_content)
    return 0


if __name__ == "__main__":
    exit(bump_version("pyproject.toml"))
