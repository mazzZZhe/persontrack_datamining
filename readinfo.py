import json 

def readinfo(jsonfile):
    with open(jsonfile,'r') as f:    
        info = json.load(f)  
        #print(info)
        #print(info['camera'])
        cameraInfo = info['camera'] 
        #c1 = cameraInfo[0]
        #print(c1)
        #position = [[camera['x'],camera['y']] for camera in cameraInfo]
        #print(len(cameraInfo))
        #print(position)
        #print(info['interval_time'])
        #names = [camera['name'] for camera in cameraInfo]
        #print(names)
        return info
readinfo('info.json')

