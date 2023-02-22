import configparser


cf = configparser.ConfigParser()

def read_ini_as_dict(ini_path)->dict:
    cf.read(ini_path)
    rslt = {}
    for sections in cf.sections():
        rslt[sections] = {}
        for key in cf[sections]:
            value = cf[sections][key]
            if value[0]=="\"":
                if value == "\"":
                    rslt[sections][key] = "\""
                else:
                    s = ""
                    for cr in value[1:]:
                        if cr !="\"":
                            s = s+cr
                        else:
                            break
                    rslt[sections][key] = s
            elif value[0]=="'":
                if value == "'":
                    rslt[sections][key] = "'"
                else:
                    s = ""
                    for cr in value[1:]:
                        if cr !="'":
                            s = s+cr
                        else:
                            break
                    rslt[sections][key] = s
            else:
                rslt[sections][key] = value.split('#')[0].rstrip()
    return rslt
