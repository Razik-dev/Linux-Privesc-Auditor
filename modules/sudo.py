import subprocess

def check_sudo():
    print("\n[+] Checking sudo configuration...\n")

    try:
        result = subprocess.run(
            ["sudo", "-l"],
            capture_output=True,
            text=True
        )

        print(result.stdout)

        if "NOPASSWD" in result.stdout:
            print("[HIGH] NOPASSWD entry found!")

        return result.stdout

    except Exception as e:
        print("Error:", e)
        return ""
