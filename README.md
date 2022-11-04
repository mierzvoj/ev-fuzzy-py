# ev-fuzzy-py

## Łukasz Cettler (s20168) oraz Wojciech Mierzejewski (s21617) - grupa 74C

<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About The Project](#about-the-project)
* [Features](#features)
* [Technologies Used](#technologies-used)

<!-- ABOUT THE PROJECT -->
## About The Project

Fuzzy logic originated with the theory of fuzzy sets introduced by mathematician Lotfi Zadeh in 1965. Fuzzy logic arises by assigning degrees of truth to propositions. The standard set of accuracy values (degrees) is in the range of [0,1] real units. Here 0 represents "completely false", 1
represents "totally true" and other values refer to partial truth (intermediate truth).

As an example of using fuzzy logic, we implemented a simple electric car range calculator. The calculator takes 3 input values, which are: average battery consumption per km, temperature and battery capacity.


## Features
Fuzzy Logic Implementation:

1. Created .xlsx file with Rule Base using Dataset taken from [Electric Vehicle Database](https://ev-database.org/#sort:path~type~order=.rank~number~desc|range-slider-range:prev~next=0~1200|range-slider-acceleration:prev~next=2~23|range-slider-topspeed:prev~next=110~350|range-slider-battery:prev~next=10~200|range-slider-towweight:prev~next=0~2500|range-slider-fastcharge:prev~next=0~1500|paging:currentPage=0|paging:number=9)
2. Created Membership Functions.
3. Fuzzification - We used skfuzzy library interpolation function for every linguistic qualifiers fuzzification.
4. To compute the output of Mamdani FIS given the inputs, one must go through six steps:
- determining a set of fuzzy rules
- fuzzifying the inputs using the input membership functions,
- combining the fuzzified inputs according to the fuzzy rules to establish a rule strength,
- finding the consequence of the rule by combining the rule strength and the output membership function,
- combining the consequences to get an output distribution,
- defuzzifying the output distribution (this step is only if a crisp output (class) is needed).
5. Defuzzification

## Technologies Used

* Python
* Skfuzzy - fuzzy logic toolbox for Python
* Matplotlib - a comprehensive library for creating static, animated, and interactive visualizations in Python
