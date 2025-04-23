#include "helpers.h"
#include <math.h>

#define RED_COLOR 0
#define GREEN_COLOR 1
#define BLUE_COLOR 2

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int row = 0; row < height; row++)
    {
        for (int col = 0; col < width; col++)
        {
            int avg = round((image[row][col].rgbtBlue + image[row][col].rgbtGreen + image[row][col].rgbtRed) / 3.0);
            image[row][col].rgbtRed = avg;
            image[row][col].rgbtBlue = avg;
            image[row][col].rgbtGreen = avg;
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    for (int row = 0; row < height; row++)
    {
        for (int col = 0; col < width; col++)
        {
            int sepiaBlue =
                round(0.272 * image[row][col].rgbtRed + 0.534 * image[row][col].rgbtGreen + 0.131 * image[row][col].rgbtBlue);
            int sepiaGreen =
                round(0.349 * image[row][col].rgbtRed + 0.686 * image[row][col].rgbtGreen + 0.168 * image[row][col].rgbtBlue);
            int sepiaRed =
                round(0.393 * image[row][col].rgbtRed + 0.769 * image[row][col].rgbtGreen + 0.189 * image[row][col].rgbtBlue);

            image[row][col].rgbtRed = fmin(255, sepiaRed);
            image[row][col].rgbtBlue = fmin(255, sepiaBlue);
            image[row][col].rgbtGreen = fmin(255, sepiaGreen);
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE buffer;
    for (int row = 0; row < height; row++)
    {
        for (int col = 0; col < width / 2; col++)
        {
            buffer = image[row][col];
            image[row][col] = image[row][width - col - 1];
            image[row][width - col - 1] = buffer;
        }
    }
    return;
}

int getBlur(int i, int j, int height, int width, RGBTRIPLE image[height][width], int color_pos)
{
    float count = 0;
    int sum = 0;
    for (int row = i - 1; row <= i + 1; row++)
    {
        for (int col = j - 1; col <= j + 1; col++)
        {
            if (row < 0 || row >= height || col < 0 || col >= width)
            {
                continue;
            }
            if (color_pos == RED_COLOR)
            {
                sum += image[row][col].rgbtRed;
            }
            else if (color_pos == GREEN_COLOR)
            {
                sum += image[row][col].rgbtGreen;
            }
            else if (color_pos == BLUE_COLOR)
            {
                sum += image[row][col].rgbtBlue;
            }
            count++;
        }
    }
    return round(sum / count);
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE buffer[height][width];
    for (int row = 0; row < height; row++)
    {
        for (int col = 0; col < width; col++)
        {
            buffer[row][col] = image[row][col];
        }
    }
    for (int row = 0; row < height; row++)
    {
        for (int col = 0; col < width; col++)
        {
            image[row][col].rgbtRed = getBlur(row, col, height, width, buffer, RED_COLOR);
            image[row][col].rgbtGreen = getBlur(row, col, height, width, buffer, GREEN_COLOR);
            image[row][col].rgbtBlue = getBlur(row, col, height, width, buffer, BLUE_COLOR);
        }
    }
    return;
}
