import numpy as np
import matplotlib.pyplot as plt
from pyscript import document, window

# Initialize attendance data
attendance = {
    'monday': 0,
    'tuesday': 0,
    'wednesday': 0,
    'thursday': 0,
    'friday': 0
}

days = list(attendance.keys())
positions = list(range(len(days)))
labels = [day.capitalize() for day in days]

def plot():
    """Update and plot the weekly attendance absences."""
    plt.clf()
    
    # Get input values from HTML
    day = document.getElementById("day").value.lower()
    num_absences = int(document.getElementById("num").value)
    
    # Update attendance data
    if day in attendance:
        attendance[day] = num_absences
    
    # Prepare data for plotting
    y = [attendance[d] for d in days]
    
    # Create plot
    plt.figure(figsize=(8, 5), dpi=100)
    plt.plot(positions, y, marker='o', color='#800000', linewidth=2, markersize=8)
    plt.fill_between(positions, y, alpha=0.3, color='#f4e4c4')
    
    plt.title("Weekly Attendance (Absences)", fontsize=16, fontweight='bold')
    plt.xlabel('Day of the Week', fontsize=12)
    plt.xticks(positions, labels, fontsize=10)
    plt.ylabel('Number of Absences', fontsize=12)
    plt.ylim(bottom=0)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    
    # Display the plot
    plt.show()

# Make plot function available to JavaScript
window.plot = plot