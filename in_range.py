def in_range(nums, lowest, highest):
    """Print numbers inside range.

    - nums: list of numbers
    - lowest: lowest number to print
    - highest: highest number to print

    For example:

      in_range([10, 20, 30, 40], 15, 30)

    should print:

      20 fits
      30 fits
    """
    newrange = [num for num in nums if num >= lowest and num <= highest]
    newrange.sort()

    for x in newrange:
        print(f"{x} fits")

    # YOUR CODE HERE


in_range([10, 20, 30, 40, 50], 15, 30)            
in_range([10,55,75,90, 20,21,22,25, 30, 40, 50], 15, 80)  
