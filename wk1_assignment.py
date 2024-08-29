import pandas as pd 


impatient = pd.read_csv(
    'https://data.cms.gov/sites/default/files/2023-04/67157de9-d962-4af0-bf0e-3578b3afec58/inpatient.csv',
    sep='|')


print(impatient.head())


#What columns are related to medical codexes?
hcpcs_code = impatient[['HCPCS_CD']]
idc_codes = impatient[['ICD_DGNS_CD1', 'IDC_DGNS_CD10', 'IDC_DGNS_CD11',
                       'IDC_DGNS_CD12', 'IDC_DGNS_CD13', 'IDC_DGNS_CD14',
                       'IDC_DGNS_CD15', 'IDC_DGNS_CD16', 'IDC_DGNS_CD17',
                       'IDC_DGNS_CD18', 'IDC_DGNS_CD19', 'IDC_DGNS_CD20',
                       'IDC_DGNS_CD2', 'IDC_DGNS_CD21', 'IDC_DGNS_CD22',
                       'IDC_DGNS_CD23', 'IDC_DGNS_CD24', 'IDC_DGNS_CD25',
                       'IDC_DGNS_CD3', 'IDC_DGNS_CD4']]
