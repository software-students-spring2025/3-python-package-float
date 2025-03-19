# MyCodeBuddy

A Python package designed to assist you throughout your coding projects. This package allows users to receive debugging tips, fun facts, resources for language help, and has a study timer to help users stay focused.

## Teammates

- [Angel Serrano](https://github.com/a-ngels)
- [Aria Nguyen](https://github.com/ariangn)
- [Melissa Kelly](https://github.com/melissalkelly)
- [Siyu Lei](https://github.com/em815)

## Link to package on PyPI
[MyCodeBuddyProject](https://test.pypi.org/project/mycodebuddyproject/0.1.2/#description)

## Developer Instructions

### Step 1: Install the Package
To use MyCodeBuddyProject in your project, first install it from PyPI. In your terminal or command prompt, type:
```
pip install mycodebuddyproject
```

### Step 2: Import Package
After installing the package, import mycodebuddyproject functions so they can be used directly in your code.

A sample program can be found [here](https://github.com/software-students-spring2025/3-python-package-float/blob/main/src/mycodebuddyproject/example.py).

```python
from mycodebuddyproject import debug_tip, get, language_help, StudyTimer

# example uses
print(debug_tip("runtime"))      # Get a debugging tip for runtime errors
print(language_help("python"))   # Get a documentation link for Python
print(get("features"))           # Get a fun fact about Python features
# last function here
```

## Functions

### `debug_tip(error_type)`
Returns a random debugging tip for the specified error type.
- **Parameters**:
   - `error_type` (str): The type of error ("syntax, "runtime", "logic").
- **Returns**: random debugging tip

#### Example
```python
debug_tip("runtime")
# Output: "Are you trying to divide by 0? This will cause an error."
```

### `language_help(language)`
Returns a link to documentation for a specified programming language.
- **Parameters**:
   - `language` (str): The programming language name.
- **Returns**: a link to documentation.

#### Example
```python
language_help("python")
# Output: "https://docs.python.org/3/"
```

### `get(fact_type)`
Returns a random fun fact for the specified fact type.
- **Parameters**:
   - `fact_type` (str): The type of fact ("features", "libraries", "trivia", "performance").
- **Returns**: random fun fact

#### Example 
```python
get("features")
# Output: "Python uses indentation (whitespace) to define code blocks instead of braces {}."
```

## Developer Contributions

If you’d like to contribute:

1. Clone the repository using:
   ```bash
   git clone https://github.com/software-students-spring2025/3-python-package-float.git
   cd 3-python-package-float
   ```
2. Create and run virtual environment
   ```bash
   # Install or update pipenv if needed
   pip install --upgrade pipenv

   # Create virtual environment and install dependencies
   pipenv install --dev

   # Activate virtual environment
   pipenv shell
   ```
3. Create a new branch and make your changes.
   ```bash
   git checkout -b branch-name
   ```

4. Run all pytests with the following command:
   ```bash
   pytest
   ```

5. Build the package with the following command:
   ```bash
   python -m build
   ```

6. Commit and push changes
   ```bash
   git add .
   git commit -m "description of changes"
   git push origin branch-name
   ```

7. Make a pull request on this projects repository on Github.
