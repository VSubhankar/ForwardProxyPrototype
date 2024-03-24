# Forward Proxy Prototype

## End Functionality of this application:- 
  A Python program serves as a forward proxy server acting as an intermediate between Firefox-Browser (Client) and Requested websites(Server) and the requests are displayed in the terminal for monitoring purposes.

## Instructions

 - Clone this repo by - git clone https://github.com/VSubhankar/ForwardProxyPrototype.git
 - Install Python3.12 (if not present ) at https://www.python.org/downloads/
 - Install Mozilla Firefox (if not present) at https://www.mozilla.org/en-US/firefox/download/thanks/

 - Go to Firefox URL bar and type about:preferences to open settings scroll down to end and click on Network Settings , Then select manual proxy and type 127.0.0.1 as proxy and 8090 as port.
 - Use pip install cardet (This module is used for finding the encoding of Server Website)
 - Open Command Prompt and type the following Code (inside the directory of cloned repo)
```
python3 httpProxy.py
```
 - Go to Firefox URL bar and type http://vulnweb.com and you can observe the proxy working sucessfully

 - Observe the output on terminal to know about the transmission between server and client
