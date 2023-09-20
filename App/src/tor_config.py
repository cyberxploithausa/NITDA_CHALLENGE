# Routing of my local browser to accept Tor proxie and enable it run via 
# the following ports on localhost
# This function is accessed and called by main.py file 

def torCon(TOR_PROXY={"http":"socks5h://localhost:9050", "https":"127.0.0.1:9050"}):
    return TOR_PROXY

    #TOR_PROXY = {"http":"socks5h://localhost:9050", "https":"127.0.0.1:9050"}
    #print(TOR_PROXY)
#torCon()