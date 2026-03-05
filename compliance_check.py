# Simulates a basic compliance check
controls = {
    "MFA Enabled": True,
    "Encryption at Rest": True,
    "Logging Enabled": False,
    "Patch Level Current": True,
}

def run_checks(controls):
    failed = [k for k, v in controls.items() if not v]
    if failed:
        print(f"COMPLIANCE FAILURES: {failed}")
        exit(1)
    else:
        print("All compliance checks passed.")

run_checks(controls)