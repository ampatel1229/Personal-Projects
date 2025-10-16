class PitStopCalculator:
  def __init__(self, tire_wear_factor=1, fuel_consumption=2.5):
      self.tire_wear_factor = tire_wear_factor
      self.fuel_consumption = fuel_consumption

  def calculate_pit_stop(self, laps, initial_tire_condition, initial_fuel_level):
      total_laps = laps
      current_laps = 0
      current_tire_condition = initial_tire_condition
      current_fuel_level = initial_fuel_level

      while current_laps < total_laps:
          current_laps += 1
          current_tire_condition -= self.tire_wear_factor
          current_fuel_level -= self.fuel_consumption

          if current_tire_condition <= 0:
              # Need a pit stop due to tire wear
              return current_laps, "Tire Wear"

          if current_fuel_level <= 0:
              # Need a pit stop due to low fuel
              return current_laps, "Low Fuel"

      # No pit stop needed
      return total_laps, "No Pit Stop Needed"


def main():
  # Get user input
  total_laps = int(input("Enter the total number of laps: "))
  initial_tire_condition = int(input("Enter the initial tire condition (100 for new tires): "))
  initial_fuel_level = float(input("Enter the initial fuel level (in liters): "))

  # Create PitStopCalculator instance
  pit_stop_calculator = PitStopCalculator()

  # Calculate pit stop strategy
  laps_until_pit, pit_reason = pit_stop_calculator.calculate_pit_stop(total_laps, initial_tire_condition,
                                                                     initial_fuel_level)

  # Display results
  if pit_reason == "No Pit Stop Needed":
      print(f"No pit stop needed. Complete the race in {total_laps} laps.")
  else:
      print(f"Pit stop needed after {laps_until_pit} laps due to {pit_reason}.")


if __name__ == "__main__":
  main()
