class FS:
    """Class to keep track of state when navigating through directories"""

    curr_loc = "/"
    filesystem = {}

    def cd(self, path: str):
        """Handle changing the current location based on the argument passed"""
        if path == "/":
            self.curr_loc = "/"
        elif path == "..":
            # Go up a directory.
            self.curr_loc = self.curr_loc[:self.curr_loc.rfind("/", 0, self.curr_loc.rfind("/")) + 1]
        else:
            self.curr_loc += f"{path}/"


    def ls(self, list_o_files: list[str]):
        """Take a list of files and add them to the current location as tracked in the filesystem.

        Cleans out filenames and just keeps the sizes. Leaves directories as strings.
        """
        files: list[str, int] = []
        for line in list_o_files:
            args = line.split(' ')
            if args[0] == "dir":
                files.append(args[1])
            else:
                (size, _) = args
                files.append(int(size))

        self.filesystem[self.curr_loc] = files

    def get_size_of_dir(self, path) -> int:
        """Recursively get the size of a given directory."""
        total = 0
        dir = self.filesystem.get(path)

        for item in dir:
            if isinstance(item, str):
                total += self.get_size_of_dir(path + item + '/')
            else:
                total += item

        return total


def main():
    with open('input.txt', 'r') as f:
        lines = f.readlines()

    lines = [line.replace("\n", "") for line in lines]

    # Get all lines that are considered commands, and track their original index.
    # Using this, we will be able to look forward and see when the next command happens,
    # which is useful in the case of `ls`, as commands are broken up by output.
    command_lines = [
        (index, line.replace('$ ', "")) 
        for index, line in enumerate(lines) 
        if line.startswith("$")
    ]

    fs = FS()

    for idx, (original_idx, command) in enumerate(command_lines):
        command = command.split(' ')
        if command[0] == 'cd':
            fs.cd(command[1])
        elif command[0] == 'ls':
            if len(command_lines) == idx+1:  # Special case for the end.
                ls_lines = lines[original_idx + 1:]
            else:
                next_original_idx, _ = command_lines[idx+1]
                ls_lines = lines[original_idx + 1:next_original_idx]
            fs.ls(ls_lines)

    print(f"Full filesystem: {fs.filesystem}")
    dir_sizes = [fs.get_size_of_dir(dir) for dir in fs.filesystem]
    print(f"List of sizes {dir_sizes}")
    print(f"Sum of all sizes <= 100,000: {sum([size for size in dir_sizes if size <= 100_000])}")

    total_space = 70_000_000
    needed = 30_000_000
    total_size = max(dir_sizes)

    size_of_smallest = min([size for size in dir_sizes if size >= needed - (total_space - total_size)])
    print(f"Smallest directory size to clear enough space for an update: {size_of_smallest}")

if __name__ == "__main__":
    for i in range(1000):
        main()
