def generate_report(suid_count, writable_count):
    html = f"""
    <html>
    <head>
        <title>Linux Privilege Escalation Report</title>
    </head>
    <body>
        <h1>Security Assessment Report</h1>

        <h2>Summary</h2>

        <p>SUID Binaries Found: {suid_count}</p>
        <p>World Writable Files Found: {writable_count}</p>

    </body>
    </html>
    """

    with open("reports/report.html", "w") as f:
        f.write(html)

    print("\n[+] Report saved to reports/report.html")
