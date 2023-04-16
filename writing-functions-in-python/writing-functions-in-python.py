# Add a docstring to count_letter()
def count_letter(content, letter):
  """Count the number of times `letter` appears in `content`."""
  if (not isinstance(letter, str)) or len(letter) != 1:
    raise ValueError('`letter` must be a single character string.')
  return len([char for char in content if char == letter])

def count_letter(content, letter):
  """Count the number of times `letter` appears in `content`.

  # Add a Google-style arguments section
  Args:
    content (str): The string to search.
    letter (str): The letter to search for.
  """
  if (not isinstance(letter, str)) or len(letter) != 1:
    raise ValueError('`letter` must be a single character string.')
  return len([char for char in content if char == letter])

def count_letter(content, letter):
  """Count the number of times `letter` appears in `content`.

  Args:
    content (str): The string to search.
    letter (str): The letter to search for.

  # Add a returns section
  Returns:
    int
  """
  if (not isinstance(letter, str)) or len(letter) != 1:
    raise ValueError('"letter" must be a single character string.')
  return len([char for char in content if char == letter])

def count_letter(content, letter):
  """Count the number of times `letter` appears in `content`.

  Args:
    content (str): The string to search.
    letter (str): The letter to search for.

  Returns:
    int

  # Add a section detailing what errors might be raised
  Raises:
    ValueError: If `letter` is not a one-character string.
  """
  if (not isinstance(letter, str)) or len(letter) != 1:
    raise ValueError('`letter` must be a single character string.')
  return len([char for char in content if char == letter])

# Get the "count_letter" docstring by using an attribute of the function
docstring = count_letter.__doc__

border = '#' * 28
print('{}\n{}\n{}'.format(border, docstring, border))

import inspect


# Inspect the count_letter() function to get its docstring
docstring = inspect.getdoc(count_letter)

border = '#' * 28
print('{}\n{}\n{}'.format(border, docstring, border))

import inspect

def build_tooltip(function):
  """Create a tooltip for any function that shows the
  function's docstring.

  Args:
    function (callable): The function we want a tooltip for.

  Returns:
    str
  """
  # Get the docstring for the "function" argument by using inspect
  docstring = inspect.getdoc(function)
  border = '#' * 28
  return '{}\n{}\n{}'.format(border, docstring, border)

print(build_tooltip(count_letter))
print(build_tooltip(range))
print(build_tooltip(print))

# edited/added
import pandas as pd
df = pd.read_csv("students.csv")

def standardize(column):
  """Standardize the values in a column.

  Args:
    column (pandas Series): The data to standardize.

  Returns:
    pandas Series: the values as z-scores
  """
  # Finish the function so that it returns the z-scores
  z_score = (column - column.mean()) / column.std()
  return z_score


# Use the standardize() function to calculate the z-scores
df['y1_z'] = standardize(df.y1_gpa)
df['y2_z'] = standardize(df.y2_gpa)
df['y3_z'] = standardize(df.y3_gpa)
df['y4_z'] = standardize(df.y4_gpa)
def mean(values):
  """Get the mean of a sorted list of values

  Args:
    values (iterable of float): A list of numbers

  Returns:
    float
  """
  # Write the mean() function
  mean = sum(values) / len(values)
  return mean

def median(values):
  """Get the median of a sorted list of values

  Args:
    values (iterable of float): A list of numbers

  Returns:
    float
  """
  # Write the median() function
  midpoint = int(len(values) / 2)
  if len(values) % 2 == 0:
    median = (values[midpoint - 1] + values[midpoint]) / 2
  else:
    median = values[midpoint]
  return median

# Use an immutable variable for the default argument
def better_add_column(values, df=None):
  """Add a column of `values` to a DataFrame `df`.
  The column will be named "col_<n>" where "n" is
  the numerical index of the column.

  Args:
    values (iterable): The values of the new column
    df (DataFrame, optional): The DataFrame to update.
      If no DataFrame is passed, one is created by default.

  Returns:
    DataFrame
  """
  # Update the function to create a default DataFrame
  if df is None:
    df = pandas.DataFrame()
  df['col_{}'.format(len(df.columns))] = values
  return df

