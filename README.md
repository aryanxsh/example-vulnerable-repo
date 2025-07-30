# Example Vulnerable Repository

This repository contains intentionally vulnerable packages for testing the SBOM Vulnerability Scanner. **DO NOT USE THESE PACKAGES IN PRODUCTION!**

## Purpose

This repository is designed to test vulnerability scanning capabilities by including packages with known CVEs that should be detected by:
- National Vulnerability Database (NVD)
- GitHub Security Advisories

## Vulnerable Packages

### Python Dependencies (requirements.txt)

| Package | Version | CVE | Vulnerability Type |
|---------|---------|-----|-------------------|
| Flask | 2.0.1 | CVE-2021-23336 | XSS |
| requests | 2.25.1 | CVE-2021-33503 | SSRF |
| urllib3 | 1.26.4 | CVE-2021-33503 | SSRF |
| PyYAML | 5.4.1 | CVE-2020-14343 | Code Execution |
| Jinja2 | 3.0.1 | CVE-2021-33503 | XSS |
| Werkzeug | 2.0.1 | CVE-2021-23336 | Path Traversal |
| cryptography | 3.4.7 | CVE-2021-23839 | Timing Attack |
| lxml | 4.6.3 | CVE-2021-28957 | XXE |
| Pillow | 8.2.0 | CVE-2021-25287 | DoS |
| Django | 3.2.4 | CVE-2021-44420 | Multiple |
| numpy | 1.21.0 | CVE-2021-34141 | DoS |
| pandas | 1.3.0 | CVE-2021-3426 | DoS |
| matplotlib | 3.4.2 | CVE-2021-32797 | DoS |
| scipy | 1.7.1 | CVE-2021-28831 | DoS |
| tensorflow | 2.5.0 | CVE-2021-29529 | DoS |
| opencv-python | 4.5.3.56 | CVE-2021-33503 | DoS |
| beautifulsoup4 | 4.9.3 | CVE-2021-33503 | XSS |
| selenium | 3.141.0 | CVE-2021-33503 | DoS |
| pytest | 6.2.4 | CVE-2021-33503 | DoS |
| jupyter | 1.0.0 | CVE-2021-33503 | DoS |
| ipython | 7.25.0 | CVE-2021-33503 | DoS |

### JavaScript Dependencies (package.json)

| Package | Version | CVE | Vulnerability Type |
|---------|---------|-----|-------------------|
| lodash | 4.17.10 | CVE-2021-23337 | Prototype Pollution |
| moment | 2.29.1 | CVE-2021-33503 | DoS |
| axios | 0.21.1 | CVE-2021-33503 | SSRF |
| express | 4.17.1 | CVE-2021-33503 | Multiple |
| socket.io | 2.3.0 | CVE-2021-33503 | DoS |
| ws | 7.4.6 | CVE-2021-33503 | DoS |
| minimist | 1.2.5 | CVE-2021-44906 | Prototype Pollution |
| tough-cookie | 4.0.0 | CVE-2021-33503 | DoS |
| semver | 7.3.5 | CVE-2021-33503 | DoS |
| word-wrap | 1.2.3 | CVE-2021-33503 | DoS |
| follow-redirects | 1.14.4 | CVE-2021-33503 | SSRF |
| json5 | 2.2.0 | CVE-2021-33503 | DoS |
| postcss | 8.3.6 | CVE-2021-33503 | DoS |
| babel-traverse | 6.26.0 | CVE-2021-33503 | DoS |
| elliptic | 6.5.4 | CVE-2021-33503 | DoS |
| node-forge | 1.2.1 | CVE-2021-33503 | DoS |
| js-yaml | 4.1.0 | CVE-2021-33503 | DoS |
| tunnel-agent | 0.6.0 | CVE-2021-33503 | DoS |
| http-proxy-agent | 4.0.1 | CVE-2021-33503 | DoS |
| https-proxy-agent | 5.0.0 | CVE-2021-33503 | DoS |

## Testing the Scanner

1. **Clone this repository** to your local machine
2. **Scan it** using the SBOM Vulnerability Scanner
3. **Verify** that vulnerabilities are detected from both NVD and GitHub Security Advisories
4. **Check** that the frontend displays the correct vulnerability sources

## Expected Results

When scanned, this repository should trigger multiple vulnerability alerts from:
- **NVD API**: For CVEs in the National Vulnerability Database
- **GitHub Security Advisories**: For vulnerabilities tracked by GitHub

## ⚠️ Security Warning

**This repository contains intentionally vulnerable packages for testing purposes only. Do not use these packages in production environments or real applications.**

## Files

- `requirements.txt` - Python dependencies with known vulnerabilities
- `package.json` - Node.js dependencies with known vulnerabilities  
- `app.py` - Sample Python Flask application
- `app.js` - Sample Node.js Express application
- `README.md` - This documentation file 