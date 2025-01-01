def greet(name: str) -> str:
    """
   Return a greeting message.

    Perameters:
       name (str): The name to greeting.

    Returns:
       str: A personalized greeting
    """
    return f"Hello,{name}!"

name = greet('Syed Umar Farooq')

print(name)