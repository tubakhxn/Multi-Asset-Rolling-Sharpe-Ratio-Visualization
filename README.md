## dev/creator = tubakhxn

# Multi-Asset Rolling Sharpe Ratio Visualization

## Project Overview
This project visualizes the 50-day rolling Sharpe ratio for multiple simulated stocks. It provides an animated, interactive dashboard where you can:
- View the rolling Sharpe ratio for 15–25 stocks on a single chart
- Highlight any stock of your choice
- Apply smoothing to the lines for clarity
- Enjoy a clean, financial dashboard-style visualization

The Sharpe ratio is a measure of risk-adjusted return, calculated as the rolling mean of returns divided by the rolling standard deviation.

## How to Fork and Run
1. **Fork this repository** using the GitHub interface (click the "Fork" button at the top right of the repo page).
2. **Clone your fork** to your local machine:
   ```sh
   git clone https://github.com/YOUR_USERNAME/REPO_NAME.git
   ```
3. **Navigate to the project directory**:
   ```sh
   cd REPO_NAME
   ```
4. **(Optional) Create a virtual environment**:
   ```sh
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```
5. **Install dependencies**:
   ```sh
   pip install -r requirements.txt
   ```
6. **Run the dashboard**:
   ```sh
   python src/rolling_sharpe_dashboard.py
   ```

## Relevant Wikipedia Links
- [Sharpe Ratio](https://en.wikipedia.org/wiki/Sharpe_ratio)
- [Rolling Window Analysis](https://en.wikipedia.org/wiki/Moving_average)
- [Stock Market](https://en.wikipedia.org/wiki/Stock_market)
- [Python (programming language)](https://en.wikipedia.org/wiki/Python_(programming_language))
- [Matplotlib](https://en.wikipedia.org/wiki/Matplotlib)
- [Pandas (software)](https://en.wikipedia.org/wiki/Pandas_(software))

---
For any questions or contributions, please open an issue or pull request.
