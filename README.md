# Trado

## Features
* Serves as a simple file transfer service between client and server. Initially designed for easy transfer of files to single-board computers, such as the Raspberry Pi.
* Can be used both locally on the network or over the internet.

 
## Installation
```bash
Soon updated
```
 
## Usage
#### Server-side
Start server where you want to receive files. If no path is specified the home folder is used. Two modes of the server can be used:

* internal,
* external.

By using the internal mode, only connection over the local network is possible, i.e. your home wifi. by using external mode, connection to the server can be made if the used port has been forward in the router.


```python
import trado

server = trado.trado()
# Connecting externally, i.e. connection 
# over the internet is possible.
server.connect_server(mode = 'external', host = '92.34.13.274', port = 1750)
server.add_path('/users/antonnormelius/documents')
server.receive()
```
 
#### Client-side
Client is used to transfer files- and folders to server. Observe that
the host and port for the client need to be the same as the host and port
specified when starting the server. 
```python
import trado

client = trado.trado()
client.connect_client(host = '92.34.13.274', port = 1750)
client.transmit(file)
```

## License
[MIT](https://choosealicense.com/licenses/mit/)