# Open "alice.txt" and assign the file to "file"
with open('alice.txt') as file:
  text = file.read()

n = 0
for word in text.split():
  if word.lower() in ['cat', 'cats']:
    n += 1

print('Lewis Carroll uses the word "cat" {} times'.format(n))

# edited/added
import numpy as np
import time
import contextlib
def get_image_from_instagram():
  return np.random.rand(84, 84)
def _process_pic(n_sec):
  print('Processing', end='', flush=True)
  for i in range(10):
    print('.', end='' if i < 9 else 'done!\n', flush=True)
    time.sleep(n_sec)
def process_with_pytorch(p):
  _process_pic(0.0328)
def process_with_numpy(p):
  _process_pic(0.1521)
@contextlib.contextmanager
def timer():
  """Time how long code in the context block takes to run."""
  t0 = time.time()
  try:
      yield
  except:
    raise
  finally:
    t1 = time.time()
    print('Elapsed: {:.2f} seconds'.format(t1 - t0))

image = get_image_from_instagram()


# Time how long process_with_numpy(image) takes to run
with timer():
  print('Numpy version')
  process_with_numpy(image)


# Time how long process_with_pytorch(image) takes to run
with timer():
  print('Pytorch version')
  process_with_pytorch(image)

# Add a decorator that will make timer() a context manager
@contextlib.contextmanager
def timer():
  """Time the execution of a context block.

  Yields:
    None
  """
  start = time.time()
  # Send control back to the context block
  yield
  end = time.time()
  print('Elapsed: {:.2f}s'.format(end - start))

with timer():
  print('This should take approximately 0.25 seconds')
  time.sleep(0.25)
@contextlib.contextmanager
def open_read_only(filename):
  """Open a file in read-only mode.

  Args:
    filename (str): The location of the file to read

  Yields:
    file object
  """
  read_only_file = open(filename, mode='r')
  # Yield read_only_file so it can be assigned to my_file
  yield read_only_file
  # Close read_only_file
  read_only_file.close()

with open_read_only('my_file.txt') as my_file:
  print(my_file.read())

# edited/added
class MockStock:
    def __init__(self, loc, scale):
        self.loc = loc
        self.scale = scale
        self.recent = list(np.random.laplace(loc, scale, 2))
    def price(self):
        sign = np.sign(self.recent[1] - self.recent[0])
        # 70% chance of going same direction
        sign = 1 if sign == 0 else (sign if np.random.rand() > 0.3 else -1 * sign)
        new = self.recent[1] + sign * np.random.rand() / 10.0
        self.recent = [self.recent[1], new]
        return new
@contextlib.contextmanager
def stock(symbol):
    base = 140.00
    scale = 1.0
    mock = MockStock(base, scale)
    print('Opening stock ticker for {}'.format(symbol))
    yield mock
    print('Closing stock ticker')

# Use the "stock('NVDA')" context manager
# and assign the result to the variable "nvda"
with stock('NVDA') as nvda:
  # Open 'NVDA.txt' for writing as f_out
  with open('NVDA.txt', 'w') as f_out:
    for _ in range(10):
      value = nvda.price()
      print('Logging ${:.2f} for NVDA'.format(value))
      f_out.write('{:.2f}\n'.format(value))
def in_dir(directory):
  """Change current working directory to `directory`,
  allow the user to run some code, and change back.

  Args:
    directory (str): The path to a directory to work in.
  """
  current_dir = os.getcwd()
  os.chdir(directory)

  # Add code that lets you handle errors
  try:
    yield
  # Ensure the directory is reset,
  # whether there was an error or not
  finally:
    os.chdir(current_dir)

# edited/added
import random
def get_user_input(prompt='Type a command: '):
    command = random.choice(['mean', 'std', 'minimum', 'maximum'])
    print(prompt)
    print('> {}'.format(command))
    return command
def mean(data):
    print(data.mean())
def std(data):
    print(data.std())
def minimum(data):
    print(data.min())
def maximum(data):
    print(data.max())
