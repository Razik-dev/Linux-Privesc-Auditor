import subprocess

def scan_suid():
    print("\n[+] Checking SUID binaries...\n")

    result = subprocess.run(
        "find / -perm -4000 -type f 2>/dev/null",
        shell=True,
        capture_output=True,
        text=True
    )

    suid_files = result.stdout.splitlines()

    for file in suid_files:
        print(file)

    return suid_files
