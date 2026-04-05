# des-implementation-python
Educational implementation of the DES (Data Encryption Standard) cipher in Python, including key schedule, Feistel rounds, ECB/CBC modes, and step-by-step understanding.
It was developed as part of my cryptography studies to understand how block ciphers work internally.

##  Why I built this

During my course, DES looked simple at a high level but confusing in practice.

So instead of just reading slides, I decided to implement it myself
to really understand:

- how permutations work  
- how S-boxes transform data  
- how the Feistel structure makes encryption reversible  
- why XOR is used everywhere  
- and how modes like ECB and CBC behave differently
- 
- ##  How DES works

1. Take a 64-bit block of plaintext  
2. Apply an initial permutation  
3. Split into two halves (L and R)  
4. Run 16 rounds:
   - expand R (32 → 48 bits)  
   - XOR with round key  
   - pass through S-boxes  
   - apply permutation  
   - combine with L using XOR  
5. Swap halves  
6. Apply final permutation  

Result: encrypted 64-bit block
