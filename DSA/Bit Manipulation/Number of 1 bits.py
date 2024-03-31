
String Conversion:
Convert the integer to its binary string representation.
Count the number of '1' characters in the binary string
Complexity
⏱️ Time Complexity: O(log n), where n is the value of the input number.

🚀 Space Complexity:O(log n)
class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')

Bit Manipulation:
Initialize a count variable to 0.
Iterate through each bit of the number using a loop.
If the current bit is 1, increment the count.
The count variable now holds the number of 1 bits.
Complexity
⏱️ Time Complexity: O(log n), where n is the value of the input number.
🚀 Space Complexity: O(1)

class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            count += n%2  #count += n & 1  can be written as
            n = n>>1
        return count

#Kernighan's 
Intuition
The problem requires counting the number of set bits (bits with value 1) in the binary representation of a given integer.
Approach
Certainly! Kernighan's algorithm provides an efficient method for counting set bits in an integer's binary representation. The algorithm takes advantage of the fact that subtracting 1 from a number flips the rightmost set bit and sets all bits to its right to 1. For instance, when subtracting 1 from the binary number 1100, we get 1011, where the rightmost set bit and all subsequent bits are flipped.

To count the set bits in an integer n, Kernighan's algorithm employs an iterative process. We initialize a count variable to 0 and repeatedly unset the rightmost set bit of n while incrementing the count. By unsetting the rightmost set bit in each iteration, we effectively remove one set bit from n. We continue this process until n becomes zero, indicating that all set bits have been counted.

An advantage of Kernighan's algorithm is its efficiency, particularly for large integers. It avoids iterating through all bits of n, which could be inefficient. Instead, it selectively processes only the bits that are set, skipping over unset bits. This targeted approach minimizes unnecessary iterations, making the algorithm well-suited for counting set bits in large binary numbers.

Complexity
Time complexity: (O(num_set_bits)), where (num_set_bits) is the number of set bits in the binary representation of the input integer (n). In the worst case, when all bits of (n) are set, this algorithm will iterate through all bits.
Space complexity: (O(1)) - Constant space is used.
Code(Python)
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0  # Initialize a variable to count the number of set bits

        while n:  # Continue iterating until n becomes zero
            count += 1  # Increment the count for each set bit encountered
            # Unset the rightmost set bit by performing bitwise AND with (n - 1)
            n &= (n - 1)
        
        return count  # Return the total count of set bits
