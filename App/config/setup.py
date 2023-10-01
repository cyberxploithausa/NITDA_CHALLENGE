import os

def start_tor():
    # Starting Tor service
    #os.system("C:/Users/cyberxploit/Desktop/Tor Browser/Browser/TorBrowser/Tor/tor.exe" if os.name=='nt' else 'service tor start')
    os.system("tor.exe" if os.name=='nt' else "service tor start")
start_tor()