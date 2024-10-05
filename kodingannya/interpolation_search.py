import time
import random

def generate_sorted_array(size, lower_bound=0, upper_bound=1000):
    """Generate a sorted array of unique integers."""
    array = random.sample(range(lower_bound, upper_bound), size)
    array.sort()
    return array

def log_message(message):
    """Log messages for debugging and tracking."""
    print(f"[LOG] {message}")

def interpolation_search(arr, target):
    """
    Perform Interpolation Search on a sorted array.
    
    Parameters:
    arr (list): The sorted list to search.
    target (int): The value to search for.
    
    Returns:
    int: The index of the target if found, else -1.
    """
    low = 0
    high = len(arr) - 1

    log_message(f"Starting Interpolation Search for {target}")

    while low <= high and target >= arr[low] and target <= arr[high]:
        # Estimate the position of the target
        if arr[high] == arr[low]:
            if arr[low] == target:
                log_message(f"Found {target} at index {low}")
                return low
            else:
                log_message(f"{target} not found in the current range.")
                return -1

        pos = low + ((high - low) // (arr[high] - arr[low]) * (target - arr[low]))

        log_message(f"Estimated position: {pos}")

        if pos < low or pos > high:
            log_message(f"Estimated position {pos} out of bounds.")
            break

        if arr[pos] == target:
            log_message(f"Found {target} at index {pos}")
            return pos
        elif arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1

    log_message(f"{target} not found in the array.")
    return -1

def measure_search_time(search_function, arr, target):
    """Measure the time taken to search for a target value."""
    start_time = time.time()
    result = search_function(arr, target)
    end_time = time.time()
    return result, end_time - start_time

def test_interpolation_search():
    """Test the Interpolation Search implementation."""
    sizes = [10, 100, 1000, 5000, 10000]
    for size in sizes:
        arr = generate_sorted_array(size)
        target = random.choice(arr)  # Choose a target that is guaranteed to be in the array
        log_message(f"Testing Interpolation Search on array of size {size}...")
        
        index, duration = measure_search_time(interpolation_search, arr, target)
        
        if index != -1:
            log_message(f"Found {target} at index {index} in {duration:.6f} seconds.")
        else:
            log_message(f"Target {target} was not found, but it should be present.")

        # Test with a target that is definitely not in the array
        non_target = 9999  # Assuming this is outside the bounds of the generated array
        index, duration = measure_search_time(interpolation_search, arr, non_target)
        
        if index == -1:
            log_message(f"Correctly identified that {non_target} is not in the array in {duration:.6f} seconds.")

def main():
    """Main function to execute the Interpolation Search tests."""
    log_message("Starting Interpolation Search Tests...")
    test_interpolation_search()
    log_message("All tests completed.")

if __name__ == "__main__":
    main()
