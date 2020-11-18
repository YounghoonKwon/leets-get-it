class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
            Link: https://leetcode.com/problems/longest-palindromic-substring/ (LC 5)
            Difficulty: Medium
            Language: Python
            Submission: Memory less than 100% and time faster than 98.45 % ( Runtime: 68 ms )
    
            Question:
                Given a string s, find the longest palindromic substring in s.
                You may assume that the maximum length of s is 1000.
    
            Sample Input 01:
                s = "babad"
            Sample Output 01:
                longest_palindromic_substring = "bab" ("aba" is also considered)
    
            Sample Input 02:
                s = "cbbd"
            Sample Output 02:
                longest_palindromic_substring = "bb"
    
            Approaches:
                1) Brute Force - O(len(s)*len(s)*len(s))
                     # Calculate all the substrings using two for loops - i from 0 to len(s) and j from i to len(s)
                     # Check whether the substring from i to j is palindrome or not (s[i:j] == s[i:j][::-1])
                     # If true and length of the substring is greater than the previous palindromic substring,
                     # Update the result with the current substring
                     # Return the result after the execution of the for loops
                2) Expanding by the centre - O(len(s)*len(s))
                    # Loop i from 0 to len(s)
                    # Consider the longest palindromic substring is s[0] and set the max length to 1
                    # Find if a palindromic substring exists with i as a centre.
                        # Case 1: For even length palindrome, the left and right values are set to i and i+1 with p as 0
                            # Expand until left and right are in boundaries and s[left]==s[right], left -= 1, right += 1
                            # Increase the length of the palindromic substring p by 2
                            # If the length of the palindromic substring is greater than max length
                            # Update the longest palindromic substring and max length accordingly (s[i-p//2+1:i+p//2+1])
                        # Case 2: For odd length palindrome, the left and right values are set to i-1, i+1 with p as 1
                            # Expand until left and right are in boundaries and s[left]==s[right], left -=1, right += 1
                            # Increase the length of the palindromic substring p by 2
                            # If the length of the palindromic substring is greater than max length
                            # Update the longest palindromic substring and max length accordingly (s[i-p//2:i+p//2+1])
                    # Return the longest palindromic substring
                3) Manacher's Algorithm - O(len(s)) - https://www.youtube.com/watch?v=nbTSfrEfo6M
        """
        # Convert the string to odd length by adding # after every character, and also $, % to mark the beginning and ending
        # of the string. Ex: aba -> $#a#b#a#%
        modified_string = ''
        for ch in s:
            modified_string += '#' + ch
        modified_string = '$' + modified_string + '#%'
    
        ps_lengths = [0] * len(modified_string)  # ps_lengths stands for palindromic substring lengths
        centre, right = 0, 0
    
        for i in range(1, len(modified_string)-1):  # Because we have to ignore the $, %
            # The character at index i, could be a part of a longest palindromic substring, in that case it finds the mirror
            # of the character on the left side of the centre.
            mirror = 2 * centre - i
    
            # Calculate the minimum palindromic substrings length, if they are in the range of longest palindromic substring
            if i < right:
                ps_lengths[i] = min(right-i, ps_lengths[mirror])
    
            while modified_string[i+(1+ps_lengths[i])] == modified_string[i-(1+ps_lengths[i])]:
                ps_lengths[i] += 1
    
            # If the palindromic substring with centre i has expanded over the right of the longest palindrome with centre c
            if i+ps_lengths[i] > right:
                centre = i
                right = i + ps_lengths[i]
    
        # Find the index of the max length
        max_length = max(ps_lengths)
        max_index = ps_lengths.index(max_length)
        longest_palindromic_substring = modified_string[max_index-max_length:max_index+max_length].replace('#', '')
        return longest_palindromic_substring    