def load_data():
    df = pd.DataFrame()
    df['height'] = [72.1, 69.8, 63.2, 64.7]
    df['weight'] = [198, 204, 164, 238]
    return df


# Add the missing function references to the function map
function_map = {
      'mean': mean,
  'std': std,
  'minimum': minimum,
  'maximum': maximum
}

data = load_data()
print(data)

func_name = get_user_input()


# Call the chosen function and pass "data" as an argument
function_map[func_name](data)

# edited/added
def has_docstring(func):
    """Check to see if the function
    `func` has a docstring.
    Args:
        func (callable): A function.
    Returns:
        bool
    """
    return func.__doc__ is not None
def load_and_plot_data(filename):
    """Load a data frame and plot each column.
    Args:
        filename (str): Path to a CSV file of data.
    Returns:
        pandas.DataFrame
    """
    df = pd.load_csv(filename, index_col=0)
    df.hist()
    return df
def as_2D(arr):
    """Reshape an array to 2 dimensions"""
    return np.array(arr).reshape(1, -1)
def log_product(arr):
    return np.exp(np.sum(np.log(arr)))


# Call has_docstring() on the load_and_plot_data() function
ok = has_docstring(load_and_plot_data)

if not ok:
  print("load_and_plot_data() doesn't have a docstring!")
else:
  print("load_and_plot_data() looks ok")

  # Call has_docstring() on the as_2D() function
ok = has_docstring(as_2D)

if not ok:
  print("as_2D() doesn't have a docstring!")
else:
  print("as_2D() looks ok")


# Call has_docstring() on the log_product() function
ok = has_docstring(log_product)

if not ok:
  print("log_product() doesn't have a docstring!")
else:
  print("log_product() looks ok")
def create_math_function(func_name):
  if func_name == 'add':
    def add(a, b):
      return a + b
    return add
  elif func_name == 'subtract':
    # Define the subtract() function
    def subtract(a, b):
      return a - b
    return subtract
  else:
    print("I don't know that one")

add = create_math_function('add')
print('5 + 2 = {}'.format(add(5, 2)))

subtract = create_math_function('subtract')
print('5 - 2 = {}'.format(subtract(5, 2)))
call_count = 0

def my_function():
  # Use a keyword that lets us update call_count
  global call_count
  call_count += 1

  print("You've called my_function() {} times!".format(
        call_count
  ))

for _ in range(20):
  my_function()

def read_files():
  file_contents = None

  def save_contents(filename):
    # Add a keyword that lets us modify file_contents
    nonlocal file_contents
    if file_contents is None:
      file_contents = []
    with open(filename) as fin:
      file_contents.append(fin.read())

  for filename in ['1984.txt', 'MobyDick.txt', 'CatsEye.txt']:
    save_contents(filename)

  return file_contents

print('\n'.join(read_files()))

def wait_until_done():
  def check_is_done():
    # Add a keyword so that wait_until_done()
    # doesn't run forever
    global done
    if random.random() < 0.1:
      done = True

  while not done:
    check_is_done()

done = False
wait_until_done()

print('Work done? {}'.format(done))
def return_a_func(arg1, arg2):
  def new_func():
    print('arg1 was {}'.format(arg1))
    print('arg2 was {}'.format(arg2))
  return new_func

my_func = return_a_func(2, 17)


# Show that my_func()'s closure is not None
print(my_func.__closure__ is not None)

def return_a_func(arg1, arg2):
  def new_func():
    print('arg1 was {}'.format(arg1))
    print('arg2 was {}'.format(arg2))
  return new_func

my_func = return_a_func(2, 17)

print(my_func.__closure__ is not None)


# Show that there are two variables in the closure
print(len(my_func.__closure__) == 2)

def return_a_func(arg1, arg2):
  def new_func():
    print('arg1 was {}'.format(arg1))
    print('arg2 was {}'.format(arg2))
  return new_func

my_func = return_a_func(2, 17)

print(my_func.__closure__ is not None)
print(len(my_func.__closure__) == 2)


# Get the values of the variables in the closure
closure_values = [
      my_func.__closure__[i].cell_contents for i in range(2)
]
print(closure_values == [2, 17])
def my_special_function():
  print('You are running my_special_function()')

