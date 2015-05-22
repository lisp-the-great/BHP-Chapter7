#include <stdio.h>
#include <sys/stat.h>
#include <time.h>


// can only monitor keyboard

int main()
{
    struct stat f_info;
    // const char *file_name = "/dev/console";
    const char *file_name = "/dev/ttys000"; // tty, ttys001
    stat(file_name, &f_info);
    printf("%ld\n", time(NULL) - f_info.st_atime);
    return 0;
}
