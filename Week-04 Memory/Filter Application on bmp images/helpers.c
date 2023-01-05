#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int b = image[i][j].rgbtBlue; //stores blue index value
            int r = image[i][j].rgbtRed; //stores red index value
            int g = image[i][j].rgbtGreen; //stores green index value
            int a = round((b + g + r) / 3.0); //averages all values and rounds to nearest integer
            image[i][j].rgbtBlue = a;
            image[i][j].rgbtRed = a;
            image[i][j].rgbtGreen = a;
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < (width / 2); j++)
        {
            int r = image[i][j].rgbtRed; //stores red index value
            int g = image[i][j].rgbtGreen; //stores green index value
            int b = image[i][j].rgbtBlue; //stores blue index value
            image[i][j].rgbtRed = image[i][width - j - 1].rgbtRed;
            image[i][j].rgbtGreen = image[i][width - j - 1].rgbtGreen;
            image[i][j].rgbtBlue = image[i][width - j - 1].rgbtBlue;
            image[i][width - j - 1].rgbtRed = r;
            image[i][width - j - 1].rgbtGreen = g;
            image[i][width - j - 1].rgbtBlue = b;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE temp[height][width]; // temporary image array to store the blured image
    int sr, sg, sb; // sum red, sum green, sum blue
    int ar, ag, ab; // average red, average green, average blue
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            sr = 0;
            sg = 0;
            sb = 0;
            float c = 0;
            for (int k = i - 1; k <= i + 1; k++)
            {
                for (int l = j - 1; l <= j + 1; l++)
                {
                    if (k >= 0 && k < height && l >= 0 && l < width) 
                    {
                        sr = sr + image[k][l].rgbtRed;
                        sg = sg + image[k][l].rgbtGreen;
                        sb = sb + image[k][l].rgbtBlue;
                        c = c + 1.0;;
                    }
                }
            }
            ar = round(sr / c);
            ag = round(sg / c);
            ab = round(sb / c);
            temp[i][j].rgbtRed = ar; 
            temp[i][j].rgbtGreen = ag;
            temp[i][j].rgbtBlue = ab;
        }
    }
    // copying the blured image form temporary array to image array
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            image[i][j] = temp[i][j];
        }
    }
    return;
}

// Detect edges
void edges(int height, int width, RGBTRIPLE image[height][width])
{
    int Gx[3][3] = { {-1, 0, 1}, {-2, 0, 2}, {-1, 0, 1} }; // Gx array
    int Gy[3][3] = { {-1, -2, -1}, {0, 0, 0}, {1, 2, 1} }; // Gy array
    int r, g, b; // stores red green blue indexes
    int sr, sg, sb;
    RGBTRIPLE temp[height][width]; // temporary image array to store the image from edge
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int gxr = 0; // Gx for red index
            int gxg = 0; // Gx for green index
            int gxb = 0; // Gx for blue index
            int gyr = 0; // Gy for red index
            int gyg = 0; // Gy for green index
            int gyb = 0; // Gy for blue index
            int e = 0;
            for (int k = i - 1; k <= i + 1; k++)
            {
                int f = 0;
                for (int l = j - 1; l <= j + 1; l++)
                {
                    if (k < 0 || k >= height || l < 0 || l >= width) 
                    {
                        // set r g b to black to act as a border
                        r = 0; 
                        g = 0;
                        b = 0;
                    }
                    else 
                    {
                        r = image[k][l].rgbtRed;
                        g = image[k][l].rgbtGreen;
                        b = image[k][l].rgbtBlue;
                    }
                    gxr = gxr + (r * Gx[e][f]);
                    gxg = gxg + (g * Gx[e][f]);
                    gxb = gxb + (b * Gx[e][f]);
                    gyr = gyr + (r * Gy[e][f]);
                    gyg = gyg + (g * Gy[e][f]);
                    gyb = gyb + (b * Gy[e][f]);
                    f++;
                }
                e++;
            }
            sr = round(sqrt((gxr * gxr) + (gyr * gyr)));
            if (sr > 255)
            {
                sr = 255;
            }
            sg = round(sqrt((gxg * gxg) + (gyg * gyg)));
            if (sg > 255)
            {
                sg = 255;
            }
            sb = round(sqrt((gxb * gxb) + (gyb * gyb)));
            if (sb > 255)
            {
                sb = 255;
            }
            temp[i][j].rgbtRed = sr;
            temp[i][j].rgbtGreen = sg;
            temp[i][j].rgbtBlue = sb;
        }
    }
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            image[i][j] = temp[i][j];
        }
    }
    return;
}
