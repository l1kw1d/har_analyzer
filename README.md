# HAR Analyzer Script

![Python Version](https://img.shields.io/badge/python-3.7%2B-blue)  
![License](https://img.shields.io/badge/license-MIT-green)  
![Status](https://img.shields.io/badge/status-Active-brightgreen)

A command-line tool for analyzing HTTP Archive (HAR) files to detect potential vulnerabilities, such as reflected XSS and other injection attacks. Ideal for security researchers, penetration testers, and developers looking to identify and mitigate security flaws in web applications.

---

## Features

- **Payload Detection**: Search for common and complex attack payloads using regex patterns.
- **Customizable**: Specify custom payloads via command-line arguments for tailored analysis.
- **Detailed Output**:
  - Extract and display HTTP request/response details.
  - Highlight matched payloads for quick identification.
- **Regex Matching**: Supports advanced pattern matching for vulnerabilities like:
  - XSS (`<script>`, `on*` attributes).
  - URL-based injections (`javascript:`, `data:` schemes).
- **Lightweight**: Minimal dependencies, simple setup, and fast execution.

---

## Installation

### Prerequisites
- **Python**: Version 3.7 or higher.
- **pip**: Package manager for Python.

## Usage

### Basic Usage

Run the script with a HAR file:
```bash
python har_analyzer.py path/to/file.har
```
# Search for Custom Payloads
You can provide specific regex patterns to match against the HAR data:
```bash
python har_analyzer.py path/to/file.har -p "<script>alert\(\".*?\"\)</script>" "java"
```
# Help Menu
Access the help menu to view all options and usage details:
```bash
python har_analyzer.py --help
```
# Example Output
Here’s an example output for a detected vulnerability:
```bash
Analyzing HAR file: example.har

Request URL: http://example.com/vulnerable
Response Status: 200
  -> Match found for pattern: <script>alert\(.*?\)</script>

```
# File Structure
```bash
har-analyzer/
├── har_analyzer.py       # Main Python script for HAR analysis
├── requirements.txt      # (Optional) Dependencies list
├── README.md             # Project documentation
└── example.har           # Sample HAR file for testing (optional)
```
# Development
Planned Features
* Add support for batch processing of multiple HAR files.
* Export matched results to CSV or JSON.
* Expand regex patterns for advanced attack types (e.g., SQLi, CSRF).

# Contributing
I welcome contributions! To contribute:
 1. Fork the repository.
 2. Create a features branch:
    ```bash
    git checkout -b feature-name
    ```
 3. Commit your changes:
    ```bash
    git commit -m "Add feature"
    ```
 4. Push to your fork:
    ```bash
    git push origin feature-name
    ```
 5. Submit a pull request to the main branch.
