# 🚧 Production Line Bottleneck Analyzer

A Python script that simulates a simple **sequential production line** to identify its **bottleneck** (slowest step) and measure the **impact of improvements**. This project demonstrates key concepts from the **Theory of Constraints (TOC)** using practical and quantifiable simulations.

---

## 📈 How It Works

The script models a production line with a series of steps, each having a specific processing time:

1. **Identifies the Bottleneck**  
   Finds the step that takes the longest time per unit (which limits overall throughput).

2. **Simulates Production**  
   Calculates the total time and throughput for a given number of units.

3. **Applies Improvement**  
   Improves the bottleneck step (e.g., by reducing its processing time by 50%).

4. **Quantifies Impact**  
   Shows throughput increase and total time reduction after improvement.

---

## 🖥️ How to Run

1. Save the script as `production_line_bottleneck_analyzer.py`.

2. Open your terminal and navigate to the file location.

3. Run the script:

   ```bash
   python production_line_bottleneck_analyzer.py
