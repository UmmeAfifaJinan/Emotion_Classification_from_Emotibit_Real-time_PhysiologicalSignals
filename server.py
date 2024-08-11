import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 12346 # Specified in C:\Program Files\EmotiBit\EmotiBit Oscilloscope\data\udpOutputSettings.xml

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))
# EA (miocrosiemens)
# BI (mS)

#condition list
# 1: vib = off, weight = small
# 2: vib = on, weight = small
# 3: vib = off, weight = large
# 4: vib = on, weight = large


currentDateAndTest = "2024-04-03_"
currentDateAndTest += "Cond3_"
currentDateAndTest += "Test2"

with open(currentDateAndTest + "-HR-output.csv", "a") as HRf:
    with open(currentDateAndTest + "-EA-output.csv", "a") as EAf:
        with open(currentDateAndTest + "-BI-output.csv", "a") as BIf:
    
            HRf.write("Time(ms), HeartRate(bpm)\n")
            EAf.write("Time(ms), Electrodermal Activity(MicroSiemens)\n")
            BIf.write("Time(ms), Inter-beat Interval(mS)\n")

            while True:
                data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
                DS = str(data)
                tags = DS.split(',')
                if tags[3] == 'HR': 
                    #tag 1 = time in ms, tag 6 = current heartrate in bpm
                    HRf.write(tags[1]+","+tags[6] + "\n")
                    print(tags[1]+","+tags[6])
                    HRf.flush()
                if tags[3] == 'EA': 
                    #tag 1 = time in ms, tag 6 = current Activity in microSiemens
                    EAf.write(tags[1]+","+tags[6] + "\n")
                    print(tags[1]+","+tags[6])
                    EAf.flush()
                if tags[3] == 'BI': 
                    #tag 1 = time in ms, tag 6 = current BI in mS
                    BIf.write(tags[1]+","+tags[6] + "\n")
                    print(tags[1]+","+tags[6])
                    BIf.flush() 

                
