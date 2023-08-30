#include <stdio.h> 
#include <stdlib.h> 
#include <string.h> 
#include <netdb.h> 
#include <unistd.h>
#include <pthread.h>

#include <readline/readline.h>
#include <readline/history.h>


#define MAXDATASIZE 1024
#define SERVER_PORT 2000

int client_socket(char *hostname)
{
    char port[20];
    struct addrinfo hints, *their_addr = NULL;
    int sockfd;

    int n = snprintf(port, 20, "%d", SERVER_PORT);
    if ((n < 0) || (n >= 20))
    {
        printf("ERROR: Malformed Port\n");
        exit(EXIT_FAILURE);
    }

    sockfd = socket(AF_INET, SOCK_STREAM, 0);
    memset(&hints, 0, sizeof(struct addrinfo));
    hints.ai_family = AF_INET;
    hints.ai_socktype = SOCK_STREAM;

    int status = getaddrinfo(hostname, port, &hints, &their_addr);
    if (status != 0) {
        fprintf(stderr, "getaddrinfo: %s\n", gai_strerror(status));
        exit(EXIT_FAILURE);
    }

    if (connect(sockfd, their_addr->ai_addr, their_addr->ai_addrlen) != 0) {
        perror("connect");
        exit(EXIT_FAILURE);
    }

    freeaddrinfo(their_addr); // Free the linked list

    return sockfd;
}

void *read_thread(void *arg) {
    int sockfd = *(int *)arg;
    char buffer[MAXDATASIZE];
    int numbytes = 0;

    while ((numbytes = read(sockfd, buffer, MAXDATASIZE - 1)) > 0) {
        buffer[numbytes] = '\0';
        printf("server: %s\n", buffer);
    }

    return NULL;
}

int main(int argc, char *argv[])
{
    char buffer[MAXDATASIZE];

    if (argc != 2) {
        fprintf(stderr, "usage: client hostname\n");
        exit(1);
    }

    int sockfd = client_socket(argv[1]);

    pthread_t readThread;
    if (pthread_create(&readThread, NULL, read_thread, &sockfd) != 0) {
        perror("pthread_create");
        exit(EXIT_FAILURE);
    }

    int numbytes = 0;
    char *line;

    do {
        line = readline(">> ");
        write(sockfd, line, strlen(line));
    } while (1);

    free(line);
    close(sockfd);

    return 0;
}
