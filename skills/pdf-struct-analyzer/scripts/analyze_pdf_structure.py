import os
import sys
import re
import subprocess

def convert_pdf_to_md(pdf_path):
    md_path = os.path.splitext(pdf_path)[0] + ".md"
    print(f"Converting {pdf_path} to {md_path}...")
    try:
        subprocess.run(["markitdown", pdf_path, "-o", md_path], check=True)
        return md_path
    except subprocess.CalledProcessError as e:
        print(f"Error during conversion: {e}")
        return None
    except FileNotFoundError:
        print("Error: 'markitdown' not found. Please install it with 'pip install markitdown'.")
        return None

def extract_structure(md_path):
    with open(md_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    tree = []
    # Improved patterns to capture Roman numeral headers (I, II, III, IV)
    patterns = [
        r'^#+ .*',                                # Markdown headers
        r'^([IVXLCDM]+\.)\s*[A-Z].*',             # Roman numeral sections
        r'^(\d+|\d+\.\d+|\d+\.\d+\.\d+)\s+[A-Z].*', # Numbered sections
        r'^[A-Z][a-z]+:'                          # Key nodes
    ]
    
    # Filter out bibliography and noisy footer patterns
    ref_pattern = r'^[0-9]+ [A-Z][a-z]+ [A-Z][a-z]+,.*'
    footer_pattern = r'^\d+\s+VOLUME\s+\d+,\s+\d+.*' # Catch "[Page] VOLUME X, Y"

    for line in lines:
        line = line.strip()
        if any(re.match(p, line) for p in patterns):
            if not re.match(ref_pattern, line) and not re.match(footer_pattern, line):
                # Calculate depth
                depth = 0
                if line.startswith('#'):
                    depth = line.count('#') - 1
                elif '.' in line.split(' ')[0]:
                    depth = line.split(' ')[0].count('.')
                elif re.match(r'^[IVXLCDM]+\.', line):
                    depth = 0
                
                # Detect suspected interleaved text (e.g., long line with lowercase in middle)
                flag = ""
                if len(line) > 60 and re.search(r'[a-z][A-Z]', line):
                    flag = " [!] REPAIR REQUIRED: Interleaved Columns Detected"
                
                tree.append("  " * depth + "└── " + line + flag)
                
    return tree

def detect_columns(pdf_path):
    # Read the first page with layout
    try:
        raw_text = subprocess.check_output(["pdftotext", "-f", "1", "-l", "1", pdf_path, "-"], encoding='utf-8')
        # Check for large gaps in the middle of lines which typically indicate columns
        lines = raw_text.split('\n')
        multi_column_lines = 0
        for line in lines:
            if re.search(r'\s{10,}', line): # Look for gaps of 10+ spaces
                multi_column_lines += 1
        
        return multi_column_lines > 5 # If more than 5 lines have large gaps, it's likely multi-column
    except Exception:
        return False

def main():
    if len(sys.argv) < 2:
        print("Usage: python analyze_pdf_structure.py <pdf_path>")
        sys.exit(1)

    pdf_path = sys.argv[1]
    if not os.path.exists(pdf_path):
        print(f"Error: File {pdf_path} not found.")
        sys.exit(1)

    is_multi = detect_columns(pdf_path)
    if is_multi:
        print("!!! WARNING: Multi-column layout detected. Structural alignment may be affected. !!!")
        print("Tip: Use 'pdftotext -layout' for manual extraction if the MD structure looks interleaved.\n")

    md_path = convert_pdf_to_md(pdf_path)
    if md_path:
        tree = extract_structure(md_path)
        print("\n# PDF Document Structure Tree\n")
        for node in tree:
            print(node)

if __name__ == "__main__":
    main()
