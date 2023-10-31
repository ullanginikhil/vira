import subprocess
import requests
import signal
import sys
import os
from colorama import init, Fore, Style

# Initialize colorama
init()

# Function to perform an Nmap scan and save results in a text file
def perform_nmap_scan(url, scan_options, result_file_name):
    nmap_command = f"nmap {scan_options} -oN {result_file_name}.txt {url}"
    try:
        subprocess.run(nmap_command, shell=True, check=True)
        print(f"{Fore.GREEN}Scan completed successfully. Nmap results saved in {result_file_name}.txt{Style.RESET_ALL}")
    except subprocess.CalledProcessError:
        print(f"{Fore.RED}Error occurred during the Nmap scan.{Style.RESET_ALL}")

# Function to prompt the user for subdomain enumeration tools selection
def select_subdomain_enum_tools():
    subdomain_tools = []
    print(f"{Fore.CYAN}Select subdomain enumeration tools:")
    print(f"{Fore.YELLOW}1) crt.sh")
    print("2) Gobuster")
    print("3) Findomain")
    print("4) Amass")
    print("5) Waybackurls")
    print("6) Assetfinder{Style.RESET_ALL}")

    selection = input("Enter the numbers of the tools you want to use (e.g., '1 3 5' for crt.sh, Findomain, and Waybackurls): ")
    selected_tools = [int(tool) for tool in selection.split()]

    if 1 in selected_tools:
        subdomain_tools.append("crt.sh")
    if 2 in selected_tools:
        subdomain_tools.append("Gobuster")
    if 3 in selected_tools:
        subdomain_tools.append("Findomain")
    if 4 in selected_tools:
        subdomain_tools.append("Amass")
    if 5 in selected_tools:
        subdomain_tools.append("Waybackurls")
    if 6 in selected_tools:
        subdomain_tools.append("Assetfinder")

    return subdomain_tools

# Function to perform subdomain enumeration using crt.sh and save results to a file
def perform_subdomain_enum_crt(url, result_file_name):
    subdomains = set()
    try:
        response = requests.get(f"https://crt.sh/?q=%.{url}&output=json")
        if response.status_code == 200:
            json_data = response.json()
            for entry in json_data:
                subdomain = entry["name_value"].lower()
                if not subdomain.startswith("www.") and not subdomain.startswith("*.") and subdomain.endswith(f".{url}"):
                    subdomains.add(subdomain)
        subdomains_file = f"{result_file_name}_crt.txt"
        with open(subdomains_file, "w") as file:
            file.write("\n".join(subdomains))
        print(f"{Fore.GREEN}Pure subdomains found for {url} saved in {subdomains_file}{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}Error during subdomain enumeration: {str(e)}{Style.RESET_ALL}")

# Function to perform subdomain enumeration using Gobuster and filter the output at runtime
def perform_subdomain_enum_gobuster(target_name, result_file_name):
    try:
        gobuster_command = f"gobuster dns -d {target_name} -w /usr/share/wordlists/seclists/Discovery/DNS/deepmagic.com-prefixes-top500.txt -o {result_file_name}_gobuster_tmp.txt"
        subprocess.run(gobuster_command, shell=True, check=True)
        with open(f"{result_file_name}_gobuster_tmp.txt", "r") as infile, open(f"{result_file_name}_gobuster.txt", "w") as outfile:
            for line in infile:
                if "Found:" in line:
                    line = line.replace("Found:", "").strip()
                outfile.write(line)
        print(f"{Fore.GREEN}Gobuster subdomain enumeration completed and results saved in {result_file_name}_gobuster.txt{Style.RESET_ALL}")
        subprocess.run(f"rm {result_file_name}_gobuster_tmp.txt", shell=True)
    except subprocess.CalledProcessError:
        print(f"{Fore.RED}Error occurred during Gobuster subdomain enumeration{Style.RESET_ALL}")

# Function to perform subdomain enumeration using Findomain
def perform_subdomain_enum_findomain(target_name, result_file_name):
    try:
        result_file_name = result_file_name.rsplit(".", 1)[0]
        findomain_command = f"findomain -t {target_name} -u {result_file_name}_findomain.txt"
        subprocess.run(findomain_command, shell=True, check=True)
        print(f"{Fore.GREEN}Findomain subdomain enumeration completed and results saved in {result_file_name}_findomain.txt{Style.RESET_ALL}")
    except subprocess.CalledProcessError:
        print(f"{Fore.RED}Error occurred during Findomain subdomain enumeration{Style.RESET_ALL}")

