#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <netdb.h> 
#include <errno.h>
#include <unistd.h>

#define MAXDATASIZE 1024 // max buffer size 
#define SERVER_PORT 2000

int listen_on(int port)
{

    int s = socket(AF_INET, SOCK_STREAM, 0);

    struct sockaddr_in sa;
    sa.sin_family = AF_INET;          /* communicate using internet address */
    sa.sin_addr.s_addr = INADDR_ANY; /* accept all calls                   */
    sa.sin_port = htons(port); /* this is port number                */

    int rc = bind(s, (struct sockaddr *)&sa, sizeof(sa)); /* bind address to socket   */
    if (rc == -1) { // Check for errors
        perror("bind");
        exit(1);
    }

    rc = listen(s, 5); /* listen for connections on a socket */
    if (rc == -1) { // Check for errors
        perror("listen");
        exit(1);
    }

    return s;
}


int accept_connection(int s) {
    struct sockaddr_storage caller;
    socklen_t length = sizeof(caller);
    int msgsock = accept(s, (struct sockaddr *)&caller, &length);
    if (msgsock == -1) {
        perror("accept");
        exit(1);
    }

    return msgsock;
}


void handle_request(int msgsock) {

    char buffer[MAXDATASIZE];
    int num_read = 0;

    num_read = read(msgsock, buffer, MAXDATASIZE - 1);
    printf("read a message %d bytes: %s\n", num_read, buffer);


    // TODO: write a function to reply to all incoming messages
    // while the connection remains open
    while (num_read > 0) {
        buffer[num_read] = '\0';
        printf("Received message!");
        write(msgsock, buffer, num_read);
        num_read = read(msgsock, buffer, MAXDATASIZE - 1);
    }
    close(msgsock);

}


// handle request by forking a new process
void handle_fork(int msgsock) {

    //TODO: run this line inside a forked child process
    if (fork() == 0){
        handle_request(msgsock);       
        exit(0);
    } else {
        wait();
        close(msgsock);
    }

    // Be very careful to close all sockets used, 
    // and exit any processes or threads which aren't used
      // Note that sockets open BEFORE a fork() are open in BOTH parent/child

    ///////////////////////////////////////////
}





int main(int argc, char *argv[]) {


    printf("\nThis is the server with pid %d listening on port %d\n", getpid(), SERVER_PORT);

    // setup the server to bind and listen on a port
    int s = listen_on(SERVER_PORT);

    while (1) { // forever

        int msgsock = accept_connection(s); // wait for a client to connect
        printf("Got connection from client!");

        // handle the request with a new process
        handle_fork(msgsock);
    }

    close(s);
    exit(0);
}
