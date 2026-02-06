import os
import subprocess
import sys

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

SCRIPTS = [
    "translate_urdf_csv.py",
    "fix_motor_name.py",
    "fix_step_filenames.py",
    "fix_stp_files.py",
    "translate_stl_files.py",
    "translate_pptx.py",
    "translate_pdfs_with_overlay.py",
]

def run_script(script_name: str) -> None:
    script_path = os.path.join(ROOT_DIR, "scripts", script_name)
    if not os.path.exists(script_path):
        raise FileNotFoundError(f"Missing script: {script_path}")

    print(f"\n{'=' * 70}\nRunning: {script_name}\n{'=' * 70}")
    result = subprocess.run(
        [sys.executable, script_path],
        cwd=ROOT_DIR,
        check=False,
        text=True,
    )
    if result.returncode != 0:
        raise RuntimeError(f"{script_name} failed with exit code {result.returncode}")


def main() -> None:
    for script in SCRIPTS:
        run_script(script)
    print("\nAll scripts completed successfully.")


if __name__ == "__main__":
    main()
