Distributed-Files-System :
This system is constructed using REST services, written in python using web.py.

Usage :
The current configuration has one client with on server file named Hello.txt.

Distributed Transparent File Access :
The system is modelled based on upload/download.Downloads only occur if files are modified, and writes are pushed upstream. Users interact with the system through the client service. Authenticated users can write to files, and these writes go to a primary copy, which in turn distributes copies of the files to replica nodes.

Client Service :
Act as a proxy between the user interface and file system. The client will allow users to read file content and write to it. The write encapsulates both opening the file and writing to it. As a result at no point, the client will keep the file open. Files are locked before writes are propagated.

Lock service :
Authenticates user. Locks file if available. If it is already locked, the user is added to the queue.
When a user unlocks, the server assigns the lock to the user in the queue if there is one, and notifies it.
However, the whole system is susceptible deadlocks, as files could be left locked and other clients waiting for the lock.

Directory service :
The directory service is the most important components. It has a full view of the status of files, this includes: where files are stored, information about primary and secondary file servers. Unfortunately, this means that directory service is a single point of failure and would have to handle much traffic.

File accesses :
When a client does a file search, the directory service returns metadata of the file. It also includes the address of a replica fileserver. This is because reads go to a replica fileserver.

Writes, on the other hand, go to the primary file server, which in turn pushes the changes to the replica. It retrieves the information about the replicas from the directory service

Caching :
When a client introduces an new file to the system, the directory server creates metadata for the file. It includes timestamp of when it was updated. During reads, the client checks with the directory service if the local copy is dated, if so it will retrieve the latest from the fileserver.

File server service :
The directory will point the client to the primary server for writes and reads to the secondary ones.

Commands -
1.)	sign up --> Signs up a user

2.)	login --> Already registered users can log in using there username and password for communicating with other services


Registration
0.0. As the system starts up the fileserver register themselves to the directory service. Heart beats are sent periodically

Login in
1.0 Client signs up first

1.1 Client encrypts its message using the authentication servers public key and sends credential.

1.2 Authentication server returns a token

Write and read
2.1 The client locks the file before writing to it. If locked it stays in queue and waits for the lock

2.1.1 Client will have the file metadata from the directory service

2.2 After acquiring the lock. It writes the file and update the information in directory server

2.3 It unlocks the file when writing is done by the client.

