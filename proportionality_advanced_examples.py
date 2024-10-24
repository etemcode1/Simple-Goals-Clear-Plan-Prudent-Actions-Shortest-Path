Here are seven advanced Python code examples focusing on **Proportionality**, showcasing various applications of proportional relationships and their profound utility in fields such as optimization, physics, and economics.

### Smart File Name:
`proportionality_advanced_examples.py`

---

### Example 1: **Direct Proportionality in Physics (Hooke's Law)**
This example demonstrates direct proportionality using Hooke's Law, where force is directly proportional to the extension of a spring.
```python
def hookes_law(spring_constant, extension):
    """Calculate force based on Hooke's law (F = k * x)."""
    return spring_constant * extension

# Example usage
k = 100  # Spring constant in N/m
x = 0.05  # Extension in meters
force = hookes_law(k, x)
print(f"Force: {force} N")
```

---

### Example 2: **Inverse Proportionality in Economics (Supply and Demand)**
This example explores inverse proportionality by modeling the relationship between supply and price in a basic economic system.
```python
def supply_demand(price, elasticity):
    """Inverse proportionality between price and supply."""
    return 1 / (price * elasticity)

# Example usage
price = 20  # Price per unit
elasticity = 0.5  # Elasticity coefficient
supply = supply_demand(price, elasticity)
print(f"Supply: {supply} units")
```

---

### Example 3: **Proportional Scaling in Image Processing**
This example performs proportional scaling of an image to maintain its aspect ratio during resizing.
```python
def proportional_scaling(original_width, original_height, target_width):
    """Scale height proportionally to the new width while maintaining aspect ratio."""
    scale_factor = target_width / original_width
    new_height = original_height * scale_factor
    return target_width, new_height

# Example usage
original_w, original_h = 1920, 1080
target_w = 1280
scaled_dimensions = proportional_scaling(original_w, original_h, target_w)
print(f"New dimensions: {scaled_dimensions[0]}x{scaled_dimensions[1]}")
```

---

### Example 4: **Proportional Distribution of Resources (Weighted Average)**
This example distributes resources proportionally based on the weights assigned to different categories, illustrating proportional allocation.
```python
def proportional_distribution(total_resources, weights):
    """Distribute resources proportionally based on given weights."""
    total_weight = sum(weights)
    distribution = [(weight / total_weight) * total_resources for weight in weights]
    return distribution

# Example usage
total_resources = 1000  # Total units of resources
weights = [0.2, 0.5, 0.3]  # Weights for each category
distribution = proportional_distribution(total_resources, weights)
print(f"Resource distribution: {distribution}")
```

---

### Example 5: **Proportionality in Optimization (Gradient Descent)**
This example uses proportionality to adjust the learning rate in gradient descent optimization for machine learning.
```python
def gradient_descent(learning_rate, gradient):
    """Update parameters using proportional adjustments in gradient descent."""
    update = learning_rate * gradient
    return update

# Example usage
learning_rate = 0.01
gradient = 0.2  # Gradient at the current step
parameter_update = gradient_descent(learning_rate, gradient)
print(f"Parameter update: {parameter_update}")
```

---

### Example 6: **Proportional Division in Voting Systems (D'Hondt Method)**
This example applies the D'Hondt method for proportional representation in voting, dividing seats based on the proportion of votes received.
```python
def dhondt_method(votes, num_seats):
    """Proportional allocation of seats using the D'Hondt method."""
    seats = [0] * len(votes)
    for _ in range(num_seats):
        quotients = [votes[i] / (seats[i] + 1) for i in range(len(votes))]
        winner = quotients.index(max(quotients))
        seats[winner] += 1
    return seats

# Example usage
votes = [30000, 20000, 15000]  # Votes for each party
num_seats = 10
seat_allocation = dhondt_method(votes, num_seats)
print(f"Seat allocation: {seat_allocation}")
```

---

### Example 7: **Proportional Control in PID Systems**
This example demonstrates proportional control in a PID controller, adjusting the control signal based on the proportional error.
```python
def proportional_control(setpoint, current_value, Kp):
    """Proportional control signal based on error."""
    error = setpoint - current_value
    control_signal = Kp * error
    return control_signal

# Example usage
setpoint = 100
current_value = 85
Kp = 0.5  # Proportional gain
control_signal = proportional_control(setpoint, current_value, Kp)
print(f"Control signal: {control_signal}")
```

---

These seven advanced Python examples cover different aspects of proportionality in various fields, from physics and economics to optimization and control systems. By leveraging proportional relationships, these techniques provide deep insights and practical applications, enhancing our understanding of natural laws, resource allocation, and system control.
