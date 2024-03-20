from speechbrain.inference import ASR_Quant_D
def speed(z):
    print(z)
    with open("numbers.txt","a")as file:
        file.write(str(z) + "\n")
    file.close() 
    print("1 loop")
    return

def run_speed_measurement(model,n,audio):
    for i in range(n):
        print(i)
        #call out boi
        model.transcribe_file(audio)

    with open("numbers.txt","r")as file:
        lines = file.readlines()
    file.close()
    numbers_from_file = [float(line.strip()) for line in lines]
    total_sum = sum(numbers_from_file)
    avg=total_sum/n
    return avg
    