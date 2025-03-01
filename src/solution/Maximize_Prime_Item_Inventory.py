"""
write a query to find the number of prime and non-prime items that can be stored in the 500,000 square feet warehouse.
 Output the item type with prime_eligible followed by not_prime and the maximum number of items that can be stocked.
 For this task, you can assume the following.

Prime and non-prime items must be stored in equal amounts, regardless of their sizes or square footage.
This means that prime items will be stored separately from non-prime items in their respective containers, but within each container,
all items must be in the same amount.
Non-prime items must always be available in stock to meet customers demand, so the non-prime item count should never be zero.
Item count should be whole numbers (Integers).

Expected Table Output:

item_type	    | item_count
prime_eligible  | 9285
not_prime	    | 6
"""
