#Program to find network speed
#time = size of file (in bits) / network speed (in bits)
#1Mbps = 1 million bps
#1Gbps = 1 billion bps
#1 Kib = 1024 bytes
#1 MiB = 1049000 bytes
memory = input("What is the size of the file you are downloading? Options are: bytes, KiB, MiB")
size = int(input("What is the size of the file (units not included)(in integer format)?"))
speedtype = input("What is the unit of transmission speed you are using? Options are: bps, Mbps, Gbps")
speed = int(input("What is the speed of download (units not included)(in integer format)?")
            
if memory == "bytes" and speedtype == "bps":
            print(size/speed)

    elif memory == "bytes": and speedtype == "Mbps":
        speed*1000000
        print(size/speed)

    elif memory == "bytes": and speedtype == "Gbps":
        speed*1000000000
         print(size/speed)

    elif memory == "KiB": and speedtype == "bps":
        size*1024
        print(size/speed)

    elif memory == "KiB": and speedtype == "Mbps":
        size*1024
        speed*1000000
         print(size/speed)

    elif memory == "KiB": and speedtype == "Gbps":
        size*1024
        speed*1000000000
         print(size/speed)

    elif memory == "MiB": and speedtype == "bps":
        size*1049000
         print(size/speed)


    elif memory == "MiB": and speedtype == "Mbps":
        size*1049000
        speed*1000000
         print(size/speed)

    elif memory == "MiB": and speedtype == "Gbps":
         size*1049000
         speed*1000000000
         print(size/speed)

    else:
        print("invalid unit")
