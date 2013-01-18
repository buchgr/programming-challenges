/**
 * Program to reverse a binary number as specified
 * by Spotify's tech puzzle at
 * http://www.spotify.com/at/jobs/tech/reversed-binary/
 */
#include <stdlib.h>
#include <stdio.h>
#include <math.h>

int main(int argc, char** argv) {
    int n;
    scanf("%d", &n);

    // Ensure the variable is in range
    if (n < 1 || n > 1000000000) {
        return -1;
    }

    // determine the position of the leftmost bit
    // that is set
    int m = n;
    int leftmost = -1;
    while (m > 0) {
        leftmost++;
        m >>= 1;
    }
   
    // reverse the binary number 
    int i,j;
    int reversednumber = 0;
    for (i=0, j=leftmost; i <= j; ++i, --j) {
        // if the jth bit is set in the original number
        // set the ith bit in the reversed number
        if (n & (1 << j)) reversednumber |= (1 << i);
        
        // if the ith bit is set in the original number
        // set the jth bit in the reversed number
        if (n & (1 << i)) reversednumber |= (1 << j);
    }

    printf("%d", reversednumber);
}
