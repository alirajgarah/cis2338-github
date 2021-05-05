def get_age():
    age = int(input())
    if(age>=18 and age<=75):
        return age
    else:
        raise ValueError("Invalid age.")

def fat_burning_heart_rate(age):
    return (220 - age) * 0.7

if __name__ == '__main__':
    try:
        age = get_age()
        print("Fat burning heart rate for a",age,"year-old:",fat_burning_heart_rate(age),"bpm")
    except ValueError as x:
        print(x.args[0])
        print("Could not calculate heart rate info.\n")
