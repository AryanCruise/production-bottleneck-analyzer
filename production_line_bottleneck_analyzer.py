# production_line_bottleneck_analyzer.py

import time

production_steps = {
    "Raw Material Prep": 5,
    "Assembly Line 1": 8,      # Takes 8 minutes per unit (potential bottleneck)
    "Quality Check": 6,        
    "Packaging": 4            
}

num_units_to_produce = 20

# --- Simulation Logic ---

def simulate_production(steps_data, units):
    print(f"\n--- Simulating Production for {units} Units ---")
    print("Initial Step Capacities (minutes per unit):")
    for step, time_per_unit in steps_data.items():
        print(f"  - {step}: {time_per_unit} minutes")

    # To calculate the total time for 'units' items, the bottleneck determines the pace.
    # The slowest step (highest time per unit) will dictate the overall production rate.
    bottleneck_time_per_unit = 0
    bottleneck_step = ""

    # Find the bottleneck (the step that takes the longest per unit)
    for step, time_per_unit in steps_data.items():
        if time_per_unit > bottleneck_time_per_unit:
            bottleneck_time_per_unit = time_per_unit
            bottleneck_step = step

    total_production_time_minutes = units * bottleneck_time_per_unit
    throughput_per_hour = (units / total_production_time_minutes) * 60 if total_production_time_minutes > 0 else 0

    print(f"\nIdentified Bottleneck: '{bottleneck_step}' (takes {bottleneck_time_per_unit} minutes per unit)")
    print(f"Total estimated time to produce {units} units: {total_production_time_minutes:.2f} minutes")
    print(f"Estimated Throughput: {throughput_per_hour:.2f} units per hour")

    return total_production_time_minutes, throughput_per_hour, bottleneck_step

def improve_bottleneck(steps_data, bottleneck_step, improvement_factor=0.5):
    new_steps_data = steps_data.copy()
    original_time = new_steps_data[bottleneck_step]
    new_time = original_time * (1 - improvement_factor)
    new_steps_data[bottleneck_step] = max(1, round(new_time, 2)) # Ensure time doesn't go below 1 minute

    print(f"\n--- Applying Improvement ---")
    print(f"Improving '{bottleneck_step}' from {original_time} to {new_steps_data[bottleneck_step]} minutes per unit (by {improvement_factor*100:.0f}%)")
    return new_steps_data

# --- Main Execution ---
if __name__ == "__main__":
    print("Welcome to the Production Line Bottleneck Analyzer!")

    # --- Initial Simulation ---
    initial_time, initial_throughput, identified_bottleneck = simulate_production(production_steps, num_units_to_produce)

    # --- Apply Improvement and Re-simulate ---
    if identified_bottleneck:
        # Simulate a 50% improvement on the bottleneck
        improved_steps = improve_bottleneck(production_steps, identified_bottleneck, improvement_factor=0.5)

        # Re-run simulation with improved steps
        final_time, final_throughput, _ = simulate_production(improved_steps, num_units_to_produce)

        # --- Quantify Impact ---
        if initial_throughput > 0:
            throughput_increase_percent = ((final_throughput - initial_throughput) / initial_throughput) * 100
            time_reduction_percent = ((initial_time - final_time) / initial_time) * 100
            print("\n--- Impact Analysis ---")
            print(f"Original Throughput: {initial_throughput:.2f} units/hour")
            print(f"New Throughput: {final_throughput:.2f} units/hour")
            print(f"Throughput Increase: {throughput_increase_percent:.2f}%")
            print(f"Total Production Time Reduction: {time_reduction_percent:.2f}%")
        else:
            print("\nCannot calculate percentage increase as initial throughput was zero.")
    else:
        print("\nNo bottleneck identified for improvement.")

    print("\nThank you for using the Production Line Bottleneck Analyzer!")
