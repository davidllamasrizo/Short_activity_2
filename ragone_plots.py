
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
P_values = np.logspace(-2, 0, 500) * P_max

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
plt.semilogx(P_pu, E_without_self_pu,
             color='blue', label='Without self-discharge')

# Plot with self-discharge
plt.semilogx(P_pu, E_with_self_pu,
             color='red', label='With self-discharge')

# Labels and title
plt.xlabel(r'Power (P/ (U$_0^2$/4R))')
plt.ylabel(r'Energy (E/Q$_0$U$_0$)')
plt.title('Ragone Discharge Plot for a battery')

# Grid and legend
plt.grid(True, which='both', linestyle='--', alpha=0.5)
plt.legend()

plt.tight_layout()
plt.show()
# ==========================================
# 7. CHARGE PROCESS
# ==========================================

# Function to calculate the energy stored
# during the battery charging process

def charge_energy(P):

    E_charge = (U0 * Q0
                + (U0 / (2 * R0)
                - np.sqrt(U0**2 / (4 * R0**2) + P / R0))
                * Q0 * R0)

    # Convert energy from Joules to Wh
    E_charge_Wh = E_charge / 3600

    return E_charge_Wh

# ==========================================
# 8. CHARGE RAGONE PLOT - DATA
# ==========================================

# Calculate the energy stored during charging
E_charge = charge_energy(P_values)

# Normalize charge energy
E_charge_pu = E_charge / E_nominal_Wh

# ==========================================
# 9. CHARGE RAGONE PLOT
# ==========================================

plt.figure(figsize=(8, 6))

# Plot charge curve
plt.semilogx(P_pu, E_charge_pu,
             color='blue', label='Charge')

# Labels and title
plt.xlabel(r'Power (P/ (U$_0^2$/4R))')
plt.ylabel(r'Energy (E/Q$_0$U$_0$)')
plt.title('Ragone Charge Plot for a Battery')

# Grid and legend
plt.grid(True, which='both', linestyle='--', alpha=0.5)
plt.legend()

plt.tight_layout()
plt.show()

# ==========================================
# 10. MAXIMUM POWER AND CURRENT
# ==========================================

# Maximum power
P_max = U0**2 / (4 * R0)

# Discharge current at maximum power
I_discharge_max = U0 / (2 * R0)

# Total battery current during discharge, including self-discharge
I_total_no_self = I_discharge_max + U0 / Rl_no_self
I_total_self = I_discharge_max + U0 / Rl_self

# Charging current at the same power
I_charge_max = (-U0 / (2 * R0)
                + np.sqrt(U0**2 / (4 * R0**2)
                + P_max / R0))

# Display results
print("\nMaximum power:")
print(f"{P_max:.3f} W")

print("\nDischarge current at maximum power:")
print(f"Load current: {I_discharge_max:.3f} A")
print(f"Total current without self-discharge: {I_total_no_self:.3f} A")
print(f"Total current with self-discharge: {I_total_self:.3f} A")

print("\nCharging current at the same power:")
print(f"{I_charge_max:.3f} A")

# ==========================================
# 11. C-RATE COMPARISON
# ==========================================

# Reference current at 1C
I_1C = Q0_Ah

# Calculate C-rates
C_rate_discharge = I_discharge_max / I_1C
C_rate_charge = I_charge_max / I_1C

# Display results
print("\nC-rate comparison:")
print(f"Reference current at 1C: {I_1C:.3f} A")
print(f"Discharge C-rate: {C_rate_discharge:.3f} C")
print(f"Charge C-rate: {C_rate_charge:.3f} C")
