import os


def tree(
    dir_path=".",
    prefix="",
    priority_files=None,
    exclude_prefixes=None,
    add_slash=False,
):
    """
    Recursively prints the directory structure as a tree

    Args:
        dir_path (str): Path of the directory to display. Defaults to the
            current directory
        prefix (str): String prefix used for printing tree branches. Used
            internally for recursion
        priority_files (list of str, optional): List of filenames that should
            appear before all others.  Defaults to ["vars.yaml",
            "my_config.yaml", "main.py"]
        exclude_prefixes (list of str, optional): List of filename prefixes to
            ignore (e.g., ".", "_").  Defaults to ["."]
        add_slash (bool, optional): Whether to add trailing slash to directories

    Behavior:
        - Prints directories and files using `├──` and `└──` connectors
        - Subdirectories are displayed recursively with indentation
        - Files starting with any prefix in `exclude_prefixes` are ignored
        - Files in `priority_files` are listed first, then the rest
            alphabetically
    """
    # Default values
    if priority_files is None:
        priority_files = ["vars.yaml", "my_config.yaml", "main.py"]
    if exclude_prefixes is None:
        exclude_prefixes = ["."]

    # Ignore files/folders starting with any of the exclude prefixes
    entries = [
        entry
        for entry in os.listdir(dir_path)
        if not any(entry.startswith(p) for p in exclude_prefixes)
    ]

    # Sort: priority files first, then the rest alphabetically
    entries.sort(key=lambda e: (0, e) if e in priority_files else (1, e.lower()))

    for i, entry in enumerate(entries):
        path = os.path.join(dir_path, entry)
        connector = "└── " if i == len(entries) - 1 else "├── "
        display_name = entry + "/" if os.path.isdir(path) and add_slash else entry
        print(prefix + connector + display_name)
        if os.path.isdir(path):
            # Recursive call for subdirectories
            tree(
                path,
                prefix + ("    " if i == len(entries) - 1 else "│   "),
                priority_files,
                exclude_prefixes,
                add_slash,
            )


if __name__ == "__main__":
    tree()
