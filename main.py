import numpy as np
import skfuzzy as fuzz
import skfuzzy.membership as mf
import matplotlib.pyplot as plt

# Input values
driving_style = int(input("Input your av. energy consumption in Wh/km: "))
input_temperature = int(input("Input temperature: "))
input_battery_capacity = int(input("Input battery size: "))

x_range = np.arange(0, 640, 1)
x_temperature = np.arange(-10, 23, 1)
# Power in kWh of estimated remaining battery capacity per 100 km
x_estimation = np.arange(10, 24, 1)
x_battery = np.arange(16, 108, 1)
# Membership functions
# Weather
weather_cold = mf.trapmf(x_temperature, [-10, -5, 0, 1])
weather_mild = mf.trapmf(x_temperature, [0, 1, 23, 23])
# Batteries
batt_low = mf.trapmf(x_battery, [15, 16, 20, 25])
batt_medium = mf.trapmf(x_battery, [20, 25, 60, 65])
batt_medium_high = mf.trapmf(x_battery, [60, 65, 90, 95])
batt_high = mf.trapmf(x_battery, [90, 95, 108, 113])
# Driving modes in Wh/km
city_drive = mf.trapmf(x_estimation, [100, 110, 120, 130])
combined_drive = mf.trapmf(x_estimation, [120, 130, 170, 180])
highway_drive = mf.trapmf(x_estimation, [170, 180, 200, 230])
# Range output membership function
range_low = mf.trapmf(x_range, [90, 100, 135, 160])
range_medium = mf.trapmf(x_range, [380, 390, 470, 480])
range_high = mf.trapmf(x_range, [470, 480, 630, 640])

# Plots for better overview
fig, (ax0, ax1, ax2, ax3) = plt.subplots(nrows=4)
ax0.plot(x_temperature, weather_cold, 'r', linewidth=1, label="range1")
ax0.plot(x_temperature, weather_mild, 'g', linewidth=2, label="range1")

ax1.plot(x_battery, batt_low, 'r', linewidth=1, label="range1")
ax1.plot(x_battery, batt_medium, 'g', linewidth=2, label="range1")
ax1.plot(x_battery, batt_medium_high, 'c', linewidth=3, label="range1")
ax1.plot(x_battery, batt_high, 'b', linewidth=4, label="range1")

ax2.plot(x_estimation, city_drive, 'c', linewidth=4, label="range_temp")
ax2.plot(x_estimation, combined_drive, 'm', linewidth=4, label="range_temp")
ax2.plot(x_estimation, highway_drive, 'y', linewidth=4, label="range_temp")

ax3.plot(x_range, range_low, 'r', linewidth=1, label="range1")
ax3.plot(x_range, range_medium, 'c', linewidth=1, label="range1")
ax3.plot(x_range, range_high, 'b', linewidth=1, label="range1")

plt.show()

# Building up interpolated membership functions, returns membership function value at input_temperature
temperature_low = fuzz.interp_membership(x_temperature, weather_cold, input_temperature)
temperature_high = fuzz.interp_membership(x_temperature, weather_mild, input_temperature)
# Building up interpolated membership functions, returns membership function value at input_battery_capacity
batt_low = fuzz.interp_membership(x_battery, batt_low, input_battery_capacity)
batt_medium = fuzz.interp_membership(x_battery, batt_medium, input_battery_capacity)
batt_medium_high = fuzz.interp_membership(x_battery, batt_medium_high, input_battery_capacity)
batt_high = fuzz.interp_membership(x_battery, batt_high, input_battery_capacity)
# Building up interpolated membership functions, returns membership function value at driving_style
city_drive = fuzz.interp_membership(x_estimation, city_drive, driving_style)
combined_drive = fuzz.interp_membership(x_estimation, combined_drive, driving_style)
highway_drive = fuzz.interp_membership(x_estimation, highway_drive, driving_style)

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
# is called fuzzification. Also, we must define what we mean by "and" / "or" in the
# fuzzy rule. This is called fuzzy combination.

rule1 = np.fmin(np.fmin(np.fmin(batt_low, weather_cold), city_drive), range_high)
rule2 = np.fmin(np.fmin(np.fmin(batt_low, weather_cold), highway_drive), range_low)
rule3 = np.fmin(np.fmin(np.fmin(batt_low, weather_cold), combined_drive), range_medium)

rule4 = np.fmin(np.fmin(np.fmin(batt_low, weather_mild), city_drive), range_high)
rule5 = np.fmin(np.fmin(np.fmin(batt_low, weather_mild), highway_drive), range_low)
rule6 = np.fmin(np.fmin(np.fmin(batt_low, weather_mild), combined_drive), range_medium)

rule7 = np.fmin(np.fmin(np.fmin(batt_medium, weather_cold), city_drive), range_high)
rule8 = np.fmin(np.fmin(np.fmin(batt_medium, weather_cold), highway_drive), range_low)
rule9 = np.fmin(np.fmin(np.fmin(batt_medium, weather_cold), combined_drive), range_medium)

rule10 = np.fmin(np.fmin(np.fmin(batt_medium, weather_mild), city_drive), range_high)
rule11 = np.fmin(np.fmin(np.fmin(batt_medium, weather_mild), highway_drive), range_low)
rule12 = np.fmin(np.fmin(np.fmin(batt_medium, weather_mild), combined_drive), range_medium)

rule13 = np.fmin(np.fmin(np.fmin(batt_medium, weather_cold), city_drive), range_high)
rule14 = np.fmin(np.fmin(np.fmin(batt_medium, weather_cold), highway_drive), range_low)
rule15 = np.fmin(np.fmin(np.fmin(batt_medium, weather_cold), combined_drive), range_medium)

rule16 = np.fmin(np.fmin(np.fmin(batt_medium, weather_mild), city_drive), range_high)
rule17 = np.fmin(np.fmin(np.fmin(batt_medium, weather_mild), highway_drive), range_low)
rule18 = np.fmin(np.fmin(np.fmin(batt_medium, weather_mild), combined_drive), range_medium)

rule19 = np.fmin(np.fmin(np.fmin(batt_high, weather_cold), city_drive), range_high)
rule20 = np.fmin(np.fmin(np.fmin(batt_high, weather_cold), highway_drive), range_low)
rule21 = np.fmin(np.fmin(np.fmin(batt_high, weather_cold), combined_drive), range_medium)

rule22 = np.fmin(np.fmin(np.fmin(batt_high, weather_mild), city_drive), range_high)
rule23 = np.fmin(np.fmin(np.fmin(batt_high, weather_mild), highway_drive), range_low)
rule24 = np.fmin(np.fmin(np.fmin(batt_high, weather_mild), combined_drive), range_medium)

#Mamdani inference system

range_low_ = np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(rule2, rule5), rule8), rule11), rule14), rule17), rule20), rule23)
range_medium_ = np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(rule3, rule6), rule9), rule12), rule15), rule18), rule21), rule24)
range_high_ = np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(rule1, rule4), rule7), rule10), rule13), rule16), rule19), rule22)

range_ = np.fmax(np.fmax(range_low_, range_medium_), range_high_)

defuzzified = fuzz.defuzz(x_range, range_, "mom")


print("Range is:", defuzzified)

