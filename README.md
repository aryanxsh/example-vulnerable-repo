# Example Vulnerable Repository

This is a test repository intentionally created with known vulnerable dependencies to demonstrate SBOM (Software Bill of Materials) vulnerability scanning capabilities.

## WARNING

**This repository contains intentionally vulnerable packages for testing purposes only. DO NOT use in production!**

## Purpose

This repository serves as a test case for SBOM vulnerability scanners. It includes:

- Known vulnerable package versions
- Common security vulnerabilities (XSS, SSRF, code execution, etc.)
- Real-world application structure

## Vulnerable Dependencies

The following packages have known CVEs:

| Package | Version | CVE | Vulnerability Type |
|---------|---------|-----|-------------------|
| Flask | 0.12.3 | CVE-2019-1010083 | XSS |
| requests | 2.19.1 | CVE-2018-18074 | SSRF |
| urllib3 | 1.24.3 | CVE-2019-11324 | CRLF Injection |
| PyYAML | 5.1 | CVE-2019-20477 | Code Execution |
| Jinja2 | 2.10.1 | CVE-2019-8341 | XSS |
| Werkzeug | 0.14.1 | CVE-2019-14806 | Path Traversal |
| cryptography | 2.1.4 | CVE-2018-10903 | Timing Attack |
| lxml | 4.2.5 | CVE-2019-17571 | XXE |
| Pillow | 5.2.0 | CVE-2019-6977 | DoS |
| Django | 1.11.23 | CVE-2019-6977 | Multiple |

## Usage

1. Clone this repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run the application: `python app.py`
4. Use your SBOM scanner to analyze this repository

## Expected Results

A proper SBOM vulnerability scanner should detect:
- Multiple high-severity vulnerabilities
- Outdated package versions
- Known CVE identifiers
- Risk assessment scores

## Security Notice

This repository is for educational and testing purposes only. The vulnerabilities are intentionally included to test security scanning tools. 