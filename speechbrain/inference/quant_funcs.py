from speechbrain.inference import ASR_Quant_D
import os
def speed(z):
    print(z)
    with open("numbers.txt","a")as file:
        file.write(str(z) + "\n")
    file.close()
    return

def run_speed_measurement(model,n,audio,my_text):
    delete_file_if_exists("numbers.txt")
    for i in range(n):
        print(i)
        words = model.transcribe_file(audio)

    with open("numbers.txt","r")as file:
        lines = file.readlines()
    file.close()
    numbers_from_file = [float(line.strip()) for line in lines]
    total_sum = sum(numbers_from_file)
    avg=total_sum/n
    print(wer(my_text,words))
    return avg

def delete_file_if_exists(filename):
    if os.path.exists(filename):
        os.remove(filename)
    
def wer(ref, hyp):
    # Tokenize the strings into words
    ref_words = ref.split()
    hyp_words = hyp.split()
    # Length of reference text
    N = len(ref_words)
    
    # Initialize matrices for dynamic programming
    dp = [[0] * (len(hyp_words) + 1) for _ in range(len(ref_words) + 1)]
    
    # Initialize first row and column
    for i in range(len(ref_words) + 1):
        dp[i][0] = i
    
    for j in range(len(hyp_words) + 1):
        dp[0][j] = j
    
    # Dynamic programming to compute edit distance
    for i in range(1, len(ref_words) + 1):
        for j in range(1, len(hyp_words) + 1):
            if ref_words[i - 1] == hyp_words[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
    
    # WER calculation
    wer = float(dp[-1][-1]) / N
    
    return wer
