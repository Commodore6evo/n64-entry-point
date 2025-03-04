# save as entrypoint.py
import struct
import sys

if len(sys.argv) != 2:
    print("Usage: entrypoint.py <rom_file>")
    sys.exit(1)

rom_file = sys.argv[1]

try:
    with open(rom_file, "rb") as f:
        f.seek(0x8)
        entry_point = struct.unpack(">I", f.read(4))[0]
        print(hex(entry_point))
except FileNotFoundError:
    print(f"Error: File '{rom_file}' not found.")
    sys.exit(1)
except Exception as e:
    print(f"An error occurred: {e}")
    sys.exit(1)