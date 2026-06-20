from modules.suid import scan_suid
from modules.sudo import check_sudo
from modules.risk import print_summary
from modules.writable import scan_writable
from modules.report import generate_report

print("""
==================================
 Linux Privilege Escalation Auditor
==================================
""")

suid_files = scan_suid()

print(f"\nFound {len(suid_files)} SUID binaries")

sudo_output = check_sudo()

writable_files = scan_writable()

generate_report(
    len(suid_files),
    len(writable_files)
)

print_summary(len(suid_files), sudo_output)
