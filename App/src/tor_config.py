# Routing of my local browser to accept Tor proxie and enable it run via 
# the following ports on localhost
# This function is accessed and called by main.py file 

def torCon(TOR_PROXY={"http":"socks5h://localhost:9050", "https":"127.0.0.1:9050"}):
    return TOR_PROXY

    #TOR_PROXY = {"http":"socks5h://localhost:9050", "https":"127.0.0.1:9050"}
    #print(TOR_PROXY)
#torCon()

'''
- This function check if you have a vpn connection in your computer in other to 
  access the tor network. 
- If activated, the main.py program will not work unless there is a VPN in the local
  computer.

def check_for_vpn():
    url = "http://ip-api.com/json/"
    key = requests.get(url)
    print(key.text)
    
    if "Nigeria" in key.text or "Lagos" in key.text or "Abuja" in key.text:
        print("Your VPN might not be on !!")
        safe = False
    else:
        safe = True

    if safe == True:
        browse()
    else:
        print("IP change failed, try again later.")
  

check_for_vpn()

'''