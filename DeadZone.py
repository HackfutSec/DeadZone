import requests
import csv
import time
import logging
import os
import sys
from pystyle import Colors, Colorate, Center


# Clear screen based on OS
if os.name == "nt":  # Check if the OS is Windows
    os.system("cls")  # Clear the screen for Windows OS
else:
    os.system("clear")  # Clear the screen for Unix-like OS


class bcolors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BLUE = '\033[34m'

"""
          #Contact : t.me/H4ckfutSec
          #Github  : https://github.com/HackfutSec
          #License : MIT  
          [Warning] I am not responsible for the way you will use this program [Warning]
"""

# Descriptions and banners with colored text
banner = """
         .-.
       .'   `.          ------------------------------
       :g g   :         | GHOST - Shell Status Finder |
       : o    `.        |       @CODE BY HackFut     |
      :         ``.     ------------------------------
     :             `.
    :  :         .   `.
    :   :          ` . `.
     `.. :            `. ``;
        `:;             `:' 
           :              `.
            `.              `.     . 
              `'`'`'`---..,___`;.-'
"""

description = """
         GHOST - Shell Status Finder is a tool designed to check the validity of URLs, 
         determining whether they are live or dead. It can test a single URL or a file containing multiple URLs. 
         Results are saved in a CSV file, including status, HTTP code, and response time. 
         The program handles network errors and redirects while using a custom User-Agent to avoid being blocked. 
         It is compatible with both Windows and Linux and offers an interactive user interface.
         """

print(Colorate.Horizontal(Colors.red_to_yellow, Center.XCenter(banner)))
print(Colorate.Horizontal(Colors.blue_to_green, Center.XCenter(description)))


# Configure logging
logging.basicConfig(filename='link_check_errors.log', level=logging.ERROR, format='%(asctime)s - %(message)s')

# Add a custom User-Agent in headers
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

def check_link_status(url, retries=3, delay=1):
    """
    Checks whether the link is live or dead, handling redirects and network errors.
    """
    try:
        # Multiple attempts in case of temporary failures (timeout, network error)
        for _ in range(retries):
            try:
                response = requests.get(url, timeout=10, allow_redirects=True, headers=HEADERS)
                
                # Check HTTP status codes
                if response.status_code == 200:
                    return "live", response.status_code, response.elapsed.total_seconds()
                elif 300 <= response.status_code < 400:
                    # Redirection, we consider it "live"
                    return "live (redirect)", response.status_code, response.elapsed.total_seconds()
                else:
                    return "died", response.status_code, response.elapsed.total_seconds()
            
            except requests.exceptions.RequestException as e:
                # If network error, log and retry
                logging.error(f"Error for {url}: {e}")
                time.sleep(delay)  # Wait before retrying

        # If it fails after multiple attempts, consider it dead
        return "died", "N/A", None

    except Exception as e:
        # Handle unexpected exceptions
        logging.error(f"\n[] Unexpected error for {url}: {e}")
        return "died", "N/A", None

def check_links_from_file(file_path, output_file):
    """
    Reads a file containing URLs, checks each link, and classifies them in a CSV file with more details.
    """
    with open(file_path, 'r') as file:
        urls = file.readlines()

    # Open the CSV file to save results
    with open(output_file, mode='w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['URL', 'Status', 'HTTP Code', 'Response Time (s)'])  # CSV file header
        
        # Check each URL
        for url in urls:
            url = url.strip()  # Remove whitespace around the URL
            if url:
                status, code, response_time = check_link_status(url)  # Check the link status
                # Handle None value for response_time
                if response_time is not None:
                    response_time = f"{response_time:.2f}s"
                else:
                    response_time = "N/A"
                
                writer.writerow([url, status, code, response_time])  # Save result in CSV file
                
                # Print the result with color handling
                if status == "live":
                    print(Colorate.Vertical(Colors.green_to_blue, f"{url} - {status} (Code: {code}, Response Time: {response_time})"))
                else:
                    print(Colorate.Vertical(Colors.red_to_yellow, f"{url} - {status} (Code: {code}, Response Time: {response_time})"))

def test_single_link():
    """
    Prompts the user to enter a single URL to test.
    """
    url = input("\n[] Enter the URL to test: ")
    if url:
        status, code, response_time = check_link_status(url)  # Check the link status
        # Handle None value for response_time
        if response_time is not None:
            response_time = f"{response_time:.2f}s"
        else:
            response_time = "N/A"
        
        # Print the result with color handling
        if status == "live":
            print(Colorate.Vertical(Colors.green_to_blue, f"{url} - {status} (Code: {code}, Response Time: {response_time})"))
        else:
            print(Colorate.Vertical(Colors.red_to_yellow, f"{url} - {status} (Code: {code}, Response Time: {response_time})"))
    else:
        print(Colorate.Vertical(Colors.red_to_yellow, "\n[] Invalid URL!"))

def menu():
    """
    Displays the menu and handles user choices.
    """
    while True:
        print("\n" + Colorate.Vertical(Colors.blue_to_green, "\n[] Menu:\n\n"))
        print(Colorate.Vertical(Colors.green_to_blue, "1. Test a single link"))
        print(Colorate.Vertical(Colors.green_to_blue, "2. Test a file containing links"))
        print(Colorate.Vertical(Colors.red_to_yellow, "3. Quit"))
        
        choice = input("\n[] Choose an option (1, 2, 3): ")
        
        if choice == "1":
            test_single_link()  # Test a single link
        elif choice == "2":
            file_path = input("\n[] Enter the file path containing the links: ")
            output_file = "link_status.csv"  # Output CSV file name
            check_links_from_file(file_path, output_file)  # Test all links in the file
        elif choice == "3":
            print(Colorate.Vertical(Colors.red_to_yellow, "\n[] Goodbye!"))
            break  # Exit the program
        else:
            print(Colorate.Vertical(Colors.red_to_yellow, "\n[] Invalid choice! Please choose 1, 2, or 3."))

if __name__ == "__main__":
    menu()  # Launch the interactive menu
