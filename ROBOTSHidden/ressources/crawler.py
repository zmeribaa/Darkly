import requests
import re
import time
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import sys

# Configuration
base_url = "http://10.14.58.57/.hidden/"
total_files = 18279
current_file = 0
found_flag = ""

# Network settings
MAX_RETRIES = 5
RETRY_DELAY = 0  # seconds between retries
REQUEST_DELAY = 0.1  # seconds between requests

# Regex to find the flag
flag_regex = re.compile(r'.*[0-9]{5,}.*')  # Look for strings with at least 5 digits

def make_request_with_retry(url, max_retries=MAX_RETRIES):
    """Make HTTP request with retry logic"""
    for attempt in range(max_retries):
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            if attempt == max_retries - 1:
                raise e
            print(f"  Retry {attempt + 1}/{max_retries} for {url}")
            time.sleep(RETRY_DELAY * (attempt + 1))  # Exponential backoff
    return None

def search_flag(url, check_for_flag=False):
    global found_flag, current_file

    if found_flag:
        return

    try:
        if check_for_flag:
            response = make_request_with_retry(url)
            if not response:
                return
                
            current_file += 1
            progress = (current_file * 100) // total_files
            print(f"Current progress: {progress}% (File {current_file}/{total_files})", end='\r')
            
            # Check if this might be the flag
            content = response.text.strip()
            if flag_regex.match(content):
                found_flag = content
                print(f"\n[+] Flag found in: {url}")
                print(f"[+] Content: {content}")
                return
            return

        # Parse directory listing
        response = make_request_with_retry(url)
        if not response:
            return
            
        soup = BeautifulSoup(response.text, 'html.parser')
        links = []
        
        # Find all links in the directory listing
        for link in soup.find_all('a'):
            href = link.get('href')
            if href and href != '../':  # Skip parent directory
                links.append(href)
        
        for link in links:
            if found_flag:
                return
                
            new_url = urljoin(url, link)
            
            if link.endswith('/'):
                # It's a directory, explore it
                search_flag(new_url)
                time.sleep(REQUEST_DELAY)  # Small delay between requests
            elif link == 'README':
                # It's a README file, check it for flag
                search_flag(new_url, True)
                time.sleep(REQUEST_DELAY)  # Small delay between requests
                
    except Exception as e:
        print(f"\n[!] Unexpected error at {url}: {e}")
        # Continue with other links instead of stopping completely

# Install BeautifulSoup if not already installed
try:
    from bs4 import BeautifulSoup
except ImportError:
    print("Installing BeautifulSoup...")
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "beautifulsoup4"])
    from bs4 import BeautifulSoup

print("[*] Starting recursive search for the flag...")
print(f"[*] Total README files to check: {total_files}")
search_flag(base_url)

if found_flag:
    print(f"\n[SUCCESS] THE FLAG IS: {found_flag}")
else:
    print(f"\n[FAILURE] Flag not found after checking {current_file} files.")
    if current_file < total_files:
        print("[!] Some files could not be accessed due to connection errors.")