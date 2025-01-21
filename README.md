
# DeadZone - Shell Status Finder

**DeadZone** is a Python-based tool designed to check the validity of URLs by determining whether they are live or dead. It can test individual URLs or process a file containing multiple URLs, making it ideal for security researchers, web admins, and developers to quickly assess the availability of multiple web resources.

**Key Features:**
- Check if a URL is live or dead.
- Handle redirects and network errors.
- Custom User-Agent to avoid being blocked.
- Results are stored in a CSV file.
- Handles both single and batch URL testing.
- Compatible with both Windows and Linux.
- User-friendly command-line interface with colorful output.

---

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
  - [Test a Single Link](#test-a-single-link)
  - [Test Links from a File](#test-links-from-a-file)
- [Dependencies](#dependencies)
- [License](#license)
- [Disclaimer](#disclaimer)
- [Contact](#contact)

---

## Installation

To use **DeadZone**, you need to have Python installed on your machine. You can install the required dependencies using `pip`.

1. Clone the repository:
   ```bash
   git clone https://github.com/HackfutSec/DeadZone.git
   cd DeadZone
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

   The `requirements.txt` file includes the following libraries:
   - `requests`
   - `pystyle`
   - `csv`
   - `time`
   - `logging`
   - `os`
   - `sys`

---

## Usage

Once you have the dependencies installed, you can run **DeadZone** to check URLs.

### Test a Single Link

1. Run the program:
   ```bash
   python deadzone.py
   ```

2. Select option 1 from the menu to test a single URL.

3. Enter the URL you want to check:
   ```
   [] Enter the URL to test: https://example.com
   ```

4. The program will output the status, HTTP code, and response time for the URL.

### Test Links from a File

1. Prepare a text file (e.g., `urls.txt`) with one URL per line.
2. Run the program:
   ```bash
   python deadzone.py
   ```

3. Select option 2 from the menu to test URLs from the file.

4. Enter the path to the file containing the URLs:
   ```
   [] Enter the file path containing the links: /path/to/urls.txt
   ```

5. The results will be saved in `link_status.csv`, where each line will contain the URL, status (live or dead), HTTP code, and response time.

---

## Dependencies

**DeadZone** requires the following dependencies:

- `requests`: For sending HTTP requests to check the status of URLs.
- `pystyle`: For colorizing the output to make it more user-friendly.

You can install all the dependencies using the following command:
```bash
pip install -r requirements.txt
```

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Disclaimer

**DeadZone** is provided "as-is" without any warranty of any kind, either expressed or implied. The creator of this software is not responsible for any misuse, damages, or legal issues arising from its usage. 

This tool is for educational purposes only and should be used with permission from the owner of the URLs or domains that you are testing. Unauthorized access or scanning of websites or servers can be illegal and unethical. Use at your own risk.

---

## Contact

If you have any questions, feel free to contact the creator:

- **Telegram**: [@H4ckfutSec](https://t.me/H4ckfutSec)
- **GitHub**: [HackfutSec](https://github.com/HackfutSec)
- **Email**: hackfutsec@protonmail.com

---

### Screenshot

Here is a sample output from the **DeadZone** tool:

```
[] Menu:
1. Test a single link
2. Test a file containing links
3. Quit

[] Choose an option (1, 2, 3): 1
[] Enter the URL to test: https://example.com
https://example.com - live (Code: 200, Response Time: 0.21s)
```

