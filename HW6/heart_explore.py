# -*- coding: utf-8 -*-
"""
Madeline Coco
Programming with Data
Created on Wed Oct 26 17:44:07 2022

File: heart_explore.py
    
Description: We are looking at all patient data and comparing it to the data
of just patients with heart disease.

Results:
Number of patients: 918
Number of patients with heart disease: 508
Average age of all patients: 53.5
Average age of patients w/ heart disease: 55.9
Average resting blood pressure of all patients: 132.4
Average resting blood pressure of patients w/ heart disease: 134.2
"""
import matplotlib.pyplot as plt

def read_data():
    filename = "heart.csv"
    
    all_patients = []
    
    with open(filename,"r") as infile:
        header = infile.readline()
        all_lines = infile.readlines()
    
    for patient in all_lines:
        single_patient = patient.strip().split(",")
        single_patient[0] = int(single_patient[0])
        single_patient[3] = int(single_patient[3])
        single_patient[4] = int(single_patient[4])
        single_patient[5] = int(single_patient[5])
        single_patient[6] = int(single_patient[6])

        all_patients.append(single_patient)
      
    return all_patients
    
def heart_disease_patient_list(all_patients):
    heart_disease_patients = []
    for patient in all_patients:
        if (patient[6] == 1):
            heart_disease_patients.append(patient)
        
    return heart_disease_patients
            
def num_patients(all_patients, heart_disease_patients):
    total_patients = len(all_patients)
    print("Number of patients:", total_patients)
    total_heart_disease = len(heart_disease_patients)
    print("Number of patients with heart disease:", total_heart_disease)

def average_age(all_patients, heart_disease_patients):
    patient_ages = []
    hd_patient_ages = []
    
    for patient in all_patients:
        patient_ages.append(patient[0])
        
    for hd_patient in heart_disease_patients:
        hd_patient_ages.append(hd_patient[0])
    
    age_sum = sum(patient_ages)
    average_age = age_sum / len(all_patients)
    print("Average age of all patients:", round(average_age, 1))
    
    hd_age_sum = sum(hd_patient_ages)
    average_age_hd = hd_age_sum / len(heart_disease_patients)
    print("Average age of patients w/ heart disease:", round(average_age_hd, 1))
    
    return average_age, average_age_hd

def average_bp(all_patients, heart_disease_patients):
    patient_bp = []
    hd_patient_bp = []
    
    for patient in all_patients:
        patient_bp.append(patient[3])
        
    for hd_patient in heart_disease_patients:
        hd_patient_bp.append(hd_patient[3])
    
    bp_sum = sum(patient_bp)
    average_bp = bp_sum / len(all_patients)
    print("Average resting blood pressure of all patients:", round(average_bp, 1))
    
    hd_bp_sum = sum(hd_patient_bp)
    average_bp_hd = hd_bp_sum / len(heart_disease_patients)
    print("Average resting blood pressure of patients w/ heart disease:", round(average_bp_hd, 1))

    return average_bp, average_bp_hd

def no_heart_disease(all_patients):
    no_hd_patients = []
    for patient in all_patients:
        if (patient[6] == 0):
            no_hd_patients.append(patient)
        
    return no_hd_patients
    
def plot_data(no_hd_patients, heart_disease_patients):
    patient_chol = []
    patient_hr = []
    hd_patient_chol = []
    hd_patient_hr = []
    
    for patient in no_hd_patients:
        patient_chol.append(patient[4])
        patient_hr.append(patient[5])
        
    for hd_patient in heart_disease_patients:
        hd_patient_chol.append(hd_patient[4])
        hd_patient_hr.append(hd_patient[5])
        
    
    plt.scatter(hd_patient_hr, hd_patient_chol, marker = '.', color = 'r', label = 'Patients w/ heart disease')
    plt.scatter(patient_hr, patient_chol, marker = '.', color = 'b', label = 'Patients w/ no heart disease')
    plt.title("Cholesterol vs Max HR in Patients")
    plt.xlabel("Maximum heart rate")
    plt.ylabel("Cholesterol")
    plt.legend()
    plt.savefig("heart.pdf")
    plt.show()
    

def main():
    all_patients = read_data()
    heart_disease_patients = heart_disease_patient_list(all_patients)
    num_patients(all_patients, heart_disease_patients)
    average_age(all_patients, heart_disease_patients)
    average_bp(all_patients, heart_disease_patients)
    no_hd_patients = no_heart_disease(all_patients)
    plot_data(no_hd_patients, heart_disease_patients)

main()
