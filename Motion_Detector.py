# ბატონო ირაკლი კოდის ძირითადი ნაწილი https://shorturl.at/SLoZK მოცემული სტატიიდან ავიღე.
# გარკვეული ლოგიკა შევცვალე დავალების მოთხოვნიდან გამომდინარე.
# შემთხვევითი რიცხვი გენერირდება მას შემდეგ რაც ვიდეოკამერა აფიქსირებს მოძრაობას.
# კოდის გაშვებამდე შესაძლოა შემდეგი ბრძანებების გაშვება დაგჭირდეთ: pip install opencv-python, pip install numpy

import cv2
import numpy as np
import random


def main():
    start = input(
        "\nAfter starting program press any key to stop it! \n"
        "Do you want to start the program? (yes/no): ").strip().lower()
    if start != 'yes':
        print("Exiting the program.")
        return

    cap = cv2.VideoCapture(0)
    last_mean = 0
    motion_flag = False

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to capture video. Exiting.")
            break

        cv2.imshow('frame', frame)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        result = np.abs(np.mean(gray) - last_mean)
        last_mean = np.mean(gray)

        if result > 0.3:
            print("Motion detected!")
            if not motion_flag:
                random_number = random.getrandbits(16)
                print(f"Generated random number: {random_number}")
                motion_flag = True

        if result <= 0.3:
            motion_flag = False

        if cv2.waitKey(1) != -1:
            print("Key pressed. Stopping the program.")
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
