#include <stdio.h>
#include <stdlib.h>

void trim_db(FILE*);
void error(const char*);

int main(int argc, char* argv[]) {

    if (argc < 3)
        error("Not enough arguments");

    FILE* read_file = fopen(argv[1], "r");
    FILE* result_file = fopen(argv[2], "w+");

    int i = 0;
    char* line;
    size_t len;
    ssize_t read;

    if (read_file == NULL) error("Cant open read file");
    if (result_file == NULL) error("Cant open write file");

    while ( (read = getline(&line, &len, read_file)) != -1 ) {
        if ( (i % 10) == 0 ) {
            printf("%s\n",line);
            fprintf(result_file, "%s", line);
        }
        i++;
    }


    fclose(read_file);
    fclose(result_file);

    return EXIT_SUCCESS;
}


void error(const char* errMsg) {
    perror(errMsg);
    exit(EXIT_FAILURE);
}