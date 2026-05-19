# Hotel Booking Data Analysis 🏨

This project performs an **Exploratory Data Analysis (EDA)** on a hotel booking dataset to uncover key factors that govern bookings, cancellations, and revenue. Using Python's data science libraries, we visualize trends and provide actionable insights to help hotel management optimize occupancy and reduce churn.

---

## 📊 Project Overview

The primary goal of this analysis is to understand customer behavior and identify patterns that lead to cancellations. By analyzing variables like lead time, deposit types, and market segments, this project aims to suggest data-driven strategies for hotel operations.

### Key Objectives:
*   **Hotel Comparison:** Analyze the booking ratios between City Hotels and Resort Hotels.
*   **Cancellation Drivers:** Identify the overall cancellation rate and the primary factors influencing it.
*   **Seasonality:** Visualize monthly and seasonal trends in booking volumes.
*   **Lead Time Impact:** Examine the relationship between how far in advance a room is booked (lead time) and its likelihood of being canceled.
*   **Demographics & Segments:** Map the distribution of guests by country of origin and market segment.

---

## 🛠️ Tech Stack

*   **Language:** Python
*   **Libraries:**
    *   **Pandas:** Data manipulation, cleaning, and profiling.
    *   **NumPy:** Efficient numerical operations.
    *   **Matplotlib:** Base visualization layer.
    *   **Seaborn:** Advanced statistical visualizations, heatmaps, and categorical plots.

---

## 📂 Dataset Description

The analysis covers a variety of operational and customer metrics within the dataset:
*   **Booking Data:** Arrival dates, length of stay, number of adults/children/babies, and room type tracking.
*   **Customer Profiles:** Country of origin, customer type (e.g., Transient, Contract, Group).
*   **Reservation Details:** Deposit types, market segments, ADR (Average Daily Rate), and final reservation status.

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone [https://github.com/YOUR_USERNAME/Data-Analytics-projects.git](https://github.com/YOUR_USERNAME/Data-Analytics-projects.git)
cd Data-Analytics-projects

2. Install Dependencies
Make sure you have Python installed, then run the following command to install the required libraries:

Bash
pip install pandas numpy matplotlib seaborn
3. Run the Analysis
Launch the Jupyter Notebook environment to explore the step-by-step code execution:

Bash
jupyter notebook hotel_analysis.ipynb
📈 Key Insights
[!TIP]
Summary of Typical Findings:

Cancellations: Approximately 37% of bookings are canceled. Interestingly, groups with "No Deposit" configurations often exhibit higher volatile behavior.

Seasonality: Peak booking volumes consistently hit their highs during July and August, while cancellation anomalies tend to spike during seasonal transitions.

Pricing Dynamics: Resort hotels command a significantly higher Average Daily Rate (ADR) during summer months, whereas City hotels maintain a steadier, more uniform pricing structure year-round.

🖼️ Visualizations Included
The notebook generates several core plots to tell the data's story:

Correlation Heatmaps: To quickly pinpoint relations between variables like lead time and cancellations.

Bar & Donut Charts: To break down categorical shares (e.g., City vs. Resort splits, cancellation distributions).

Line Plots: To map out dynamic monthly price (ADR) fluctuations over the calendar year.

📄 License
This project is licensed under the MIT License - see the LICENSE file for details.
