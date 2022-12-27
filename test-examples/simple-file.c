#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>

int main() {
    int fd;
    char *output = "write to file";
    fd = open("testfile.txt", O_CREAT|O_WRONLY);
    int written = write(fd,output,13);
    int x = close(fd);
    return 0;
}