import math
from data import *

c_T = 1 

def calculate_max_endurance_turbojet():
    CL_opt = math.sqrt(CD0/k)
    CD_opt = CD0 + k * CL_opt**2
    L_D_max = CL_opt / CD_opt

    m_initial = m
    m_final = m - fuelMass
    
    E_max = (L_D_max / c_T) * math.log(m_initial / m_final)
    
    return E_max, CL_opt

def calculate_max_range_turbojet():
    CL_opt = math.sqrt(CD0 / k)
    CD_opt = CD0 + k * CL_opt**2
    L_D_max = CL_opt / CD_opt
    
    m_initial = m
    m_final = m - fuelMass
    
    R_max = (2 / c_T) * math.sqrt(2 / (density * S)) * L_D_max * (math.sqrt(m_initial) - math.sqrt(m_final))
    
    return R_max, CL_opt

def calculate_max_endurance_turboprop():
    CL_opt = math.sqrt(3 * CD0 / k)
    CD_opt = CD0 + k * CL_opt**2
    CL_15_CD = CL_opt**1.5 / CD_opt
    
    m_initial = m
    m_final = m - fuelMass
    
    E_max = (CL_15_CD / c_T) * math.sqrt(2 * density * S) * (1 / math.sqrt(m_final) - (1 / math.sqrt(m_initial)))
    
    return E_max, CL_opt

def calculate_max_range_turboprop():
    CL_opt = math.sqrt(CD0 / k)
    CD_opt = CD0 + k * CL_opt**2
    L_D_max = CL_opt / CD_opt
    
    m_initial = m
    m_final = m - fuelMass
    
    R_max = (L_D_max / c_T) * math.log(m_initial / m_final)
    
    return R_max, CL_opt

E_max_jet, CL_jet_E = calculate_max_endurance_turbojet()
R_max_jet, CL_jet_R = calculate_max_range_turbojet()
    
E_max_prop, CL_prop_E = calculate_max_endurance_turboprop()
R_max_prop, CL_prop_R = calculate_max_range_turboprop()
    
print("Turbojet Performance:")
print("Maximum Endurance:", E_max_jet, "seconds at CL =", CL_jet_E)
print("Maximum Range:",R_max_jet,"meters at CL =", CL_jet_R,"\n")
print("Turboprop Performance:")
print("Maximum Endurance:",E_max_prop,"seconds at CL =", CL_prop_E)
print("Maximum Range:", R_max_prop,"meters at CL =", CL_prop_R)