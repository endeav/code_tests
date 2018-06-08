import os


def compute_max_sum(file_path):
    """
    Compute the maximum sum from top to bottom in a triangle
    :param file_path: The file's path
    :return: Sum as an integer
    """
    if os.path.getsize(file_path) == 0:
        raise ValueError('File is empty')

    with open(file_path, 'r') as f:
        # Read the file content and built a 2D array of integers
        data = [list(map(int, item.split())) for item in f.readlines()]

        # Not to miss the biggest sum, start adding from the bottom to the top
        reverse_data = data[::-1]
        max_sum = data[-1]
        for row in reverse_data[1:]:
            max_sum = list(max(max_sum[poz], max_sum[poz+1]) + item for poz, item in enumerate(row))
        return max_sum[0]
