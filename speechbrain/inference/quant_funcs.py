from speechbrain.inference import ASR_Quant_D
def speed(z):
    print(z)
    file.write(str(z)+"\n")
    print("1 loop")
    return

def run_speed_measurement(model,n,audio):
    with open("numbers.txt","a") as file:
        for i in range(n):
            print(i)
            #call out boi
            model.transcribe_file(audio)
    file.close()
    with open("numbers.txt","r")as file:
        lines = file.readlines()
    file.close()
    numbers_from_file = [int(line.strip()) for line in lines]
    total_sum = sum(numbers_from_file)
    avg=total_sum/n
    return avg
    