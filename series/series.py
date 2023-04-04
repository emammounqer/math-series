def fibonacci(n: int) -> int:
    """
    Return the nth number in the fibonacci sequence.

    Args:
        n (int): The index of the number in the sequence.

    Returns:
        int: The nth number in the fibonacci sequence.
    """
    if n == 0 or n == 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
