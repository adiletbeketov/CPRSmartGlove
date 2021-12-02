import serial
import time

def time_convert(sec):
  mins = sec // 60
  sec = sec % 60
  hours = mins // 60
  mins = mins % 60
  #print("Time Lapsed = {0}:{1}:{2}".format(int(hours),int(mins),sec))
  return (sec)

def cycles(start_time,end_time, data):
    pass
    state=0
    counter=0
    for i in range(2,len(data)):
        if(state==0 and i<(len(data)-2)):
            if (data[i+1]>mavg and data[i]>mavg and data[i-1]<(mavg-(mavg-mmin)/2)):
                print("pressed")
                state=1
        if(state==1 and i<(len(data)-2)):
            if (data[i]<mavg and data[i+1]<mavg and data[i+2]<mavg):
                print("released")
                state=0
                counter+=1
    time_lapsed = end_time - start_time
    print(counter,"presses over" ,time_convert(time_lapsed), "seconds.")

mmax=250
mavg=185
mmin=120

try:
    ser = serial.Serial('COM4', 9600, timeout=1)
    
except:
    print("Could not connect to the arduino. Closing...")
    exit()

print("Successfully connected to the arduino.")
for i in range(5):
    print(5-i,"second(s) to start!")
    time.sleep(1)

time.sleep(1)
ser.flush()
ser.read_all()
print("GOGOGOGOGOGO")
start_time = time.time()
data=[]
for i in range(180):
    vara=ser.readline()
    if (vara):
        data.append(vara)
    
    ser.read_all()
    time.sleep(0.05)
end_time = time.time()
print(len(data), "data points")
for i in range(len(data)):
    print(data[i])

for i in range(len(data)):
    try:
        data[i]=int(data[i].decode().strip())
    except:
        print("invalid data", data[i])
        if (i!=0):
            data[i]=data[i-1]
        else:
            data[i]=0
        

cycles(start_time,end_time,data)





