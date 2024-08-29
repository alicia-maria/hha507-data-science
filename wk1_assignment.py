import pandas as pd 


impatient = pd.read_csv(
    'https://data.cms.gov/sites/default/files/2023-04/67157de9-d962-4af0-bf0e-3578b3afec58/inpatient.csv',
    sep='|')


print(impatient.head())


#What columns are related to medical codexes?
hcpcs_code = impatient[['HCPCS_CD']]
idc_codes = impatient[['ICD_DGNS_CD1', 'ICD_DGNS_CD10', 'ICD_DGNS_CD11',
                       'ICD_DGNS_CD12', 'ICD_DGNS_CD13', 'ICD_DGNS_CD14',
                       'ICD_DGNS_CD15', 'ICD_DGNS_CD16', 'ICD_DGNS_CD17',
                       'ICD_DGNS_CD18', 'ICD_DGNS_CD19', 'ICD_DGNS_CD20',
                       'ICD_DGNS_CD2', 'ICD_DGNS_CD21', 'ICD_DGNS_CD22',
                       'ICD_DGNS_CD23', 'ICD_DGNS_CD24', 'ICD_DGNS_CD25',
                       'ICD_DGNS_CD3', 'ICD_DGNS_CD4']]
drg_codes = impatient[['CLM_DRG_CD','CLM_DRG_OUTLIER_STAY_CD',]]



#Frequency count of medical codexes
hcpcs_frequency = hcpcs_code.value_counts()
print("HCPCS Codes Frequency::\n""idc_frequency",)


idc_frequency = idc_codes.value_counts()
print("IDC Codes Frequency::\n""idc_frequency",)

drg_frequency = drg_codes.value_counts()
print("DRG Codes Frequency::\n""idc_frequency",)


#Missing Data 
missing_icd = idc_codes.isnull().sum()
missing_drg = drg_codes.isnull().sum()
missing_hcpcs = hcpcs_code.isnull().sum()

print(f"Missing ICD Codes: {missing_icd}")
print(f"Missing DRG Codes: {missing_drg}")
print(f"Missing HCPCS Codes: {missing_hcpcs}")


#Summary of findings 
print("Top 5 Most Common ICD Codes:\n", idc_frequency.head())
print("Top 5 Most Common DRG Codes:\n", drg_frequency.head())
print("Top 5 Most Common HCPCS Codes:\n", hcpcs_frequency.head())
