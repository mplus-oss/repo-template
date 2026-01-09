import os
import shutil

REMOVED_PATH = [
    "base_app",
    "hooks",
    "templates",
    ".copier-answers.yml",
]


def cleanup():
    for pathstr in REMOVED_PATH:
        if os.path.exists(pathstr):
            if os.path.isdir(pathstr):
                shutil.rmtree(pathstr, ignore_errors=True)
            else:
                os.remove(pathstr)

        print(f"Cleaned up {pathstr}")


if __name__ == "__main__":
    cleanup()
