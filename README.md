# Annual electricity production
![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-0.24.2-orange?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-3.4.2-%23ffffff?style=for-the-badge&logo=matplotlib)
![Streamlit](https://img.shields.io/badge/Streamlit-1.12.0-ff4b4b?style=for-the-badge&logo=streamlit&logoColor=white)

This is a small project that aims to analyze a dataset related to electricity production. Why this dataset? Because it is an increasingly present subject today and it is important to explore this data a little in order to see the efficiency of our deployed means of electricity production in France.

## Features
- **Year:** The year the electricity was produced.
- **Region name:** The region where the electricity was produced.
- **Voltage domain:** Corresponds to the classification of electrical installations.
- **Number of wind, photovoltaic, hydraulic, bio-energy, cogeneration and other sites:** The number of electricity production installations per department.
- **Energy produced:** The total energy produced according to the different installations.


## Installation Guide

1. **Clone the Repository**
   
   Begin by cloning the project to your local machine:
   ```bash
   git clone https://github.com/Theooo91/Annual-electricity-production.git
   ```

2. **Access Project Directory**

   Change to the project's root directory:
   ```bash
   cd Annual-electricity-production
   ```


## Running the Project

1. **Before you begin, you will need to install a virtual environment**

   ```bash
   python -m venv venv
   ```
   
2. **Launch the virtual environment**

   ```bash
   .\venv\Scripts\activate
   ```

3. **Launch the Streamlit app**

   ```bash
   streamlit run app.py
   ```
