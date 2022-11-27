#include <stdio.h>
#include <string.h>

int main() {

    char* word1 = "Hello world";
    char* word2 = "Goodo world";

    printf("Word1: %s\n", word1);
    printf("Word2: %s\n", word2);

    for (int i = 0; i < strlen(word1); i++) {
        printf("i: %c\n", *(word1+i));
        //word1 = word1 + 1;
        printf("Word1: %s\n", word1);

        if (*word1 == *word2) {
            printf("Equal\n");
        }
    }
    return 0;
}