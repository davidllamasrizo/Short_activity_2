
# ==========================================
# SHORT ACTIVITY 2 - RAGONE PLOTS
# Energy Storage Technologies
# Lithium-ion battery
# ==========================================

# 1. BATTERY PARAMETERS

U0 = 3.7          # Open circuit voltage (V)
R0 = 0.05         # Internal resistance (Ohm)

Q0_Ah = 2         # Battery capacity (Ah)
Q0 = Q0_Ah * 3600 # Battery capacity (A.s)

Rl_no_self = 1000 # Leakage resistance without self-discharge (Ohm)
Rl_self = 20      # Leakage resistance with self-discharge (Ohm)


# 2. NOMINAL ENERGY AND MAXIMUM POWER

# Nominal energy
E_nominal = U0 * Q0       # Energy in Joules (J)
E_nominal_Wh = E_nominal / 3600  # Energy in Wh

# Maximum power
P_max = U0**2 / (4 * R0)  # Maximum power (W)

# Display results
print("Nominal energy:")
print(E_nominal, "J")
print(E_nominal_Wh, "Wh")

print("\nMaximum power:")
print(P_max, "W")


# ==========================================
# 3. DISCHARGE PROCESS
# ==========================================

import numpy as np

# Function to calculate the energy delivered
# during the battery discharge process

def discharge_energy(P, Rl):

    # Calculate the total discharge current
    It = (U0 / (2 * R0)
          - np.sqrt(U0**2 / (4 * R0**2) - P / R0)
          + U0 / Rl)

    # Calculate the energy delivered (J)
    E_load = P * Q0 / It

    # Convert energy from Joules to Wh
    E_load_Wh = E_load / 3600

    return E_load_Wh

# ==========================================
# 4. DISCHARGE RAGONE PLOT - DATA
# ==========================================

# Generate power values (W)
P_values = np.linspace(0.01, P_max, 500)

# Calculate discharge energy without self-discharge
E_without_self = discharge_energy(P_values, Rl_no_self)

# Calculate discharge energy with self-discharge
E_with_self = discharge_energy(P_values, Rl_self)

# ==========================================
# 5. NORMALIZATION
# ==========================================

# Normalize power
P_pu = P_values / P_max

# Normalize discharge energy
E_without_self_pu = E_without_self / E_nominal_Wh
E_with_self_pu = E_with_self / E_nominal_Wh

# ==========================================
# 6. DISCHARGE RAGONE PLOT
# ==========================================

import matplotlib.pyplot as plt

plt.figure(figsize=(8, 6))

# Plot without self-discharge
plt.loglog(P_pu, E_without_self_pu,
           color='blue', label='Without self-discharge')

# Plot with self-discharge
plt.loglog(P_pu, E_with_self_pu,
           color='red', label='With self-discharge')

# Labels and title
plt.xlabel('Normalized Power (p.u.)')
plt.ylabel('Normalized Energy (p.u.)')
plt.title('Ragone Plot - Discharge')

# Grid and legend
plt.grid(True, which='both', linestyle='--', alpha=0.5)
plt.legend()

plt.tight_layout()
plt.show()