# Function to perform subdomain enumeration using Amass
def perform_subdomain_enum_amass(target_name, result_file_name):
    try:
        amass_command = f"amass enum -d {target_name} -o {result_file_name}_amass.txt"
        subprocess.run(amass_command, shell=True, check=True)
        print(f"{Fore.GREEN}Amass subdomain enumeration completed and results saved in {result_file_name}_amass.txt{Style.RESET_ALL}")
    except subprocess.CalledProcessError:
        print(f"{Fore.RED}Error occurred during Amass subdomain enumeration{Style.RESET_ALL}")

# Function to perform subdomain enumeration using waybackurls
def perform_subdomain_enum_waybackurls(target_name, result_file_name):
    try:
        waybackurls_command = f"waybackurls {target_name} > {result_file_name}_wayback.txt"
        subprocess.run(waybackurls_command, shell=True, check=True)
        print(f"{Fore.GREEN}Waybackurls subdomain enumeration completed and results saved in {result_file_name}_wayback.txt{Style.RESET_ALL}")
    except subprocess.CalledProcessError:
        print(f"{Fore.RED}Error occurred during Waybackurls subdomain enumeration{Style.RESET_ALL}")

# Function to process the waybackurls output file
def process_waybackurls_output(result_file_name):
    wayback_file = f"{result_file_name}_wayback.txt"
    temp_file = f"{result_file_name}_wayback_tmp.txt"
    with open(wayback_file, "r") as infile, open(temp_file, "w") as outfile:
        for line in infile:
            line = line.replace("http://", "").replace("https://", "").replace("www.", "")
            outfile.write(line)
    os.remove(wayback_file)
    os.rename(temp_file, wayback_file)

# Function to perform subdomain enumeration using assetfinder
def perform_subdomain_enum_assetfinder(target_name, result_file_name):
    try:
        assetfinder_output_file = f"{result_file_name}_assetfinder.txt"
        assetfinder_command = f"assetfinder --subs-only {target_name} > {assetfinder_output_file}"
        subprocess.run(assetfinder_command, shell=True, check=True)
        print(f"{Fore.GREEN}Assetfinder subdomain enumeration completed and results saved in {assetfinder_output_file}{Style.RESET_ALL}")
    except subprocess.CalledProcessError:
        print(f"{Fore.RED}Error occurred during Assetfinder subdomain enumeration{Style.RESET_ALL}")

# Function to combine subdomain output files into a single file
def combine_subdomain_output(result_file_name, selected_files):
    combined_file_name = f"combined_{result_file_name}_subdomain_list.txt"
    with open(combined_file_name, "w") as outfile:
        for file_name in selected_files:
            with open(file_name, "r") as infile:
                outfile.write(infile.read())
            print(f"{Fore.GREEN}Appended {file_name} to {combined_file_name}{Style.RESET_ALL}")

# Function to probe subdomains using httprobe
def probe_subdomains(result_file_name):
    combined_file_name = f"combined_{result_file_name}_subdomain_list.txt"
    httprobe_output_file = f"{result_file_name}_httprobes.txt"

    httprobe_command = f"cat {combined_file_name} | httprobe -p http:80 -p https:443 -t 20000 > {httprobe_output_file}"
    try:
        subprocess.run(httprobe_command, shell=True, check=True)
        print(f"{Fore.GREEN}HTTP probing completed. Results saved in {httprobe_output_file}{Style.RESET_ALL}")
    except subprocess.CalledProcessError:
        print(f"{Fore.RED}Error occurred during HTTP probing{Style.RESET_ALL}")

