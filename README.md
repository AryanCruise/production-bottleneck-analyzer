Production Line Bottleneck Analyzer
This Python script simulates a simple sequential production line to identify its slowest step (the bottleneck) and quantifies the impact of improving that bottleneck on overall efficiency. It's a practical demonstration of concepts from the Theory of Constraints (TOC).

How it Works
The script defines a series of production steps, each with a specific time required per unit. It then:

Identifies the Bottleneck: Finds the step that takes the longest time per unit, which dictates the overall production rate.

Simulates Production: Calculates the total time and throughput for a given number of units based on the bottleneck.

Applies Improvement: Simulates an improvement (e.g., a 50% reduction in time) to the identified bottleneck.

Quantifies Impact: Shows the percentage increase in throughput and reduction in total production time after the improvement.

How to Run
Save the code: Save the provided Python code as production_line_bottleneck_analyzer.py.

Open a terminal or command prompt.

Navigate to the directory where you saved the file.

Run the script:

python production_line_bottleneck_analyzer.py

You can modify the production_steps dictionary and num_units_to_produce variable within the script to explore different scenarios.

What it Demonstrates
Operational Analysis: Understanding and modeling sequential processes.

Theory of Constraints (TOC): Identifying and focusing on the single limiting factor for systemic improvement.

Quantifiable Impact: Measuring the tangible benefits of targeted interventions.

Python for Problem-Solving: Using Python for data simulation, analysis, and deriving actionable insights.

Example Output (after running the script)
--- Simulating Production for 20 Units ---
Initial Step Capacities (minutes per unit):
  - Raw Material Prep: 5 minutes
  - Assembly Line 1: 8 minutes
  - Quality Check: 6 minutes
  - Packaging: 4 minutes

Identified Bottleneck: 'Assembly Line 1' (takes 8 minutes per unit)
Total estimated time to produce 20 units: 160.00 minutes
Estimated Throughput: 7.50 units per hour

--- Applying Improvement ---
Improving 'Assembly Line 1' from 8 to 4.0 minutes per unit (by 50%)

--- Simulating Production for 20 Units ---
Initial Step Capacities (minutes per unit):
  - Raw Material Prep: 5 minutes
  - Assembly Line 1: 4.0 minutes
  - Quality Check: 6 minutes
  - Packaging: 4 minutes

Identified Bottleneck: 'Quality Check' (takes 6 minutes per unit)
Total estimated time to produce 20 units: 120.00 minutes
Estimated Throughput: 10.00 units per hour

--- Impact Analysis ---
Original Throughput: 7.50 units/hour
New Throughput: 10.00 units/hour
Throughput Increase: 33.33%
Total Production Time Reduction: 25.00%

Future Enhancements (Optional)
Add a simple command-line interface (CLI) for user input.

Integrate a plotting library (e.g., Matplotlib, Plotly) to visualize throughput changes or bottleneck shifts.

Allow for more complex production line structures (e.g., parallel steps, branching paths).

Implement cost analysis to show financial impact of improvements.
