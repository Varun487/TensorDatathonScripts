import os

start = 2005
end = 2019

metric = ['stdmet', 'cwind', 'swden', 'swdir', 'swdir2', 'swr1', 'swr2', 'ocean', 'srad']
bouy_id = 'BFTN7'
metric_char = ['h', 'c', 'w', 'd', 'i', 'j', 'k', 'o', 'r']
state = 'SOUTH_CAROLINA'
sub_folder = ['Standard', 'Wind', 'Spectral_wave_density','Spectral_wave_(alpha1)_direction_data', 'Spectral_wave_(alpha2)_direction_data', 'Spectral_wave_(r1)_direction_data', 'Spectral_wave_(r2)_direction_data', 'Ocean', 'Solar_radiation']

def init_folder(state, bouy_id):
        for new_folder in sub_folder:
            os.system('cmd /c "mkdir C:\\Users\\seshu\\Documents\\college_everything\\SEM4\\TENSOR_STUFF\\DATASETS\\NEW\\{}\\{}\\{}"'.format(state, bouy_id, new_folder))

init_folder(state, bouy_id)

def download_data(start, end, i):
    print("-----------------------SUBFOLDER {} ----------------------------".format(sub_folder[i]))
    while start <= end:
            command = "curl https://www.ndbc.noaa.gov/data/historical/{}/{}{}{}.txt.gz --output C:/Users/seshu/Documents/college_everything/SEM4/TENSOR_STUFF/DATASETS/NEW/{}/{}/{}/{}{}{}.txt.gz".format(metric[i],bouy_id.lower(),metric_char[i],start, state, bouy_id.upper(), sub_folder[i],bouy_id, metric_char[i],start)
            #print(command)
            os_string = 'cmd /c "{}"'.format(command)
            os.system(os_string)
            start += 1

for i in range(2):
    download_data(start, end, i)