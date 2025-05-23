# Algorithm Module Comparison

A comprehensive Python module that implements various search and sorting algorithms with performance monitoring capabilities. This project includes both a command-line interface and a REST API for algorithm operations.

## Features

- **Search Algorithms**
  - Linear Search
  - Binary Search
  - Interpolation Search
  - Jump Search
  - Exponential Search

- **Sorting Algorithms**
  - Bubble Sort
  - Insertion Sort
  - Quick Sort
  - Selection Sort

- **Performance Monitoring**
  - Step counting
  - Execution time measurement
  - Debug mode for detailed analysis

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/AlgorithmsModuleComparison.git
cd AlgorithmsModuleComparison
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Basic Usage

```python
from Algorithms import Algorithms

# Initialize with a list and target value
algo = Algorithms(lst=[1, 2, 3, 4, 5], target=3)

# Perform search operations
result = algo.BinarySearch()  # Returns index of found value

# Perform sort operations
sorted_list = algo.QuickSort()  # Returns sorted list
```

### Debug Mode

```python
# Enable debug mode for detailed performance metrics
algo = Algorithms(lst=[1, 2, 3, 4, 5], target=3, debug=True)

# Search with performance metrics
result = algo.BinarySearch()
# Returns: (value, index, elapsed_time_ms, algorithm_name, steps)

# Sort with performance metrics
sorted_result = algo.QuickSort()
# Returns: (sorted_list, elapsed_time_ms, algorithm_name, steps)
```

### Using the GUI Application

Run the GUI application:
```bash
python GUI.py
```

The GUI provides:
- Input controls for list size and target value
- Buttons to generate sorted or random lists
- Dropdown menus to select algorithms for comparison
- Real-time performance comparison with:
  - Execution time in milliseconds
  - Number of steps/iterations
  - Visual results display
  - Syntax highlighting for better readability
- Dark theme interface
- Thread-safe algorithm execution

### Using the API

1. Start the API server:
```bash
uvicorn api:app --reload
```

2. Access the API endpoints:
- GET `/`: Welcome message
- GET `/get-item/{ID}`: Search for a student profile by ID

Example API request:
```bash
curl http://localhost:8000/get-item/224110775
```

### Example Scripts

1. **Sorting Student Profiles** (`sort.py`):
```python
from Algorithms import Algorithms
import json

# Load and sort student profiles
algo = Algorithms(lst=student_ids)
sorted_profiles = algo.QuickSort()
```

2. **Searching Student Profiles** (`search.py`):
```python
from Algorithms import Algorithms
import json

# Search for a specific student
algo = Algorithms(lst=student_ids, target=224110775)
result = algo.BinarySearch()
```

## Error Handling

The module includes custom error handling for common scenarios:
- Value not found in search operations
- Invalid input types
- Empty lists
- Algorithm type mismatches (search vs sort)

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is licensed under the MIT License - see the LICENSE file for details. 