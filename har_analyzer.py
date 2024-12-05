import json
import re
import argparse

# Function to analyze HAR file
def analyze_har(file_path, payload_patterns):
    try:
        with open(file_path, 'r') as har_file:
            har_data = json.load(har_file)
    except Exception as e:
        print(f"Error loading HAR file: {e}")
        return

    print(f"\nAnalyzing HAR file: {file_path}")
    matches_found = False

    for entry in har_data['log']['entries']:
        request = entry['request']
        response = entry['response']
        response_content = response['content'].get('text', '')

        print(f"\nRequest URL: {request['url']}")
        print(f"Response Status: {response['status']}")

        # Search for payload patterns
        for pattern in payload_patterns:
            if re.search(pattern, response_content, re.IGNORECASE):
                print(f"  -> Match found for pattern: {pattern}")
                matches_found = True

    if not matches_found:
        print("\nNo matches found for the provided patterns.")

# Main function for command-line usage
def main():
    parser = argparse.ArgumentParser(description="Analyze HAR files for potential vulnerabilities.")
    parser.add_argument("file", help="Path to the HAR file")
    parser.add_argument(
        "-p", "--patterns", nargs="+", 
        default=["<script>alert\\(.*?\\)</script>", "javascript:.*?", "on\\w+=['\"].*?['\"]"],
        help="List of regex patterns to search for (default: common XSS payloads)"
    )
    args = parser.parse_args()

    analyze_har(args.file, args.patterns)

if __name__ == "__main__":
    main()
