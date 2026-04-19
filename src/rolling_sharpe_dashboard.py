import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from matplotlib.widgets import RadioButtons, CheckButtons
import datetime

# --- Parameters ---
N_STOCKS = 20
WINDOW = 50
DAYS = 500
np.random.seed(42)

# --- Simulate price data ---
dates = pd.date_range(end=datetime.date.today(), periods=DAYS)
stocks = [f"Stock_{i+1}" for i in range(N_STOCKS)]

# Simulate log returns, then prices
log_returns = np.random.normal(loc=0.0005, scale=0.02, size=(DAYS, N_STOCKS))
prices = 100 * np.exp(np.cumsum(log_returns, axis=0))
prices_df = pd.DataFrame(prices, index=dates, columns=stocks)

# --- Compute daily returns ---
returns = prices_df.pct_change().fillna(0)

# --- Rolling Sharpe Ratio ---
def rolling_sharpe(df, window):
    mean = df.rolling(window).mean()
    std = df.rolling(window).std()
    sharpe = mean / std
    return sharpe

sharpe_df = rolling_sharpe(returns, WINDOW)

# --- Visualization ---
def plot_rolling_sharpe_animated(sharpe_df, highlight_stock, smoothing, ax, lines, legend, frame):
    colors = list(mcolors.TABLEAU_COLORS.values()) + list(mcolors.CSS4_COLORS.values())
    pastel_colors = [c for c in colors if 'light' in c or 'pale' in c or 'lavender' in c or 'powder' in c or 'misty' in c or 'honeydew' in c or 'beige' in c or 'mint' in c or 'azure' in c or 'alice' in c or 'linen' in c or 'seashell' in c or 'snow' in c or 'lemon' in c or 'peach' in c or 'blanched' in c or 'moccasin' in c or 'wheat' in c or 'cornsilk' in c or 'oldlace' in c or 'ivory' in c or 'floral' in c or 'gainsboro' in c or 'thistle' in c or 'plum' in c or 'pink' in c or 'bisque' in c or 'misty' in c]
    if len(pastel_colors) < len(sharpe_df.columns):
        pastel_colors = colors[:len(sharpe_df.columns)]
    for i, stock in enumerate(sharpe_df.columns):
        data = sharpe_df[stock]
        if smoothing:
            data = data.rolling(10, min_periods=1).mean()
        if stock == highlight_stock:
            lines[i].set_data(sharpe_df.index[:frame], data.values[:frame])
            lines[i].set_color('navy')
            lines[i].set_linewidth(2.5)
            lines[i].set_alpha(0.9)
            lines[i].set_zorder(3)
        else:
            lines[i].set_data(sharpe_df.index[:frame], data.values[:frame])
            lines[i].set_color(pastel_colors[i % len(pastel_colors)])
            lines[i].set_linewidth(1)
            lines[i].set_alpha(0.5)
            lines[i].set_zorder(2)
    ax.set_xlim(sharpe_df.index[0], sharpe_df.index[-1])
    ax.set_ylim(np.nanmin(sharpe_df.values), np.nanmax(sharpe_df.values))
    ax.set_title("50-Day Rolling Sharpe Ratio", fontsize=18, weight='bold')
    ax.set_xlabel("Date", fontsize=14)
    ax.set_ylabel("Rolling Sharpe", fontsize=14)
    ax.set_facecolor('#f7f7fa')
    if legend:
        legend.remove()
    legend = ax.legend(loc='center left', bbox_to_anchor=(1, 0.5), title='Stocks', fontsize=10, title_fontsize=12, frameon=False)
    return legend

# --- Interactive Dashboard ---
def interactive_dashboard():
    import matplotlib.pyplot as plt
    from matplotlib.widgets import RadioButtons, CheckButtons
    from matplotlib.animation import FuncAnimation

    plt.style.use('seaborn-v0_8-whitegrid')
    highlight_stock = sharpe_df.columns[0]
    smoothing = [False]
    frame = [WINDOW]

    fig, ax = plt.subplots(figsize=(14, 7))
    plt.subplots_adjust(left=0.2, right=0.75)
    lines = []
    for _ in sharpe_df.columns:
        line, = ax.plot([], [], lw=1)
        lines.append(line)
    legend = None

    def animate(f):
        nonlocal legend
        legend = plot_rolling_sharpe_animated(sharpe_df, highlight_stock, smoothing[0], ax, lines, legend, f)
        return lines

    ani = FuncAnimation(fig, animate, frames=range(WINDOW, len(sharpe_df)), interval=30, blit=False, repeat=True)

    # Radio for highlight
    rax = plt.axes([0.78, 0.5, 0.18, 0.4], facecolor='#f7f7fa')
    radio = RadioButtons(rax, sharpe_df.columns, active=0)
    def on_radio(label):
        nonlocal highlight_stock
        highlight_stock = label
    radio.on_clicked(on_radio)

    # Checkbox for smoothing
    cax = plt.axes([0.78, 0.4, 0.18, 0.08], facecolor='#f7f7fa')
    check = CheckButtons(cax, ['Smoothing'], [False])
    def on_check(label):
        smoothing[0] = check.get_status()[0]
    check.on_clicked(on_check)

    plt.show()

if __name__ == "__main__":
    interactive_dashboard()
