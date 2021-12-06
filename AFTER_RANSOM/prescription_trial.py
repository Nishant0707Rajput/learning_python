from prescription_data import *


trial_patients = ["Denise", "Eddie", "Frank", "Georgia", "Kenny"]

# Remove Warfarin and add Edoxaban
for patient in trial_patients:
    prescription = patients[patient]
    try:
        prescription.remove(warfarin)
        prescription.add(edoxaban)
    except KeyError:
        print(f"Patient {patient} doesn't need to be in this trial")
    print(patient,prescription)
