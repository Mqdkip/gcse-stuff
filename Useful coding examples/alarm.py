def operate_alarm(chemical_reaction_rate,temperature,chemical_concentration):
        O = chemical_reaction_rate >= 40
        V = process_t <= 115
        E = chemical_concentration > 4

        return ((not O) or (E and (not V)) or (O and not V))


chemical_reaction_rate = int(input("Enter the chemical reaction rate: "))
process_t = int(input("Enter the process temperature (\u00B0C): "))
chemical_concentration = int(input("Enter the concentration of the chemical: "))

if operate_alarm(chemical_reaction_rate, process_t, chemical_concentration):
    print("Alarm On")
else:
    print("Alarm off")
