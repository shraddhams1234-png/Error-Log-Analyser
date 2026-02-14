# analyzer.py
# Simple Error Log Analyzer

def analyze_log(file_path):
    errors = {}
    with open(file_path, "r") as f:
        for line in f:
            if "ERROR" in line:
                error_type = line.strip()
                errors[error_type] = errors.get(error_type, 0) + 1
    
    print("\n--- Error Report ---")
    for error, count in errors.items():
        print(f"{error}: {count} t")


if __name__ == "__main__":
    log_file = input("Enter log file path: ")
    analyze_log(log_file)
