#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <unistd.h> // basic libraries to include

void *print_message_function( void *ptr ); // function prototype so you can call the function before you have made it

int main() // main
{
	pthread_t childPid; // creating a new thread object for the child
	pthread_create(&childPid, NULL, print_message_function, NULL); // creating and initializing a new thread that runs print_message_function with no parameters
	sleep(1); // sleeps for a second
	return(0); // returns
}

void *print_message_function( void *ptr ) // the function that the child will be running
{
	printf("child thread\n"); // prints that we are in the child thread
	sleep(5); // sleeps for 5 seconds
	printf("Hello World\n"); // prints Hello World
	pthread_exit(NULL); // terminates the thread (not the whole process)
}

/**
When you sleep in the parent for 1 second, and do not sleep in the child, it successfully
prints "Hello World" in the child. When you add a 5 second delay in the child before the print, 
it does not print "Hello World", and the code exits. The reason this occurs is the parent thread
has terminated before the child, so the child is becomes a zombie thread where it will continue to 
exist as I don't think anything will actively terminate it until something large happens like
restarting the PC.

"If the main parent thread finishes before a child thread, does that child thread still continue?"
Yes. It becomes a zombie thread that will sit there for a very long time. You fix this by calling
something like wait() in the parent to confirm that its children have terminated before allowing
the parent to terminate itself.
*/