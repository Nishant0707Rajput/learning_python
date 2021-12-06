from prescription_data import patients
trial_patients = {"Denise", "Eddie", "Frank", "Georgia", "Kenny"}

while trial_patients:
    patient = trial_patients.pop()

    prescription = patients[patient]
    print(patient, ":", prescription)
