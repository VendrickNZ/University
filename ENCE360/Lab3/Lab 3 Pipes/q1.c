#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>
#include <sys/wait.h>

#define INP 1
#define OUTP 0

int main(void) {
    int fd[2];
    pid_t childpid;

    pipe(fd);
    if ((childpid = fork()) == 0) { 
        close(fd[OUTP]);
        dup2(fd[INP], STDOUT_FILENO);
        close(fd[INP]);

        execl("/bin/sort", "sort", NULL);
        perror("The exec of sort failed");
    }

    else { 
        wait(NULL);
        close(fd[INP]);
        dup2(fd[OUTP], STDIN_FILENO);
        close(fd[OUTP]);

        execl("/usr/bin/head", "head", "-n", "2", NULL);
        perror("The exec of head failed");
    }

    exit(0);
}