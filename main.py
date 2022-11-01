import numpy as np
import skfuzzy as fuzz
import skfuzzy.membership as mf
import matplotlib.pyplot as plt

# Input values
input_passengers = int(input("Input number of passengers: "))
input_temperature = int(input("Input temperature: "))
input_battery_capacity = int(input("Input battery size: "))

x_range = np.arange(0, 380, 1)
x_temperature = np.arange(-30, 50, 1)

# Tesla model 4 batteries types
# Batteries in kWh
batt_capacity_low = int(54)
batt_capacity_medium = int(62)
batt_capacity_medium_higher = int(75)
batt_capacity_high = int(82)
# Memebership functions
# Batteries
range_long_min = mf.trapmf(x_range, [0, 0, 320, 328])
range_long_med = mf.trapmf(x_range, [0, 0, 330, 338])
range_long_med_high = mf.trapmf(x_range, [0, 0, 340, 348])
range_long_max = mf.trapmf(x_range, [0, 0, 350, 358])
# Ranges in route mode
range_city = mf.trapmf(x_range, [0, 0, 250, 320])
range_highway = mf.trapmf(x_range, [0, 0, 350, 358])
# Ranges vs temp
range_temp_lower_than_min10 = mf.trapmf(x_range, [0, 200, 200, 200])
range_temp_min10_0 = mf.trapmf(x_range, [0, 250, 250, 250])
range_temp_0_10 = mf.trapmf(x_range, [0, 350, 350, 350])
# Range combined with passengers number
range_passengers_two = mf.trapmf(x_range, [0, 350, 358, 358])
range_passengers_four = mf.trapmf(x_range, [0, 350, 350, 350])

# Ranges low, mid, long, output membership function
range_low = mf.trapmf(x_range, [100, 150, 200, 250])
range_mid = mf.trapmf(x_range, [200, 250, 300, 350])
range_long = mf.trapmf(x_range, [300, 350, 380, 400])


# Plots for better overview
fig, (ax0, ax1, ax2, ax3, ax4) = plt.subplots(nrows=5)
ax0.plot(x_range, range_long_min, 'r', linewidth=2, label="range1")
ax0.plot(x_range, range_long_med, 'g', linewidth=2, label="range1")
ax0.plot(x_range, range_long_med_high, 'b', linewidth=2, label="range1")
ax0.plot(x_range, range_long_max, 'y', linewidth=2, label="range1")

ax1.plot(x_range, range_city, 'r', linewidth=2, label="range1")
ax1.plot(x_range, range_highway, 'g', linewidth=2, label="range1")

ax2.plot(x_range, range_temp_lower_than_min10, 'c', linewidth=4, label="range_temp")
ax2.plot(x_range, range_temp_min10_0, 'm', linewidth=4, label="range_temp")
ax2.plot(x_range, range_temp_0_10, 'y', linewidth=4, label="range_temp")

ax3.plot(x_range, range_passengers_two, 'y', linewidth=4, label="range_pass_2")
ax3.plot(x_range, range_passengers_four, 'y', linewidth=4, label="range_pass_4")
ax4.plot(x_range, range_low, 'r', linewidth=4)
ax4.plot(x_range, range_mid, 'r', linewidth=4)
ax4.plot(x_range, range_long, 'r', linewidth=4)
plt.show()

# Building up interpolated membership functions, returns membership function value at input_passengers
range_pass_two = fuzz.interp_membership(x_range, range_passengers_two, input_passengers)
range_pass_four = fuzz.interp_membership(x_range, range_passengers_four, input_passengers)
# returns membership function value at input_temperature
range_temp_low = fuzz.interp_membership(x_range, range_temp_lower_than_min10, input_temperature)
range_temp_med = fuzz.interp_membership(x_range, range_temp_min10_0, input_temperature)
range_temp_high = fuzz.interp_membership(x_range, range_temp_0_10, input_temperature)
# returns membership function value at input_battery_capacity
range_batt_small = fuzz.interp_membership(x_range, range_long_min, input_battery_capacity)
range_batt_med = fuzz.interp_membership(x_range, range_long_med, input_battery_capacity)
range_batt_med_high = fuzz.interp_membership(x_range, range_long_med_high, input_battery_capacity)
range_batt_high = fuzz.interp_membership(x_range, range_long_max, input_battery_capacity)

# Creating fuzzy rules
# Fuzzy rules are a collection of linguistic statements that describe how the FIS (Fuzzy Inference System)
# should make a decision regarding
# classifying an input or controlling an output. Fuzzy rules are always written in the following form:
# if (input1 is membership function1) and/or (input2 is membership function2) and/or. then (output n is output
# membership function n).
# For example, one could make up a rule that says:
# if temperature is high and humidity is high then room is hot.
# There would have to be membership functions that define what we mean by high temperature
# (input1), high humidity (input2) and a hot room (output1). This process of taking an input such as
# temperature and processing it through a membership function to determine what we mean by "high" temperature
# is called fuzzification and is discussed in section 4.1.2. Also, we must define what we mean by "and" / "or" in the
# fuzzy rule. This is called fuzzy combination and is discussed in section 4.1.3.

rule1 = np.fmin(np.fmin(range_pass_four, range_temp_low), range_low)
