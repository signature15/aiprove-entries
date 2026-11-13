/* Count primes <= N (1 <= N <= 5,000,000) from stdin, print count to stdout.
 * Odd-only bit-packed Eratosthenes sieve. Build: gcc -O2 primes.c -o primes */
#include <stdio.h>
#include <stdlib.h>
int main(void){
    int n; if(scanf("%d",&n)!=1) return 1;
    if(n<2){ puts("0"); return 0; }
    unsigned char *s = (unsigned char*)calloc((size_t)n/16+2, 1);
    if(!s) return 2;
    int c = 1;                 /* count 2 */
    long long i, j;
    for(i=3; i*(long long)i<=n; i+=2)
        if(!((s[i>>4] >> ((i>>1)&7)) & 1))
            for(j=i*i; j<=n; j+=2*i)
                s[j>>4] |= (unsigned char)(1u << ((j>>1)&7));
    for(i=3; i<=n; i+=2)
        if(!((s[i>>4] >> ((i>>1)&7)) & 1)) c++;
    printf("%d\n", c);
    free(s);
    return 0;
}