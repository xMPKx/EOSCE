import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Parameter
station_names = [f"Station {i+1}" for i in range(12)]
times = [f"{8+i}:00" for i in range(9)]

# Zufallsdaten erzeugen (Anzahl Prüflinge pro Station pro Stunde)
np.random.seed(42)  # für Reproduzierbarkeit
data = np.random.randint(0, 11, size=(9, 12))

# DataFrame erstellen
df = pd.DataFrame(data, index=times, columns=station_names)

print(df)


plt.plot(times, df["Station 1"], marker="o", color="green")
plt.xlabel("Zeit")
plt.ylabel("Prüflinge")
plt.title("EOSCE – Station 1")
plt.show()