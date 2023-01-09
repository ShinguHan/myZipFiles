import zipfile
import os
from datetime import datetime

def zipFiles(path):
    file_path = path
    zipFileCount = 15
    now = datetime.now()
    # date_time_str = now.strftime("%Y%m%d")
    if '/' in path:
        split = path.split('/')
    else:
        split = path.split('\\')
    site = split[-1]
    
    day = split[-2][:-1]
    if len(day) == 1:
        day = '0' + day
        
    month = split[-3][:-1]
    if len(month) == 1:
        month = '0' + month
        
    year = split[-4][:-1]
    
    date_time_str = '20' + year + month + day
    


    index = 1
    pdfFiles = []
    for file in os.listdir(file_path):
        if file.endswith('.pdf'):
            pdfFiles.append(file)
    
    lenPDFFiles = len(pdfFiles)
    if lenPDFFiles > 0:
        lstFormat = []
        
        if lenPDFFiles > zipFileCount:
            idx = 0
            for index in range(int(lenPDFFiles / zipFileCount)):
                idx = index + 1
                lstFormat.append([15,idx])
                
            if (lenPDFFiles % zipFileCount) != 0:
                lstFormat.append([lenPDFFiles % zipFileCount, idx +1])
        else:
            lstFormat = [[lenPDFFiles, 1]]
        
        for format in lstFormat:
            fileName = site + "_" + date_time_str + "_" + str(format[0]) + "EA_" + str(format[1])
            zip_file = zipfile.ZipFile(file_path + "\\" + fileName + ".zip", "w")  # "w": write 모드
            f = open(file_path + "\\" + fileName + ".txt", "a")
            
            if len(lstFormat) == 1:
                for file in pdfFiles:
                    f.writelines(file.split('.')[0]+'\n')                    
                    zip_file.write(os.path.join(file_path, file), compress_type=zipfile.ZIP_DEFLATED)
            else:
                strIndex = (format[1]-1) * zipFileCount
                endIndex = format[0] + ((format[1]-1) * zipFileCount)
                for idx in range(strIndex,endIndex):
                    f.writelines(str(pdfFiles[idx]).split('.')[0]+'\n')
                    zip_file.write(os.path.join(file_path, str(pdfFiles[idx])), compress_type=zipfile.ZIP_DEFLATED)                
                    
            zip_file.close()          
            f.close()
            
            

    

