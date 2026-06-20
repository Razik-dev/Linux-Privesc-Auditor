import subprocess

def scan_writable():
    print("\n[+] Checking world-writable files...\n")

    command = """
    find / \
    -path /proc -prune -o \
    -path /sys -prune -o \
    -path /run -prune -o \
    -type f -perm -0002 -print 2>/dev/null
    """

    result = subprocess.run(
        command,
        shell=True,
        capture_output=True,
        text=True
    )

    files = result.stdout.splitlines()

    for file in files[:20]:
        print(file)

    print(f"\nFound {len(files)} world-writable files")

    return files
