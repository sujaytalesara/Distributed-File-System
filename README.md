Distributed-filesystem
This system is constructed using REST services, written in python using web.py.

Usage
Current configuration has one clients with on server file named Hello.txt.

Distributed Transparent File Access
The system is modeled based on upload/download.Downloads only occur if files are modified and writes are pushed upstream. Users interact with system through the client service. Authenticated users can write to files, and these writes go to a primary copy, which in turn distributes copies of the files to replica nodes.

Client Service
Act as a proxy between user interface and file system. Client will allow users to read file content and write to it. The write encapsulates both opening the file and writing to it. As a result at no point the client will keep the file open. Files are locked before writes are propagated

Lock service
Authenticates user
Locks file if available. If it is already locked, the user is added to the queue.
When a user unlocks, the server assigns the lock to the user in the queue if there is one, and notifies it.
However, the whole system is susceptible deadlocks, as files could be left locked and other clients waiting for the lock.

Directory service
The directory service is the most important components. It has a full view of the status of files, this includes: where files are stored, information about primary and secondary fileservers. Unfortunately, this means that directory service is a single point of failure and would have to handle lot of traffic.

File accesses
When a client does a filesearch, the directory service returns metadata of the file. It also includes address of a replica fileserver. This is because reads go to a replica fileserver.

Writes on the otherhand go to the primary fileserver, which in turn pushes the changes to the replica. It retrieves the information about the replicas from the directory service

Handling transactions
Similar to the fileserver the directory server also has its own shadow copy, which is merged at a successful commit.

Replication service
As described above reads go to the secondary copies and writes to the primary copy.

Caching
When a client introduces an new file to the system, the directory server creates metadata for the file. It includes timestamp of when it was updated. During reads, the client checks with the directory service if the local copy is dated, if so it will retrieve the latest from the fileserver.

Fileserver service
The directory will point client to primary server for writes and reads to the secondary ones.

Stores the files
Starts by registering itself then it regularly sends heartbeats to the directory service.
Each fileserver represent a directory. The directory name is passed in an environment variable
Asynchronously sends the copy (if primary copy)
Transaction Service
To initiate a transaction the client makes a call to the Transaction Server(TS), which returns a transaction id.
Client uses this id and sends file changes. TS locks the files and stores the changes.
If the file is locked, transaction waits till it is unlocked.
Once the client executes commit, the file changes are transfered to the fileserver's shadow copy.
Upon receiving the shadow copy, fileservers will send a ready to commit signal
If all the servers send ready to commit. Transaction server instructs servers to update their true copy.
There are many possible point of failures, example being where the servers not responding with ready to commit signal. With current implementation the transaction stalls. A better solution would take into account a timeout before canceling the transaction

Commands
sign up --> Signs up a user

login --> Already registered users can login using there username and password for communicating with other services


Registration
0.0. As the system starts up the fileserver register themselves to the directory service. Heart beats are sent periodically

Login in
1.0 Client signs up first

1.1 Client encrpts its message using the authentication servers public key and sends credential.

1.2 Authentication server returns a token

Write and read
2.1 The client locks the file before writing to it. If locked it stays in queue and waits for the lock

2.1.1 Client will have the file metadata from the directory service

2.2 After acquiring the lock. It writes the file and update the information in directory server

2.3 It unlocks the file when writting is done by the client.

