# Import required libraries
import tkinter as tk
from tkinter import messagebox

# Global variable for water tracking
total_water = 0

# Function to calculate BMI
def calculate_bmi():
    try:
        # Get input (lbs and inches)
        weight_lb = float(weight_entry.get())
        height_in = float(height_entry.get())

        # Convert to metric
        weight_kg = weight_lb * 0.453592
        height_m = height_in * 0.0254

        # Calculate BMI
        bmi = weight_kg / (height_m ** 2)

        # Determine category
        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 25:
            category = "Normal"
        elif bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"

        # Display result
        bmi_result_label.config(text=f"BMI: {bmi:.2f} ({category})")

    except:
        messagebox.showerror("Error", "Please enter valid numbers")

# Function to track water intake
def add_water():
    try:
        global total_water

        # Get water input
        water = float(water_entry.get())

        # Add to total
        total_water += water

        # Display updated total
        water_result_label.config(text=f"Total Water Intake: {total_water} oz")

    except:
        messagebox.showerror("Error", "Enter a valid number")

# Function to calculate calories
def calculate_calories():
    try:
        # Get inputs
        age = int(age_entry.get())
        weight_lb = float(weight_entry.get())
        height_in = float(height_entry.get())

        # Convert to metric
        weight_kg = weight_lb * 0.453592
        height_cm = height_in * 2.54

        # Mifflin-St Jeor Equation (male version)
        calories = 10 * weight_kg + 6.25 * height_cm - 5 * age + 5

        # Display result
        calorie_result_label.config(
            text=f"Estimated Calories: {calories:.0f} kcal/day"
        )

    except:
        messagebox.showerror("Error", "Enter valid inputs")

# Function to reset all fields
def reset_fields():
    global total_water

    # Clear all entries
    weight_entry.delete(0, tk.END)
    height_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    water_entry.delete(0, tk.END)

    # Reset water total
    total_water = 0

    # Clear labels
    bmi_result_label.config(text="")
    calorie_result_label.config(text="")
    water_result_label.config(text="Total Water Intake: 0 oz")

# Create main window
root = tk.Tk()
root.title("Health Tracker App")
root.geometry("420x550")

# Title
title_label = tk.Label(root, text="Health Tracker", font=("Arial", 16))
title_label.pack(pady=10)

# BMI Frame
bmi_frame = tk.Frame(root, bd=2, relief="groove", padx=10, pady=10)
bmi_frame.pack(pady=10, fill="x", padx=10)

tk.Label(bmi_frame, text="BMI Calculator", font=("Arial", 12)).pack()

tk.Label(bmi_frame, text="Weight (lbs):").pack()
weight_entry = tk.Entry(bmi_frame)
weight_entry.pack()

tk.Label(bmi_frame, text="Height (inches):").pack()
height_entry = tk.Entry(bmi_frame)
height_entry.pack()

tk.Button(bmi_frame, text="Calculate BMI", command=calculate_bmi).pack(pady=5)

bmi_result_label = tk.Label(bmi_frame, text="")
bmi_result_label.pack()

# Water Tracker Frame
water_frame = tk.Frame(root, bd=2, relief="groove", padx=10, pady=10)
water_frame.pack(pady=10, fill="x", padx=10)

tk.Label(water_frame, text="Water Intake Tracker", font=("Arial", 12)).pack()

tk.Label(water_frame, text="Water (oz):").pack()
water_entry = tk.Entry(water_frame)
water_entry.pack()

tk.Button(water_frame, text="Add Water", command=add_water).pack(pady=5)

water_result_label = tk.Label(water_frame, text="Total Water Intake: 0 oz")
water_result_label.pack()

# Calorie Estimator Frame
calorie_frame = tk.Frame(root, bd=2, relief="groove", padx=10, pady=10)
calorie_frame.pack(pady=10, fill="x", padx=10)

tk.Label(calorie_frame, text="Calorie Estimator", font=("Arial", 12)).pack()

tk.Label(calorie_frame, text="Age:").pack()
age_entry = tk.Entry(calorie_frame)
age_entry.pack()

tk.Button(calorie_frame, text="Estimate Calories", command=calculate_calories).pack(pady=5)

calorie_result_label = tk.Label(calorie_frame, text="")
calorie_result_label.pack()

# Reset Button
tk.Button(root, text="Reset All", command=reset_fields, bg="lightgray").pack(pady=15)

# Run application
root.mainloop()