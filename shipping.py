weight = 4.8
cost_ground_premium = 125

# Ground Shipping

if weight < 2:
  cost_ground = float(1.5) * weight
elif weight > 2 and weight <= 6:
  cost_ground = 3 * weight + 20
elif weight > 6 and weight <= 10:
  cost_ground = 4 * weight + 20
elif weight > 10:
  cost_ground = 4.75 * weight + 20
else:
  print("Error")

# Drone Shipping

if weight < 2:
  cost_drone = 4.5 * weight
elif weight > 2 and weight <= 6:
  cost_drone = 9 * weight
elif weight > 6 and weight <= 10:
  cost_drone = 12 * weight
elif weight > 10:
  cost_drone = 14.25 * weight
else:
  print("Error")

print("Ground Shipping: $", cost_ground)
print("Ground Premium Shipping: $", cost_ground_premium)
print("Drone Shipping: $", round(cost_drone,2))



