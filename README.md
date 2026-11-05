
# A Low-Cost IoT System Development for Real-Time Residential Water Monitoring


**Journal:** IEEE Latin America Transactions

**Manuscript  ID :**  11019

**Authors:**
- Andrea Monserrath Fernández-Saldaña
- Alejandro Monroy-Avelino
- Pedro Miranda-Romagnoli
- Roberto Noriega-Papaqui

**Affiliation:** Autonomous University of the State of Hidalgo, Pachuca, Mexico


---


Abstract— Water, as a natural resource, faces increasing pres-
sure globally due to climate change, urbanization, and poor
management, highlighting the need for accessible technological
solutions for its monitoring. In this paper, we present the design
of a low-cost IoT system for real-time monitoring of water
consumption and level in residential environments (applicable
to infrastructure in Mexico). The IoT system integrates a Hall-
effect-based sensor for flow measurement, a level sensor based
on a pressure difference, derived from a technology transfer, and
a data acquisition and cloud communication unit. Additionally,
a user interface was developed to enable real-time data visual-
ization. The experimental results demonstrate the viability of the
proposed solution as a scalable, low-cost alternative for smart
water monitoring in urban environments.

<img width="1328" height="531" alt="v-abstract" src="https://github.com/user-attachments/assets/e9292bb0-5c3a-408a-9e19-3bb900858f4b" />

## Overview

This repository contains the code, figures and explanations for the low-cost monitoring system of water level and flow in residential applications.

Repository contents:

***Code:*** The firmware necessary to operate the electronics. It also contains a Readme.md with information about Hardware, System operation, Software architecture and Main required Libraries in order to facilitates reproduction. The name of the developed code for the ESP32 is:

- Monitor_WL_WC-v0.6.9.ino

The Code folder also includes the Blynk configuration. On the other hand, the app interface was developed in the Blink platform, which is interactive and does not generate a code file.
  
***Data:*** Because the original data files are very large, we cannot publish them here; instead, we provide CSV files with the processed data —corresponding to daily consumption, cumulative consumption, and water levels for the three residences.

***Diagram:*** It includes the electronic diagram, which is useful for reproducing the hardware.

***Figures_app:*** Here are the screenshots of the mobile app.



---

**Installation**

*Dependecies:*

- BlynkEdgent

- LiquidCrystal_I2C

- TimeLib

- WidgtetRTC

- Preferences

*Installation:*

The first step is to install the libraries through Arduino IDE Library Manager before compiling. The second step is to compile the Monitor_WL_WC-v0.6.9.ino, located in the Code folder. The third step is to download the compiled file into the ESP32.

For a more detailed information, useful for reproduction, see the Readme.md in the Code folder.







