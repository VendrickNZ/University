#include <stdio.h>
#include <signal.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/types.h>
#include <signal.h>

void handler(int sigNum);
void install_handler();

int counter = 0;

int main() {
    int child_pid;
    
    if ((child_pid = fork()) < 0) exit(1);
    
    if (child_pid == 0) {
        while(1) install_handler();
    }
    
    else {
        sleep(3);
        kill(child_pid, SIGQUIT);
        sleep(3);
        kill(child_pid, SIGQUIT);
    }
    
    return 0;
}

void handler(int sigNum) {
    if (sigNum == SIGQUIT) {
        write(1, "SIGQUIT\n", 8);
        counter++;

        if (counter == 2)
        {
            exit(0);
        }
    }
}

void install_handler() {
    signal(SIGQUIT, handler);
}
