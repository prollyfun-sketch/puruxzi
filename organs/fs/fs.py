"""
FS Organ
File access and resource organ for the Puruxzi Seed.

Seed-level responsibilities:
- Provide a minimal, deterministic API for file access.
- No async, no background workers.
- Kernel and other organs can call this safely.
"""

import os


class FS:
    def __init__(self, base_dir: str | None = None) -> None:
        # Base directory for all file operations.
        # Default = current working directory at seed startup.
        self.base_dir = base_dir or os.getcwd()

    # ---------------------------------------------
    # Internal helper: resolve absolute path
    # ---------------------------------------------
    def _abs_path(self, path: str) -> str:
        # If the path is already absolute, return it as-is.
        # Otherwise, join it to base_dir.
        if os.path.isabs(path):
            return path
        return os.path.join(self.base_dir, path)

    # ---------------------------------------------
    # Read file (used by Kernel.run_file_task)
    # ---------------------------------------------
    def read_file(self, path: str) -> str:
        """
        Deterministic file read.

        - Resolves path relative to base_dir if needed.
        - Returns the file contents as a string.
        - Raises standard exceptions on failure (caller can catch).
        """
        full_path = self._abs_path(path)
        with open(full_path, "r", encoding="utf-8") as f:
            return f.read()

    # (Optional) write_file stub – not used yet, but safe to keep.
    def write_file(self, path: str, data: str) -> None:
        """
        Deterministic file write (not used by the seed bridges yet).
        """
        full_path = self._abs_path(path)
        with open(full_path, "w", encoding="utf-8") as f:
            f.write(data)

    # ---------------------------------------------
    # Status
    # ---------------------------------------------
    def status(self) -> str:
        """
        Proof-of-life / status hook for the FS organ.
        """
        return f"[FS] Online (base_dir={self.base_dir})"
