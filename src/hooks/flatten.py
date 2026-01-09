import os
import shutil

try:
    from _utils import load_answers
except ImportError:
    from hooks._utils import load_answers


def flatten_files():
    base_src = "base_app"

    answers = load_answers()
    selected_stacks = answers.get(base_src, [])

    # Throw error if langs not created
    if len(selected_stacks) < 1:
        raise Exception("No selected base app.")

    if isinstance(selected_stacks, str):
        selected_stacks = [selected_stacks]

    if not os.path.exists(base_src):
        print(f"{base_src} folder not found, skipping flatten.")
        return

    # Copy out the folder to root and replace if needed
    for stack in selected_stacks:
        source_folder = os.path.join(base_src, stack)

        if os.path.exists(source_folder):
            for filename in os.listdir(source_folder):
                file_path = os.path.join(source_folder, filename)
                dest_path = os.path.join(".", filename)

                if os.path.isfile(file_path):
                    # Check if file exists before moving
                    if os.path.exists(dest_path):
                        print(f"Warning: {filename} hit by {stack} (Overwriting)")
                        os.remove(dest_path)
                    shutil.move(file_path, dest_path)
                    print(f"Moved: {filename} from {stack}")

            os.rmdir(source_folder)


if __name__ == "__main__":
    flatten_files()
