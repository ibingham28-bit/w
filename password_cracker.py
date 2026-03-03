from pathlib import Path
from zipfile import BadZipFile, ZipFile
import zlib


ROOT = Path(__file__).resolve().parent
ZIP_PATH = ROOT / "whitehouse_secrets.zip"

# Support either repo-root or img/ placement for the leaked passwords file.
PASSWORD_FILE_CANDIDATES = [
    ROOT / "Ashley-Madison.txt",
    ROOT / "img" / "Ashley-Madison.txt",
]


def find_password_file() -> Path:
    for candidate in PASSWORD_FILE_CANDIDATES:
        if candidate.exists():
            return candidate
    raise FileNotFoundError("Could not find Ashley-Madison.txt")


def load_passwords(password_file: Path) -> list[str]:
    with password_file.open(encoding="ascii", errors="ignore") as f:
        return [line.rstrip("\n\r") for line in f if line.strip()]


def main() -> None:
    password_file = find_password_file()
    passwords = load_passwords(password_file)
    print(f"Loaded {len(passwords)} passwords from {password_file}")

    for i, password in enumerate(passwords):
        if i % 10000 == 0:
            print(f"i={i} password={password}")
        try:
            with ZipFile(ZIP_PATH) as zf:
                zf.extractall(path=ROOT, pwd=password.encode("ascii"))
            print(f"FOUND PASSWORD: {password}")
            return
        except (RuntimeError, BadZipFile, zlib.error):
            continue

    print("No password found.")


if __name__ == "__main__":
    main()