def get_new_func(func):
  def call_func():
    func()
  return call_func

new_func = get_new_func(my_special_function)


# Redefine my_special_function() to just print "hello"
def my_special_function():
  print("hello")

new_func()

def my_special_function():
  print('You are running my_special_function()')

def get_new_func(func):
  def call_func():
    func()
  return call_func

new_func = get_new_func(my_special_function)


# Delete my_special_function()
del(my_special_function)

new_func()

def my_special_function():
  print('You are running my_special_function()')

def get_new_func(func):
  def call_func():
    func()
  return call_func


# Overwrite `my_special_function` with the new function
my_special_function = get_new_func(my_special_function)

my_special_function()

# edited/added
def print_args(func):
    sig = inspect.signature(func)
    def wrapper(*args, **kwargs):
        bound = sig.bind(*args, **kwargs).arguments
        str_args = ', '.join(['{}={}'.format(k, v) for k, v in bound.items()])
        print('{} was called with {}'.format(func.__name__, str_args))
        return func(*args, **kwargs)
    return wrapper

def my_function(a, b, c):
  print(a + b + c)


# Decorate my_function() with the print_args() decorator
my_function = print_args(my_function)

my_function(1, 2, 3)


# Decorate my_function() with the print_args() decorator
@print_args
def my_function(a, b, c):
  print(a + b + c)

my_function(1, 2, 3)
def print_before_and_after(func):
  def wrapper(*args):
    print('Before {}'.format(func.__name__))
    # Call the function being decorated with *args
    func(*args)
    print('After {}'.format(func.__name__))
  # Return the nested function
  return wrapper

@print_before_and_after
def multiply(a, b):
  print(a * b)

multiply(5, 10)
def print_return_type(func):
  # Define wrapper(), the decorated function
  def wrapper(*args, **kwargs):
    # Call the function being decorated
    result = func(*args, **kwargs)
    print('{}() returned type {}'.format(
          func.__name__, type(result)
    ))
    return result
  # Return the decorated function
  return wrapper

@print_return_type
def foo(value):
  return value

print(foo(42))
print(foo([1, 2, 3]))
print(foo({'a': 42}))
def counter(func):
  def wrapper(*args, **kwargs):
    wrapper.count += 1
    # Call the function being decorated and return the result
    return func(*args, **kwargs)
  wrapper.count = 0
  # Return the new decorated function
  return wrapper


# Decorate foo() with the counter() decorator
@counter
def foo():
  print('calling foo()')

foo()
foo()

print('foo() was called {} times.'.format(foo.count))
def add_hello(func):
  def wrapper(*args, **kwargs):
    print('Hello')
    return func(*args, **kwargs)
  return wrapper


# Decorate print_sum() with the add_hello() decorator
@add_hello
def print_sum(a, b):
  """Adds two numbers and prints the sum"""
  print(a + b)

print_sum(10, 20)
print_sum_docstring = print_sum.__doc__
print(print_sum_docstring)

def add_hello(func):
  # Add a docstring to wrapper
  def wrapper(*args, **kwargs):
    """Print 'hello' and then call the decorated function."""
    print('Hello')
    return func(*args, **kwargs)
  return wrapper

@add_hello
def print_sum(a, b):
  """Adds two numbers and prints the sum"""
  print(a + b)

print_sum(10, 20)
print_sum_docstring = print_sum.__doc__
print(print_sum_docstring)


# Import the function you need to fix the problem
from functools import wraps

def add_hello(func):
  def wrapper(*args, **kwargs):
    """Print 'hello' and then call the decorated function."""
    print('Hello')
    return func(*args, **kwargs)
  return wrapper

@add_hello
def print_sum(a, b):
  """Adds two numbers and prints the sum"""
  print(a + b)

print_sum(10, 20)
print_sum_docstring = print_sum.__doc__
print(print_sum_docstring)

from functools import wraps

def add_hello(func):
  # Decorate wrapper() so that it keeps func()'s metadata
  @wraps(func)
  def wrapper(*args, **kwargs):
    """Print 'hello' and then call the decorated function."""
    print('Hello')
    return func(*args, **kwargs)
  return wrapper

