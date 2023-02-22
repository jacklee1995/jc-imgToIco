import os
def get_allfiles_path(path):
    Absolute_path = []
    a = []

    for dirpath, dirnames, filenames in os.walk(path): 
        a.append(os.path.join(dirpath))
    
    for i in a:               
        dir_list = os.listdir(i)    
        for j in dir_list:
            sub_dir = os.path.join(i, j)
            if os.path.isdir(sub_dir):   
                pass
            else:                
                Absolute_path.append(sub_dir)
    return(Absolute_path)