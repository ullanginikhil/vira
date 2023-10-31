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
* Python packages: Colorama and Requests<br>
This script simplifies the reconnaissance process by offering a unified interface for Nmap scanning and subdomain enumeration. It streamlines the collection of critical information for security assessments, ensuring a smoother and more efficient workflow.

# How to Use
Clone the repository or download the script.

`git clone https://github.com/ullanginikhil/vira.git`

Run the script from the command line using Python:

`python nmap_subdomain_enum.py`<br>
**Simply choose the options for namp as mentioned below to use the tool:**

![1](https://github.com/ullanginikhil/vira/assets/72622870/1eca1807-17b6-4f08-9493-3b25f246774e)

**Then select the tools for subdomain enumuraiton. You can select all, with spaces in between of two numbers (ex: 1 2 3):**

![2](https://github.com/ullanginikhil/vira/assets/72622870/a5777602-a749-498b-b8c0-8ba3503e5975)

**Then select the file names ypu want to combine for end result combined file:**
 
![3](https://github.com/ullanginikhil/vira/assets/72622870/d074be69-f469-41b3-bf1a-9e0645b7995b)


**You can change the Wordlist by simpling changing this line in the script:** 

![4](https://github.com/ullanginikhil/vira/assets/72622870/91aa9600-51e5-4ea2-aea4-b07f23c19908)


**The output files are saved in a very systematic format as <filename_toolname>:**

![5](https://github.com/ullanginikhil/vira/assets/72622870/08319692-d0f0-4c5e-8fd9-faa96851cefb)


# Author
* Nikhil Ullangi AKA Ncrypto.

# Acknowledgments
* The script utilizes several excellent open-source tools for subdomain enumeration, including those developed by <a href=https://github.com/tomnomnom>Tomnomnom</a>
* Acknowledgments to the open-source community and contributors to the tools and libraries used in this script.
* Special thanks to the developers of Nmap for creating a powerful network scanning tool.

