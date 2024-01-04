desired_jump = int(input())

total_jumps = 0
failed_jumps = 0
init_jump = desired_jump - 30

while True:
    if failed_jumps == 3:
        print(f"Tihomir failed at {init_jump}cm after {total_jumps} jumps.")
        break
    current_jump = int(input())
    total_jumps += 1
    if init_jump == desired_jump:
        if current_jump > desired_jump:
            print(f"Tihomir succeeded, he jumped over {desired_jump}cm after {total_jumps} jumps.")
            break
    if current_jump > init_jump:
        init_jump += 5
        failed_jumps = 0
    else:
        failed_jumps += 1
        continue



