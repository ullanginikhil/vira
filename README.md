# vira
The VIRA tool is a total subdoamin enumuration tool created by `NIKHIL ULLANGI` AKA `Ncrypto` which uses Nmap and Subdomain Enumeration Script in a powerful and flexible command-line fomat. Desiged for security professionals, researchers, and system administrators. It simplifies the process of gathering comprehensive information about a target website or IP address through a combination of Nmap scanning and subdomain enumuration techniques.

# Key Features
* Nmap Scanning: The script allows users to perform Nmap scans with various scanning options. Nmap is a versatile open-source network scanning tool that can provide essential information about open ports, services, operating systems, and more.

* Allows us to customise the scanning process and combine the output files of disired tools and also check weather the subdoamin are running or not using httprobe.

* Subdomain Enumeration: The tool offers multiple subdomain enumeration options, leveraging popular subdomain discovery tools such as crt.sh, Gobuster, Findomain, Amass, Waybackurls, and Assetfinder. This aids in identifying subdomains associated with the target domain, which can be crucial for security assessments and reconnaissance.

* Subdomain Output Combination: After running subdomain enumeration tools, the script provides the capability to combine their results into a single file for easier analysis. This feature simplifies the management of subdomain data.

* Subdomain Probing: The script probes the enumerated subdomains to check which of them are live or responsive. Identifying live subdomains can be critical when assessing potential attack surfaces.

* User-Friendly Interface: The script features a user-friendly command-line interface that guides users through the process of selecting Nmap scan options, subdomain enumeration tools, and more. It streamlines the reconnaissance process and reduces the complexity of running multiple commands manually.

# Prerequisites
Make sure to install golang and all the go tools used in the vira tool and properly configure the path to theri bin files.
Before using the script, users need to have the following dependencies and tools installed on their system:

* Nmap
* Gobuster
* crt.sh
* Findomain
* Amass
* Waybackurls
* Assetfinder
* Python 3
* httprobe
* Python packages: Colorama and Requests</br>
This script simplifies the reconnaissance process by offering a unified interface for Nmap scanning and subdomain enumeration. It streamlines the collection of critical information for security assessments, ensuring a smoother and more efficient workflow.

# How to Use
Clone the repository or download the script.

git clone https://github.com/ullanginikhil/vira


Run the script from the command line using Python:

