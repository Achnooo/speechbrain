from speechbrain.inference import ASR_Quant_D
import os
def speed(z):
    print(z)
    with open("numbers.txt","a")as file:
        file.write(str(z) + "\n")
    file.close() 
    print("1 loop")
    return

def run_speed_measurement(model,n,audio):
    delete_file_if_exists("numbers.txt")
    for i in range(n):
        print(i)
        model.transcribe_file(audio)

    with open("numbers.txt","r")as file:
        lines = file.readlines()
    file.close()
    numbers_from_file = [float(line.strip()) for line in lines]
    total_sum = sum(numbers_from_file)
    avg=total_sum/n
    return avg

def delete_file_if_exists(filename):
    if os.path.exists(filename):
        os.remove(filename)
    
def wer(predicted, correct):
    #calculate WER
    return