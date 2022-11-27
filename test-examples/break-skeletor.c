#include <stdio.h>
#include <string.h>


int main() {
    char* sWord = "skeletor";
    char bMod[8];
    bMod[0] = 8;
    bMod[1] = 9;
    bMod[2] = 10;
    bMod[3] = 0xb;
    bMod[4] = 0xc;
    bMod[5] = 0xd;
    bMod[6] = 0xe;
    bMod[7] = 0xf;
    for (int i = 0; i < strlen(sWord); i++) {
        printf("%c", *(sWord + i));
    }
    for (int i = 0; i < strlen(sWord); i++) {
        printf("%c", *(sWord + i) ^ bMod[i]);
    }
    return 0;
}