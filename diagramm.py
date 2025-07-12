import matplotlib.pyplot as plt
import numpy as np

# Daten für die 114 Suren (chronologische Reihenfolge)
suren = list(range(1, 115))  # Suren 1 bis 114
# Geschätzte Anzahl der Verse mit diesseitigen und jenseitigen Drohungen
# Basierend auf der Analyse: Mekkanische Suren (1-86) hauptsächlich jenseitig, medinensische (87-114) gemischt
diesseitige_drohungen = [
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  # Sure 96, 68, 73, 74, 1, 111, 81, 87, 92, 89
    0, 0, 0, 0, 0, 0, 0, 0, 2, 0,  # Sure 93, 94, 103, 100, 108, 102, 107, 109, 105, 113
    0, 0, 0, 0, 0, 0, 2, 0, 0, 2,  # Sure 114, 112, 53, 80, 97, 91, 85, 95, 106, 101
    0, 2, 2, 2, 0, 2, 2, 2, 4, 2,  # Sure 75, 104, 77, 50, 90, 86, 54, 38, 7, 72
    2, 2, 2, 2, 4, 2, 2, 2, 2, 2,  # Sure 36, 25, 35, 19, 20, 56, 26, 27, 28, 17
    2, 2, 0, 2, 4, 2, 2, 2, 2, 2,  # Sure 10, 11, 12, 15, 6, 37, 31, 34, 39, 40
    2, 2, 2, 2, 2, 2, 2, 2, 2, 2,  # Sure 41, 42, 43, 44, 45, 46, 51, 88, 18, 16
    2, 2, 2, 2, 2, 2, 2, 2, 2, 2,  # Sure 71, 14, 21, 23, 32, 52, 67, 69, 70, 78
    2, 2, 2, 2, 2, 4, 4, 4, 4, 2,  # Sure 79, 82, 84, 30, 29, 83, 2, 8, 3, 33
    2, 4, 2, 2, 2, 2, 2, 2, 2, 2,  # Sure 60, 4, 99, 57, 47, 13, 55, 76, 65, 98
    4, 4, 4, 2, 2, 2, 2, 2, 2, 2,  # Sure 59, 24, 22, 63, 58, 49, 66, 62, 64, 61
    2, 6, 8, 0  # Sure 48, 5, 9, 110
]
jenseitige_drohungen = [
    4, 3, 2, 4, 1, 3, 1, 2, 2, 2,  # Sure 96, 68, 73, 74, 1, 111, 81, 87, 92, 89
    0, 0, 1, 1, 1, 2, 1, 0, 0, 2,  # Sure 93, 94, 103, 100, 108, 102, 107, 109, 105, 113
    0, 0, 1, 2, 0, 2, 2, 1, 0, 3,  # Sure 114, 112, 53, 80, 97, 91, 85, 95, 106, 101
    2, 3, 3, 3, 2, 0, 2, 3, 6, 2,  # Sure 75, 104, 77, 50, 90, 86, 54, 38, 7, 72
    3, 3, 2, 2, 4, 4, 3, 2, 2, 3,  # Sure 36, 25, 35, 19, 20, 56, 26, 27, 28, 17
    2, 3, 0, 2, 5, 3, 2, 2, 3, 3,  # Sure 10, 11, 12, 15, 6, 37, 31, 34, 39, 40
    3, 2, 3, 3, 3, 2, 3, 3, 3, 3,  # Sure 41, 42, 43, 44, 45, 46, 51, 88, 18, 16
    2, 2, 2, 3, 2, 3, 3, 3, 3, 3,  # Sure 71, 14, 21, 23, 32, 52, 67, 69, 70, 78
    3, 3, 3, 2, 3, 3, 6, 5, 5, 3,  # Sure 79, 82, 84, 30, 29, 83, 2, 8, 3, 33
    2, 5, 2, 3, 3, 2, 2, 2, 2, 2,  # Sure 60, 4, 99, 57, 47, 13, 55, 76, 65, 98
    3, 4, 3, 2, 2, 1, 3, 1, 2, 2,  # Sure 59, 24, 22, 63, 58, 49, 66, 62, 64, 61
    2, 6, 7, 0  # Sure 48, 5, 9, 110
]

# Diagramm erstellen
plt.figure(figsize=(20, 8))
bar_width = 0.4
plt.bar(suren, jenseitige_drohungen, bar_width, label='Jenseitige Drohungen', color='red')
plt.bar(np.array(suren) + bar_width, diesseitige_drohungen, bar_width, label='Diesseitige Drohungen', color='blue')

# Beschriftungen und Layout
plt.xlabel('Sure (Chronologische Reihenfolge)')
plt.ylabel('Anzahl der Verse mit Drohungen')
plt.title('Diesseitige und Jenseitige Drohungen in den 114 Suren des Korans')
plt.legend()
plt.axvline(x=86.5, color='black', linestyle='--', label='Trennung Mekkanisch/Medinensisch')
plt.xticks(np.arange(1, 115, step=5), rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()

# Diagramm speichern
plt.savefig('koran_drohungen_diagramm.png')
plt.show()
