import os


# Starting Tor service
os.system('\Desktop\TorBrowser\Browser\Tor\tor.exe' if os.name=='nt' else 'service tor start')
