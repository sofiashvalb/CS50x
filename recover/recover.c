#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

// Constants
typedef uint8_t BYTE;
int const BLOCK_SIZE = 512;

// Main function
int main(int argc, char *argv[])
{
    // Check for usage
    if (argc != 2)
    {
        printf("Usage: ./recover file.raw");
        return 1;
    }

    // Open file
    FILE *raw_file = fopen(argv[1], "r");

    // If file could not be opened warn the user
    if (raw_file == NULL)
    {
        printf("File could not be opened");
        return 1;
    }

    // Generate jpg
    // Create couter for name of jpg
    unsigned int img_id = 0;

    // Create block for storing the blocks of read data
    BYTE block[BLOCK_SIZE];

    // Create the file pointer for the generated jpgs
    FILE *jpg_file = NULL;

    // Loop thru all blocks
    while (fread(block, 1, BLOCK_SIZE, raw_file) == BLOCK_SIZE)
    {
        // Run if block start is jpg header
        if (block[0] == 0xff && block[1] == 0xd8 && block[2] == 0xff && (block[3] & 0xf0) == 0xe0)
        {
            // Close only when a file has been opened
            if (jpg_file != NULL)
            {
                fclose(jpg_file);
            }

            //Generate the filename to follow the pattern ###.jpg where ###
            //is a 3 dijit number that is the id (the nth image) of the image
            char filename[8];
            sprintf(filename, "%03i.jpg", img_id);

            // Create a jpg in base of the filename
            jpg_file = fopen(filename, "w");

            // Increase img id
            img_id++;

            // If file could not be created warn the user
            if (raw_file == NULL)
            {
                printf("File could not be created");
                return 1;
            }
        }
        // If a file has already been opened write the data to it
        if (jpg_file != NULL)
        {
            fwrite(block, 1, BLOCK_SIZE, jpg_file);
        }
    }

    // Close file to prevent memory leaks
    fclose(raw_file);
    fclose(jpg_file); 
}