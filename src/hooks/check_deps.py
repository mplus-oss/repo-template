import shutil
import sys

try:
    from _utils import load_answers
except ImportError:
    from hooks._utils import load_answers

TOOLS_MAPPING = {
    "js": [
        "node",
        "npm",
        "eslint",
    ],
    "python": [
        "python3",
        "pip",
        "python",
        "ruff",
        "pylint",
    ],
    "xml": [
        "xmllint",
    ],
}

def check_dependencies():
    print("Checking system dependencies..")

    answers = load_answers()
    selected_stacks = answers.get("langs", [])

    # Throw error if langs not created
    if len(selected_stacks) < 1:
        raise Exception("No selected language.")

    # Normalize to list if the user only selected one
    if isinstance(selected_stacks, str):
        selected_stacks = [selected_stacks]

    missing_tools = []

    for stack in selected_stacks:
        required_tools = TOOLS_MAPPING.get(stack, [])
        for tool in required_tools:
            # shutil.which returns the path if the tool exists, or None if not
            if shutil.which(tool) is None:
                missing_tools.append(tool)

    if missing_tools:
        print("\nMISSING TOOLS DETECTED [!]")
        print(
            "This template requires the following tools which "
            + "were not found in your PATH:"
        )

        for tool in missing_tools:
            print(f"  - {tool}")

        print(
            "\nPlease install these tools to ensure "
            + "linters/scripts work correctly.\n"
        )

        sys.exit(1)
    else:
        print("OK! All required tools are available.")


if __name__ == "__main__":
    check_dependencies()
