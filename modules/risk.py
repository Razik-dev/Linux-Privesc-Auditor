def print_summary(suid_count, sudo_output):
    print("\n==================================")
    print("         SECURITY SUMMARY")
    print("==================================")

    if "NOPASSWD" in sudo_output:
        print("[HIGH] Dangerous sudo configuration found")
    else:
        print("[LOW] No dangerous sudo configuration found")

    print(f"[INFO] Total SUID binaries: {suid_count}")
