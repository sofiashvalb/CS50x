#include <cs50.h>
#include <stdio.h>


bool valid_triangle(int x, int y, int z);

int main (int valid_triangle)
{
    if (valid_triangle == false)
    {
        printf("This is FALSE");
    }
    else
    {
        printf("TRUE Triangle");
    }
}

bool valid_triangle(int x, int y, int z)
{
    // check if the lengths are positive
    if ( x <= 0 || y <= 0 || z <= 0)
    {
        return false;
    }
    //check if the sums of every two legth is smaller then the third
    if (x + y <= z || y + z <= x || z + x <= y)
    {
        return  false;
    }
    // if passed both tests
    return true;
}