
# Distributed File Server :
Distributed File System is implemented in Python using RESTful Webservices. Web.py is used to
implement RESTful webservices in python. NFS File System style is used.

Six main components are implemented in DFS. The following are them:
1. Distributed Transparent File Access
2. Directory Service
3. Security Service
4. Lock Service
5. Client Proxy
6. Caching - In progress

# 1. Distributed Transparent File Access --
The following are the tasks that is taken care by distributed file server:
1. Makes a call to the Authentication server for authentication.
2. Carry out the read and write operations.
3.) Instead of provding a download option, file are directly written on the server to avoid version issues.

# 2. Lock service --
Maintains a persistent dictionary that stores filenames and the corresponding lock state : lock - 1 and unlock - 0.
First Checks whether the requested file is locked or not. Does the locking of file (whenever a write method) when triggered.
Unlock the file when triggered (after write operation is completed)

# 3. Directory service --
The directory service is the most important components. It has a full view of the status of files, this includes: where files are stored, information about primary and secondary fileservers. A persistent dictionary is maintained at the Directory Server side in which filename, absolute file path and the port number in which the file server (in which that particular filename
resides) runs.
Unfortunately, this means that directory service is a single point of failure and would have to handle lot of traffic.

# 4.) Security (authentication Server) -
As a first step, client is asked to login to the system. The username and password is authenticated by
the Authentication Server. Authentication server maintains a persistent dictionary at its side in
which the usernames and corresponding passwords are saved. After the authentication of the client,
server sends back the token that is encrypted using the client’s password.

# 5. Client Proxy - 
A client program has been created that includes a client proxy that calls each of servers via rest calls.
The client takes the input from the user and passes the received data to the client proxy. The user is
not aware about the client proxy that runs in the background.
Client proxy is responsible for making the rest call to each of the servers which are up in the order.
The following are the steps that are taken care by the client proxy:
1. Client proxy receives the username and password and make a rest call to the Authentication
Server for the authentication. 
2. It then makes a call to the Directory Server by passing the filename and receives the absolute file
path along with the fileserver address.
3. Makes appropriate calls to the lock server for locking and unlocking the files.
4. Makes calls to the file server for read and write operations.

The following is the flow of the read and write operations:
If the operation requested by user is read:

Case 1 – File is not locked
If the file is not locked, make another call to the lock server to lock the file by passing the encrypted
filename and receive the response from lock server -> encrypts the file path and content to be
written and makes a call to the file server by passing this encrypted message to write the content in 
the file -> Receives the encrypted success message from file server -> decrypts the success message
and displays it -> Unlock the file by calling lock service.

Case 2 – file is locked
If the file is locked, display that the write operation is not possible and exits.

# 6. Caching --
When a client introduces an new file to the system, the directory server creates metadata for the file. It includes timestamp of when it was updated. During reads, the client checks with the directory service if the local copy is dated, if so it will retrieve the latest from the fileserver.

# Commands -
1.) sign up --> Signs up a user

2.) login --> Already registered users can login using there username and password for communicating with other services


# Registration :-
0.0. As the system starts up the fileserver register themselves to the directory service. Heart beats are sent periodically

 Login in :
1.0 Client signs up first

1.1 Client encrpts its message using the authentication servers public key and sends credential.

1.2 Authentication server returns a token

Write and read :
2.1 The client locks the file before writing to it. If locked it stays in queue and waits for the lock

2.1.1 Client will have the file metadata from the directory service

2.2 After acquiring the lock. It writes the file and update the information in directory server

2.3 It unlocks the file when writting is done by the client.
