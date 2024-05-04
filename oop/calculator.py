class Calculator:

  @staticmethod
  def add(x, y):
    return x + y

  @staticmethod
  def subtract(x, y):
    return x - y


print(Calculator.add(5, 10))
print(Calculator.subtract(15, 10))

# In Python, a static method is a method that belongs to a class but does not operate on instance-level data. It does not receive instance data as the first argument (usually self in Python). Static methods are used when a method does not need to access instance attributes or methods.

# In the above example, the add and subtract methods in the Calculator class are defined as static methods using the @staticmethod decorator.

# These methods do not rely on any instance-specific data and can be called directly on the class without creating an instance of the class.
