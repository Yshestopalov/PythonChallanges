# The Sieve of Eratosthenes - www.101computing.net/the-sieve-of-eratosthenes

# --- Input Data ---

LAST_INTEGER = 100

# --- Process ---

def sieve_of_eratosthenes(last_integer):
    """Finds all prime numbers between the interval 0 to last_integer.
    
    Args:
        last_integer (int): The end of the interval.

    Returns:
        list: A list containing all prime numbers in the interval.
    """
    # boolean list to track prime numbers
    is_prime = [True] * (last_integer + 1)

    # 0 and 1 are not prime numbers
    is_prime[0] = is_prime[1] = False

    # Sieve algorithm
    # Optimized range for faster result
    for number in range(2, int(last_integer**0.5) + 1):
        if is_prime[number]:
            # Avoid retrying already marked multiples like number * 2
            for multiple in range(number ** 2, last_integer + 1, number):
                is_prime[multiple] = False

    # Combine prime numbers
    primes = []
    for number in range(2, last_integer + 1):
        if is_prime[number]:
            primes.append(number)

    return primes

# --- Calculations and Output ---

prime_numbers = sieve_of_eratosthenes(LAST_INTEGER)

print(f"Prime numbers up to {LAST_INTEGER}:")
for prime in prime_numbers:
    print(prime, end=" ")
