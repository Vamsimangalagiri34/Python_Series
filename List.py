# Initializing a list
my_list = [10, 20, 30, 40, 50]
print("Original List:", my_list)

# 1. Append - Add an element to the end
my_list.append(60)
print("After Append:", my_list)

# 2. Insert - Add an element at a specific position
my_list.insert(2, 25)  # Insert 25 at index 2
print("After Insert:", my_list)

# 3. Extend - Add multiple elements to the end
my_list.extend([70, 80])
print("After Extend:", my_list)

# 4. Pop - Remove and return an element (default last)
removed_element = my_list.pop()
print("After Pop (Removed):", removed_element, "| List:", my_list)

# 5. Remove - Remove the first occurrence of a value
my_list.remove(25)  # Remove the value 25
print("After Remove:", my_list)

# 6. Index - Find the index of a value
index_of_30 = my_list.index(30)
print("Index of 30:", index_of_30)

# 7. Count - Count occurrences of a value
count_of_40 = my_list.count(40)
print("Count of 40:", count_of_40)

# 8. Reverse - Reverse the list
my_list.reverse()
print("After Reverse:", my_list)

# 9. Sort - Sort the list in ascending order
my_list.sort()
print("After Sort:", my_list)

# 10. Copy - Create a shallow copy of the list
copied_list = my_list.copy()
print("Copied List:", copied_list)

# 11. Clear - Remove all elements from the list
my_list.clear()
print("After Clear:", my_list)

# 12. Access elements (Indexing)
print("Access 2nd element (Copied List):", copied_list[1])

# 13. Slicing
print("Slicing (Copied List, First 3 Elements):", copied_list[:3])

# 14. Length of the list
print("Length of Copied List:", len(copied_list))

# 15. Concatenation (using +)
new_list = copied_list + [90, 100]
print("After Concatenation:", new_list)

# 16. Repetition (using *)
repeated_list = copied_list * 2
print("After Repetition:", repeated_list)
