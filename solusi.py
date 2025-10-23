import pulp as lp

# Inisialisasi model
model = lp.LpProblem("Optimasi_Transportasi_PT_Sembako_Jaya", lp.LpMinimize)

# Data biaya (dalam ribu rupiah)
biaya = [
    [10, 12, 8, 11],  # P1 ke G1..G4
    [9, 10, 11, 9],   # P2 ke G1..G4
    [13, 9, 10, 8]    # P3 ke G1..G4
]

supply = [1200, 1000, 1500]  # kapasitas pabrik
demand = [900, 800, 1300, 700]  # kebutuhan gudang

# Variabel keputusan x_ij
x = [[lp.LpVariable(f"x{i}{j}", lowBound=0) for j in range(4)] for i in range(3)]

# Fungsi tujuan: minimisasi total biaya
model += lp.lpSum(biaya[i][j] * x[i][j] for i in range(3) for j in range(4))

# Kendala pasokan (supply)
for i in range(3):
    model += lp.lpSum(x[i][j] for j in range(4)) == supply[i]

# Kendala permintaan (demand)
for j in range(4):
    model += lp.lpSum(x[i][j] for i in range(3)) == demand[j]

# Jalankan solver
model.solve()

# Tampilkan hasil
print("Status:", lp.LpStatus[model.status])
for i in range(3):
    for j in range(4):
        if x[i][j].value() > 0:
            print(f"P{i+1} -> G{j+1} : {x[i][j].value()} unit")
print("Total biaya minimum (ribu Rp):", lp.value(model.objective))
