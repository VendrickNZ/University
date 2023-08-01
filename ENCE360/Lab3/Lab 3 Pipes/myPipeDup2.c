/* Title: pipedup2.c
 * Description: ENCE360 Example code - dup2.
 */

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>

#define INP 1
#define OUTP 0

int main(void) {
    int fd1[2], fd2[2];
    pid_t childpid;

    pipe(fd1);
    if ((childpid = fork()) == 0) { /* Child code: Runs ls */
        dup2(fd1[INP], STDOUT_FILENO);
        close(fd1[OUTP]);
        close(fd1[INP]);
        execl("/bin/ls", "ls", "-l", NULL);
        perror("The exec of ls failed");
    }
    pipe(fd2);
    if ((childpid = fork()) == 0) { /* Child code: Runs ls */
        close(fd1[INP]);
        close(fd2[OUTP]);
        
        dup2(fd1[OUTP], STDIN_FILENO);
        dup2(fd2[INP], STDOUT_FILENO);

        close(fd1[OUTP]);
        close(fd2[INP]);
        execl("/usr/bin/sort", "sort", "-k", "+9", NULL);
        /* Note: The location of sort depends on your distribution.
         * Use 'which sort' to find the correct location */
        perror("The exec of sort failed");
    }

    else { /* Parent code: Runs sort */
        close(fd1[OUTP]);
        close(fd1[INP]);
        
        dup2(fd2[OUTP], STDIN_FILENO);
        
        close(fd2[OUTP]);
        close(fd2[INP]);
        execl("/usr/bin/head", "head", "-5", NULL);
        perror("The exec of head failed");

    }

    exit(0);
}