# Function to get user input for scan options and result file name
def get_user_input():
    url = input("Enter the target URL or IP address: ")
    scan_option_choice = input(
        f"{Fore.CYAN}Choose a scan technique:\n"
        f"{Fore.YELLOW}1) Ping Scan (-sn)\n"
        "2) Default Script Scan (-sC)\n"
        "3) Service Version Detection (-sV)\n"
        "4) OS Detection (-O)\n"
        "5) No Ping Scan (-Pn)\n"
        "6) Scan All Ports (-p-)\n"
        "7) All of the above (-sn -sC -sV -O -Pn -p-)\n"
        "8) Custom Flags (Manually enter flags separated by spaces)\n"
        "Enter the scan option (1-8): "
    )
    if scan_option_choice == '1':
        scan_options = '-sn'
    elif scan_option_choice == '2':
        scan_options = '-sC'
    elif scan_option_choice == '3':
        scan_options = '-sV'
    elif scan_option_choice == '4':
        scan_options = '-O'
    elif scan_option_choice == '5':
        scan_options = '-Pn'
    elif scan_option_choice == '6':
        scan_options = '-p-'
    elif scan_option_choice == '7':
        scan_options = '-sn -sC -sV -O -Pn -p-'
    elif scan_option_choice == '8':
        custom_flags = input("Enter custom Nmap flags separated by spaces: ")
        scan_options = custom_flags
    else:
        print(f"{Fore.RED}Invalid option. Using the default option (-sn){Style.RESET_ALL}")
        scan_options = '-sn'
    result_file_name = input("Enter the name for the result file (without extension): ")
    return url, scan_options, result_file_name

# Function to gracefully handle script interruption (Ctrl+C)
def signal_handler(signal, frame):
    print(f"{Fore.YELLOW}Thank you, see you soon!{Style.RESET_ALL}")
    sys.exit(0)

# Register the signal handler for Ctrl+C
signal.signal(signal.SIGINT, signal_handler)

# Main function
if __name__ == "__main__":
    url, scan_options, result_file_name = get_user_input()
    perform_nmap_scan(url, scan_options, result_file_name)
    subdomain_tools = select_subdomain_enum_tools()
    selected_files_to_combine = []

    if "crt.sh" in subdomain_tools:
        perform_subdomain_enum_crt(url, result_file_name)
        selected_files_to_combine.append(f"{result_file_name}_crt.txt")

    if "Gobuster" in subdomain_tools:
        perform_subdomain_enum_gobuster(url, result_file_name)
        selected_files_to_combine.append(f"{result_file_name}_gobuster.txt")

    if "Findomain" in subdomain_tools:
        perform_subdomain_enum_findomain(url, result_file_name)
        selected_files_to_combine.append(f"{result_file_name}_findomain.txt")

    if "Amass" in subdomain_tools:
        perform_subdomain_enum_amass(url, result_file_name)
        selected_files_to_combine.append(f"{result_file_name}_amass.txt")

    if "Waybackurls" in subdomain_tools:
        perform_subdomain_enum_waybackurls(url, result_file_name)
        process_waybackurls_output(result_file_name)
        selected_files_to_combine.append(f"{result_file_name}_wayback.txt")

    if "Assetfinder" in subdomain_tools:
        perform_subdomain_enum_assetfinder(url, result_file_name)
        selected_files_to_combine.append(f"{result_file_name}_assetfinder.txt")

    if selected_files_to_combine:
        print(f"{Fore.CYAN}Subdomain enumeration completed. You can now select files to combine.")
        print(f"{Fore.YELLOW}Select the files you want to combine by entering their respective numbers:{Style.RESET_ALL}")
        for i, file_name in enumerate(selected_files_to_combine, start=1):
            print(f"{Fore.CYAN}{i}) {file_name}{Style.RESET_ALL}")

        user_selection = input("Enter the numbers of the tools you want to combine (e.g., '1 2 3' for crt.sh, Gobuster, and Findomain): ")
        selected_indices = [int(index) for index in user_selection.split() if 1 <= int(index) <= len(selected_files_to_combine)]

        # Combine selected subdomain output files
        selected_files_to_combine = [selected_files_to_combine[i - 1] for i in selected_indices]
        combine_subdomain_output(result_file_name, selected_files_to_combine)

        print(f"{Fore.GREEN}Selected subdomain enumeration output files combined into combined_{result_file_name}_subdomain_list.txt{Style.RESET_ALL}")

        # Probe the subdomains and save the results
        probe_subdomains(result_file_name)
    else:
        print(f"{Fore.YELLOW}No subdomain enumeration output files were selected for combining.{Style.RESET_ALL}")
