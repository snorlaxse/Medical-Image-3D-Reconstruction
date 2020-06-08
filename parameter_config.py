import pydicom
import os

dcm_dir = '/Users/Captain/Desktop/Homework_19031211529_郑健/data/test_case_01'
tmp_file = os.path.join(dcm_dir, os.listdir(dcm_dir)[0])
ds = pydicom.dcmread(tmp_file)
rescale_slope = int(ds['00281053'].value)
rescale_intercept = int(ds['00281052'].value)
