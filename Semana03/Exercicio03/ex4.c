#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>

int spawn(char *program, char** arg_list){
    pid_t child_pid;

    child_pid = fork();
    if (child_pid != 0 ){
        return child_pid;
    }else{
        execvp(program, arg_list);
        fprintf(stderr, "an error ocurred in execvp\n"); //se der erro, dai ele retorna para esse programa e printa esse texto
        abort(); //Mata esse processo filho
    }
}


int main (){
    char *arg_list [] = {
        "ls",
        "-l",
        "/",
        NULL
    };

    spawn("ls", arg_list);
 


    return 0;
}