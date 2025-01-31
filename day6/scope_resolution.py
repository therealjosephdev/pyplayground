# variable scope = where a variable is visible and accessible
# scope resolution =
# L: Local 🏠 – Variables defined inside a function.
# E: Enclosing 📦 – Variables in an outer function (for nested functions).
# G: Global 🌍 – Variables defined at the top level of a script or module.
# B: Built-in 🏗️ – Predefined names in Python (like print, len, etc.).
# Python searches for a variable in this specific order
# (LEGB), and if it doesn't find it, you'll get a NameError.

# 1️⃣ Local Scope (Inside a Function)
# def my_function():
#     x = 10  # Local variable
#     print(x)  # Accessible here

# my_function()
# print(x)  # ❌ Error: 'x' is not defined outside the function

# 🔍 Key Takeaway
# x is local to my_function(), meaning it only exists inside the function.
# If you try to access x outside the function, Python will give an error.

# 2️⃣ Enclosing Scope (Nested Functions)
# def outer():
#     y = 20  # Enclosing variable

#     def inner():
#         print(y)  # Inner function can access y

#     inner()

# outer()

# 🔍 Key Takeaway
# The inner function (inner()) can access y, even though y is not defined inside it.
# But y is still not global—it only exists inside outer().

# 3️⃣ Global Scope (Accessible Everywhere)
# A variable defined outside of any function is a global variable.
# It can be accessed inside functions,
# but modifying it requires the global keyword.

# z = 30  # Global variable

# def my_function():
#     print(z)  # Can access global z

# my_function()
# print(z)  # Still accessible here

# 🔍 Key Takeaway
# z is a global variable, so my_function() can read it.
# But if you want to modify it inside the function, you need global.

# Modifying a Global Variable in a Function

# a = 5  # Global variable

# def modify_global():
#     global a  # Declare a as global
#     a = 10    # Now we're modifying the global 'a'

# modify_global()
# print(a)  # Output: 10 (a was changed globally)

# Without global, Python will create a new local variable instead of modifying the global one.

# 4️⃣ Built-in Scope (Python’s Predefined Functions)
# Python has built-in functions and constants, like print() and len(),
# which are always available.

# print(len("hello"))  # 'len' is a built-in function

# # If you create a variable with the same name as a built-in function, Python will override it in your scope.

# len = 100  # This overrides the built-in 'len'
# print(len)  # Output: 100

# # print(len("hello"))  # ❌ Error: 'int' object is not callable

# 🔄 Summary of LEGB Order
# When Python encounters a variable, it looks in the following order:

# 1. Local (Inside the function)
# 2. Enclosing (If there's a nested function)
# 3. Global (If not found in local or enclosing)
# 4. Built-in (Python's built-in names)

# Example:

# x = "global"  # Global

# def outer():
#     x = "enclosing"  # Enclosing
    
#     def inner():
#         x = "local"  # Local
#         print(x)  # Finds 'local' first

#     inner()

# outer()
# print(x)  # Still prints 'global' since outer() didn't modify it

# What does this print?
# ✅ "local" from inner(), because Python follows LEGB.

