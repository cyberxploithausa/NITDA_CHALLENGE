﻿# NITDA_CHALLENGE
## Challenge
```bash
Build advanced web crawling tools that navigate the dark web, collect relevant data, and provide organizations with insights into emerging threats and vulnerabilities. This tool should feature an analytics to process and categorize unstructured dark web data, providing actionable insights to security teams
```
## Challenge Outline
- ` Legal and Ethical Considerations`
    - Understand the legal and ethical implications of crawling the dark web. 
    - Ensure that i comply with all relevant laws and regulations, such as cybersecurity and privacy laws.
    - Consider ethical guidelines and principles to protect privacy and handle sensitive information appropriately.
- ` Project Scope and Objectives`
    - Determine what types of data i intend to collect and the specific insights i want to provide.
- ` Permissions and Access`
    - We need to make a proxies connection to Tor Network that will route the program to be able to access the DarkWeb. This can be achieve with Tor Browser, stem library (python).
    - Some areas of the dark web may require specific access methods or authorization.
- ` Technologies Used`
    - Python version 3
    - Tor Browser Tor Network
    - Microsoft Excel
- ` Data Collection`
    - Create web crawlers or spiders that can navigate the dark web, collect data from various sources (websites, forums, etc.), and store it securely.
- ` Data Processing and Analytics`
    - Implement data processing and analysis tools to make sense of the collected data. This may involve natural language processing (NLP) techniques, data categorization, and machine learning for identifying patterns or moreover using Microsoft Excel.
- ` Insights and Reporting`
    - Develop a system to generate actionable insights and reports based on the analyzed dark web data. 
    - Security teams should be able to understand emerging threats and vulnerabilities from the insights provided.
- ` Security Measures`
    - Prioritize security throughout the project. Protect the data i collect, use encryption where necessary, and establish secure communication channels.
- ` Testing and Validation`
    - Rigorously test the crawling, data processing, and analytics components to ensure accuracy and reliability. 
    - Use a variety of dark web sources to validate your results.
- ` Feedback and Improvement`
    - Encourage feedback from users and stakeholders to enhance the tool's capabilities and accuracy over time.

## USAGE
```bash
git clone https://github.com/cyberxploithausa/NITDA_CHALLENGE.git
cd NITDA_CHALLENGE
pip install -r requirements.txt
cd App/config
python setup.py
cd ../src
python main.py
```

## TO-Dos
> Things to note
    - Connect to Tor network and browse the dark web | status = Done
    - Search for keywords base of a search engine
    - Crawl through the results and keep track of every link
    - Store the links of the crawled result in text file for now
    - Detect Threats and vulnerabilities of technologies
    - Raise Alarm of the above
