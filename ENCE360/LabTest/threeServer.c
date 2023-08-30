#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <netdb.h> 
#include <errno.h>
#include <unistd.h>

#define MAXDATASIZE 1024  


int main(int argc, char *argv[])  {

    if (argc != 2) {  // need two arguments for server
            fprintf(stderr,"usage: threeServer port-number\n"); 
            exit(1); 
    } 

	printf("\nThis is the server with pid %d listening on port %s\n", getpid(), argv[1]); // printing server

	int s = socket(AF_INET, SOCK_STREAM, 0); // create a new socket

	struct sockaddr_in sa, caller; // creating object for the sockets address, and the caller
	sa.sin_family = AF_INET;   // your domain, tcp
	sa.sin_addr.s_addr = INADDR_ANY; // address
	sa.sin_port = htons(atoi(argv[1])); // the port chosen from command line

	int rc = bind(s, (struct sockaddr *)&sa, sizeof(sa)); // attaching local address to socket

	rc = listen(s, 5); // the number of connections this socket can have, says to kernel "I am now passively accepting connections!"


	socklen_t length = sizeof(caller); // caller is client that wants to connect

	int msgsock = accept(s, (struct sockaddr *)&caller, &length); // accepting connection call, assigning it to a msgsock file descriptor so kernel can traffic data correctly

	char message[MAXDATASIZE] = "congrats you successfully connected to the server!"; // message to print in this case, usually the buffer
	char buffer[MAXDATASIZE]; // making a buffer for temp data
	while (strlen(message) > 0) // usually use buffer, but here printing message
	{
		buffer[num_read] = '\0'; // so it knows end of file
		int numbytes; // number of bytes of data read from socket

		// send data to the client and then get data back from the client:
		write(msgsock, buffer, message); // sending data over the connection
		read(msgsock, buffer, MAXDATASIZE - 1);

		message[numbytes - 1] = '\0'; // so it knows end of file
	}

	close(msgsock); // close the socket so that the kernel doesnt try to send information to it

    exit (0);
}

/**
It would print like that because this reads one character at a time, and it's while strlen(message) > 0
so every loop it will remove one from the end and continue until it has removed all of them. You usually wouldnt
do it lke this, youd just printf it, or you would print written data to the server by using a buffer of chars
not just a string
*/