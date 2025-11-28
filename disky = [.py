import matplotlib.pyplot as plt

# Data o cenách disků
typy = ["SSD 512GB", "SSD 1TB", "SSD 1TB NVMe",
        "HDD 1TB", "HDD 2TB", "HDD 2TB 7200RPM"]

ceny = [1100, 1900, 1700,
        1200, 1150, 980]

# Vytvoření grafu
plt.figure(figsize=(10, 5))
plt.bar(typy, ceny, color=["#4CAF50", "#4CAF50", "#4CAF50", "#2196F3", "#2196F3", "#2196F3"])

plt.title("Ceny SSD a HDD disků")
plt.ylabel("Cena v Kč")
plt.xticks(rotation=45, ha="right")
plt.grid(axis="y", linestyle="--", alpha=0.5)

# Zobrazení cen nad sloupci
for i, v in enumerate(ceny):
    plt.text(i, v + 30, f"{v} Kč", ha='center')

plt.tight_layout()
plt.show()
