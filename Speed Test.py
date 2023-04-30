import time

print("Welcome to the Speed Typing Test!")
print("Type the following text as fast as you can:\n")

# the text to be typed
text = "The quick brown fox jumps over the lazy dog."

print(text)

# start the timer
start_time = time.time()

# get user input
user_input = input()

# stop the timer
end_time = time.time()

# calculate the elapsed time
elapsed_time = end_time - start_time

# calculate the typing speed
typing_speed = len(text) / elapsed_time

# display the results
print("You typed the following text in", elapsed_time, "seconds.")
print("Your typing speed was", typing_speed, "characters per second.")