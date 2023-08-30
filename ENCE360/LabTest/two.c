#include <stdio.h>    
#include <stdlib.h>    
#include <unistd.h>   
#include <ctype.h>   // libraries to use
                      

void translator(int input_pipe[], int output_pipe[]) 
{ 
    int c; // user input int
    char ch; // to hold a character
    int rc; // return value

    /* first, close unnecessary file descriptors */ 
    close(input_pipe[1]); // close unnecessary input
    close(output_pipe[0]) // close unnecessary output

    /* enter a loop of reading from the user_handler's pipe, translating */ 
    /* the character, and writing back to the user handler.              */ 
    while (read(input_pipe[0], &ch, 1) > 0) { // while there is still characters to read from pipe
        c = ch; // ascii character = character
        if (isascii(c) && isupper(c)) // if ascii or uppercase
            c = tolower(c); // make it lower case
        ch = c; // cast it back to char from int

        /* write translated character back to user_handler. */ 
        rc = write(output_pipe[1], &ch, 1); // writes to the userhandler function
		if (rc == -1) {  // if there's an error, do some error handling and close your pipes to free up space
            perror("translator: write"); 
            close(input_pipe[0]); 
            close(output_pipe[1]); 
            exit(1); 
        } 
    } 

    close(input_pipe[0]); // close the pipes to free up space
    close(output_pipe[1]); 
    exit(0); 
} 



void user_handler(int input_pipe[], int output_pipe[]) 
{ 
    int c;    /* user input - must be 'int', to recognize EOF (= -1). */ 
    char ch;  /* the same - as a char. */ 
    int rc;   /* return values of functions. */ 

    /* first, close unnecessary file descriptors */ 
    close(output_pipe[1]); // close output pipe fd you wont need
    close(input_pipe[0]); // close input pipe fd you wont need

	printf("Enter text to translate:\n"); // print to console/user
    /* loop: read input from user, send via one pipe to the translator, */ 
    /* read via other pipe what the translator returned, and write to   */ 
    /* stdout. exit on EOF from user.                                   */ 
    while ((c = getchar()) > 0) {  // while there's still a character left to parse
        ch = (char)c; // cast int c into char

        /* write to translator */ 
        rc = write(input_pipe[1], &ch, 1); // write to input pipe fd to translate
        if (rc == -1) { /* write failed - notify the user and exit. */ 
            perror("user_handler: write"); // error handling and closing pipes fds for space
            close(input_pipe[0]); 
            close(output_pipe[1]); 
            exit(1); 
        } 

        /* read back from translator */ 
        ch = read(output_pipe[0], &ch, 1);

        c = (int)ch; // type cast to int again
        if (rc <= 0) {  // error handling
            perror("user_handler: read"); 
            close(input_pipe[0]); 
            close(output_pipe[1]); 
            exit(1); 
        } 

		putchar(c);// writes to stream
		if (c=='\n' || c==EOF) break; // checking for end of file
    } 

    close(input_pipe[0]); // close file descriptors
    close(output_pipe[1]); 
    exit(0); 
} 

int main(int argc, char* argv[]) 
{ 
    int user_to_translator[2]; // file descriptor for one of pipes
    int translator_to_user[2]; // file descriptor for the other pipe
    int pid;        // pid to identify whether you are in the child or parent
    int rc;         // return value of pipe to check for errors

    rc = pipe(user_to_translator); // creating a pipe out of the first file descriptor
    if (rc == -1) {  // these 3 lines are just error handling
        perror("main: pipe user_to_translator"); 
        exit(1); 
    } 

	rc = pipe(translator_to_user); // creating another pipe out the second file descriptor
    if (rc == -1) {  // these 3 lines for error handling
        perror("main: pipe translator_to_user"); 
        exit(1); 
    } 

    pid = fork(); // forking a new process

    switch (pid) {  // elegant way of checking where you are
        case -1:      // these 3 lines are error handling
            perror("main: fork"); 
            exit(1); 
        case 0:   // if you are in the child (pid == 0)
            translator(user_to_translator, translator_to_user); /* line 'A' */ // call the translator function and give the file descriptors as arguments
			exit(0); // exit when finished as parent
        default:         
            user_handler(translator_to_user, user_to_translator); /* line 'B' */ //call the user_handler function and give the file descriptors as arguments
    } 

    return 0;   
}



/* Show below the output for the following input: I wish YOU a HAPPY new YEAR
"i wish you a happy new year"

It reduces all of the chars to lowercase individually.
*/