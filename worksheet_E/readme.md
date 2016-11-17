worksheet_E

(a)

    s2 = 0
    s3 = s0

    s2 += s1
    s3 += -1

    while s3 != 0:
        s2 += s1
        s3 += -1

    # I know this is conventionally '-=' but I prefer multiple '+=' when reading addition code sequentially. (Also the literal equivalent of addi ... ... -1 is += -1 !)

(b)

The value in the s3 register acts as a counter, adding the value stored in s1 to itself n times, where n is the value stored in s3: the definition of multiplying s1 by n. Setting $s3 (or n) to the value stored in s0 will add $s1 to itself $s3 times before exiting the programs loop, leaving the result of $s1 * $s0 stored in the s2 register.

(c)

    s0 = 10
    s1 = 1

    while s0 != 0:
        s2 = 0
        s3 = s0

        while s3 != 0:
            s2 += s1
            s3 += -1

        s1 = s2
        s0 += -1
    
(d)

Using an embedded version of the answer to (a), the multiplying coefficient s0 (stored in s3 as before) decreases by one after ever multiplication iteration, within another loop which exits when it finally reaches 0. Using the example $s0 = n, the result is n * n-1 * n-2 * ... * 2 * 1 = $s1 which is the definition of n!

(e)

I tried a couple of mips simulators: Mars, PCSpim, and QtSpim. Failed to get any of them to work. At least I'm not a computing student! Although after reading the documentation I am confident that this is right.

        addi $s0, $zero, 10
        addi $s1, $zero, 1
    
    foo:mult $s1, $s0
        mflo $s1
        addi $so, $s0, -1
        bne $s0, $zero, foo
