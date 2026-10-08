"""Check that your machine can run every command in the workshop.

Usage (from the root of this repository):
    python3 check_setup.py
"""

from importlib.metadata import PackageNotFoundError, version
import os
import shutil
import subprocess
import sys

# (package name on PyPI, minimum version, why we need it)
PACKAGES = [
    ("numpy", None, "diabetes.py"),
    ("pandas", None, "diabetes.py"),
    ("scikit-learn", "1.4", "diabetes.py (root_mean_squared_error)"),
    ("jupyterlab", None, "diabetes.ipynb"),
    ("typer", None, "demo/ project"),
    ("loguru", None, "demo/ project"),
    ("python-dotenv", None, "demo/ project"),
    ("tqdm", None, "demo/ project"),
    ("demo", None, "demo/ project (pip install -e .)"),
]

problems = 0


def report(ok, label, detail="", required=True):
    global problems
    problems += required and not ok
    mark = "\033[32m✓\033[0m" if ok else ("\033[31m✗\033[0m" if required else "\033[33m!\033[0m")
    print(f"  {mark} {label}" + (f"  ({detail})" if detail else ""))


def as_tuple(v):
    return tuple(int(p) for p in v.split(".")[:2] if p.isdigit())


print("Python")
report(sys.version_info >= (3, 10), f"python {sys.version.split()[0]}", "need 3.10+")
in_venv = sys.prefix != sys.base_prefix or "CONDA_PREFIX" in os.environ
report(in_venv, "running inside a virtual environment", "recommended", required=False)

print("\nPackages")
for name, minimum, why in PACKAGES:
    try:
        v = version(name)
        ok = minimum is None or as_tuple(v) >= as_tuple(minimum)
        report(ok, f"{name} {v}", why if ok else f"need >= {minimum} for {why}")
    except PackageNotFoundError:
        report(False, f"{name} missing", why)

print("\nGit")
if shutil.which("git"):
    v = subprocess.run(["git", "--version"], capture_output=True, text=True).stdout.strip()
    report(True, v)
    for key in ("user.name", "user.email"):
        value = subprocess.run(
            ["git", "config", "--global", key], capture_output=True, text=True
        ).stdout.strip()
        report(bool(value), f"git config {key}", value or f'run: git config --global {key} "..."')
else:
    report(False, "git not installed", "https://git-scm.com/downloads")

print()
if problems:
    print(f"{problems} problem(s) found. See the Setup section of README.md.")
    sys.exit(1)
print("All set! See you at the workshop.")
