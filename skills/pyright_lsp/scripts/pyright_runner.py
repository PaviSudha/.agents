import subprocess
import json
import sys
import argparse
import os

def run_pyright(path, project_root):
    """Runs pyright and returns JSON output."""
    cmd = ["pyright", "--outputjson"]
    if path:
        cmd.append(path)
    
    try:
        result = subprocess.run(
            cmd,
            cwd=project_root,
            capture_output=True,
            text=True,
            check=False # Pyright returns 1 if errors are found
        )
        
        if not result.stdout:
            print(f"Error: Pyright produced no output. Stderr: {result.stderr}")
            return None
            
        return json.loads(result.stdout)
    except Exception as e:
        print(f"Failed to run pyright: {e}")
        return None

def main():
    parser = argparse.ArgumentParser(description="Pyright Diagnostic Runner")
    parser.add_argument("--path", help="File or directory to analyze")
    parser.add_argument("--root", help="Project root directory", default=os.getcwd())
    args = parser.parse_args()

    data = run_pyright(args.path, args.root)
    if not data:
        sys.exit(1)

    diagnostics = data.get("generalDiagnostics", [])
    
    if not diagnostics:
        print("✓ No issues found.")
        return

    print(f"Found {len(diagnostics)} issues:\n")
    
    for diag in diagnostics:
        file_path = diag.get("file")
        start = diag.get("range", {}).get("start", {})
        line = start.get("line", 0) + 1
        col = start.get("character", 0) + 1
        severity = diag.get("severity", "error").upper()
        rule = diag.get("rule", "general")
        msg = diag.get("message", "")
        
        print(f"[{file_path}] [{line}:{col}] [{severity}] [{rule}] {msg}")

if __name__ == "__main__":
    main()