@add_hello
def print_sum(a, b):
  """Adds two numbers and prints the sum"""
  print(a + b)

print_sum(10, 20)
print_sum_docstring = print_sum.__doc__
print(print_sum_docstring)

# edited/added
def check_inputs(a, *args, **kwargs):
  for value in a:
    time.sleep(0.01)
  print('Finished checking inputs')
def check_outputs(a, *args, **kwargs):
  for value in a:
    time.sleep(0.01)
  print('Finished checking outputs')
def check_everything(func):
  @wraps(func)
  def wrapper(*args, **kwargs):
    check_inputs(*args, **kwargs)
    result = func(*args, **kwargs)
    check_outputs(result)
    return result
  return wrapper

@check_everything
def duplicate(my_list):
  """Return a new list that repeats the input twice"""
  return my_list + my_list

t_start = time.time()
duplicated_list = duplicate(list(range(50)))
t_end = time.time()
decorated_time = t_end - t_start

t_start = time.time()

# Call the original function instead of the decorated one
duplicated_list = duplicate.__wrapped__(list(range(50)))
t_end = time.time()
undecorated_time = t_end - t_start

print('Decorated time: {:.5f}s'.format(decorated_time))
print('Undecorated time: {:.5f}s'.format(undecorated_time))

# edited/added
def run_n_times(n):
  """Define and return a decorator"""
  def decorator(func):
    def wrapper(*args, **kwargs):
      for i in range(n):
        func(*args, **kwargs)
    return wrapper
  return decorator


# Make print_sum() run 10 times with the run_n_times() decorator
@run_n_times(10)
def print_sum(a, b):
  print(a + b)

print_sum(15, 20)


# Use run_n_times() to create the run_five_times() decorator
run_five_times = run_n_times(5)

@run_five_times
def print_sum(a, b):
  print(a + b)

print_sum(4, 100)


# Modify the print() function to always run 20 times
print = run_n_times(20)(print)

print('What is happening?!?!')
def html(open_tag, close_tag):
  def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
      msg = func(*args, **kwargs)
      return '{}{}{}'.format(open_tag, msg, close_tag)
    # Return the decorated function
    return wrapper
  # Return the decorator
  return decorator


# Make hello() return bolded text
@html('<b>', '</b>')
def hello(name):
  return 'Hello {}!'.format(name)

print(hello('Alice'))


# Make goodbye() return italicized text
@html('<i>', '</i>')
def goodbye(name):
  return 'Goodbye {}.'.format(name)

print(goodbye('Alice'))


# Wrap the result of hello_goodbye() in <div> and </div>
@html('<div>', '</div>')
def hello_goodbye(name):
  return '\n{}\n{}\n'.format(hello(name), goodbye(name))

print(hello_goodbye('Alice'))
def tag(*tags):
  # Define a new decorator, named "decorator", to return
  def decorator(func):
    # Ensure the decorated function keeps its metadata
    @wraps(func)
    def wrapper(*args, **kwargs):
      # Call the function being decorated and return the result
      return func(*args, **kwargs)
    wrapper.tags = tags
    return wrapper
  # Return the new decorator
  return decorator

@tag('test', 'this is a tag')
def foo():
  pass

print(foo.tags)
def returns_dict(func):
  # Complete the returns_dict() decorator
  def wrapper(*args, **kwargs):
    result = func(*args, **kwargs)
    assert type(result) == dict
    return result
  return wrapper

@returns_dict
def foo(value):
  return value

try:
  print(foo([1,2,3]))
except AssertionError:
  print('foo() did not return a dict!')

def returns(return_type):
  # Write a decorator that raises an AssertionError if the
  # decorated function returns a value that is not return_type
  def decorator(func):
    def wrapper(*args, **kwargs):
      result = func(*args, **kwargs)
      assert type(result) == return_type
      return result
    return wrapper
  return decorator

@returns(dict)
def foo(value):
  return value

try:
  print(foo([1,2,3]))
except AssertionError:
  print('foo() did not return a dict!')
