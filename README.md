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
#Web security scanner
# Search for Custom Payloads
You can provide specific regex patterns to match against the HAR data:
```bash
python har_analyzer.py path/to/file.har -p "<script>alert\(\".*?\"\)</script>" "java"
```
