#include <stdio.h>
#include <stdlib.h>

void error(const char*);

int main(int argc, char* argv[]) {

    if (argc < 4) {
        printf("Usage: ./db_trimmer 'path to .csv file' 'path to result file' number_of_rows_to_trim\n");
        error("Not enough arguments");
    }
        

    FILE* read_file = fopen(argv[2], "r");
    FILE* result_file = fopen(argv[3], "w+");

    int i = 0;
    int c = atoi(argv[1]);
    char* line;
    size_t len;
    ssize_t read;

    if (read_file == NULL) error("Cant open read file");
    if (result_file == NULL) error("Cant open write file");

    while ( (read = getline(&line, &len, read_file)) != -1 ) {
        if ( (i % c) == 0 ) {
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