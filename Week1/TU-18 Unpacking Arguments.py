# Unpacking arguments is a method in passing arguments to a funtion in the order the function was defined.

# Let's say we want to pass a person's IQ index

def iqIndex(studyHours, reasoning, playfullness):
    dates_honey = reasoning
    brainUsage = (15 + studyHours) + (dates_honey * 10) - playfullness
    print(brainUsage)

maihajasData = [8, 10, 1]

iqIndex(maihajasData[0], maihajasData[1], maihajasData[2])

iqIndex(*maihajasData)

