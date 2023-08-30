#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <netdb.h> 
#include <errno.h>
#include <unistd.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <pthread.h>

#define MAXDATASIZE 1024 // max buffer size 
#define SERVER_PORT 2000
#define MAX_CONNECTIONS 5

void* child_thread(void* arg);

int connections[MAX_CONNECTIONS];
int next_index = 0;
pthread_mutex_t mutex;

int listen_on(int port)
{

    int s = socket(AF_INET, SOCK_STREAM, 0);

    struct sockaddr_in sa;
    sa.sin_family = AF_INET;
    sa.sin_addr.s_addr = INADDR_ANY; 
    sa.sin_port = htons(port); 

    int rc = bind(s, (struct sockaddr *)&sa, sizeof(sa));
    if (rc == -1) {
        perror("bind");
        exit(1);
    }

    rc = listen(s, 5); 
    if (rc == -1) {
        perror("listen");
        exit(1);
    }

    return s;
}


int accept_connection(int s) {
    struct sockaddr_storage caller;
    socklen_t length = sizeof(caller);
    int msgsock = accept(s, (struct sockaddr *)&caller, &length);
    pthread_mutex_lock(&mutex);
    if (next_index < MAX_CONNECTIONS) {
        for (int i = 0; i < MAX_CONNECTIONS; i++) {
            if (connections[i] == -1) {
                connections[i] = msgsock;
                next_index++;
                break;
            }
        }
    } else {
        printf("Server full!");
        exit(0);
    }
    pthread_mutex_unlock(&mutex);
    return msgsock;
}


void handle_request(int msgsock) {
    char buffer[MAXDATASIZE];
    int num_read = 0;

    num_read = read(msgsock, buffer, MAXDATASIZE - 1);
    buffer[num_read] = '\0';

    printf("read a message %d bytes: %s\n", num_read, buffer);

    while (num_read > 0) {
        buffer[num_read] = '\0';
        printf("read a message %d bytes: %s\n", num_read, buffer);
        pthread_mutex_lock(&mutex);
        for (int i = 0; i < MAX_CONNECTIONS; i++) {
            if (connections[i] != -1 && connections[i] != msgsock) {
                write(connections[i], buffer, num_read);
            }
        }
        pthread_mutex_unlock(&mutex);
        num_read = read(msgsock, buffer, MAXDATASIZE-1);
    }
    close(msgsock);
    pthread_mutex_lock(&mutex);
    for (int i = 0; i < MAX_CONNECTIONS; i++) {
        if (connections[i] == msgsock) {
            connections[i] = -1;
        }
    }
    pthread_mutex_unlock(&mutex);
}


void handle_thread(int msgsock) {
    pthread_t childId;
    int* pclient = malloc(sizeof(int));
    *pclient = msgsock;
    if(pthread_create(&childId, NULL, child_thread, pclient) != 0) {
        perror("create");
        exit(1);
    } else {
        pthread_detach(childId);
    }
}

void* child_thread(void* arg) {
    int msgsock = *(int*)arg;
    free(arg);
    handle_request(msgsock);
    return NULL;
}

int main(int argc, char *argv[]) {
    for (int i = 0; i < MAX_CONNECTIONS; i++) {
        connections[i] = -1;
    }
    printf("\nThis is the server with pid %d listening on port %d\n", getpid(), SERVER_PORT);

    int s = listen_on(SERVER_PORT);

    while (1) { // forever
        int msgsock = accept_connection(s);
        printf("Got connection from client!\n");

        handle_thread(msgsock);
    }

    close(s);
    exit(0);
}

