#Write a program to count the number of even and odd numbers in a tuple.
nums = (1, 2, 3, 4, 5, 6)
even_count = len([x for x in nums if x % 2 == 0])
odd_count = len([x for x in nums if x % 2 != 0])
                
