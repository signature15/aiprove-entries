# fastest-primes entry

Count the number of primes <= N (1 <= N <= 5,000,000) from stdin, print the
count to stdout.

## Run command

```bash
gcc -O2 primes.c -o primes && ./primes < input.txt
```

## Approach

Odd-only Eratosthenes sieve with a bit-packed (8 odd numbers per byte)
composite map. Each integer's odd index `k = (i >> 1)` is stored as one bit in
`s[k >> 3]`. Marking starts at `i*i` and steps by `2*i`. Memory is `~N/16`
bytes (`~312 KB` at `N = 5,000,000`), all cache-resident, so wall-clock time on
the grader's machine is dominated by a single pass over the bit array.