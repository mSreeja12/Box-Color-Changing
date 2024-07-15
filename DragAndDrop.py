import cv2
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)
cap.set(3, 1100)  
cap.set(4, 720)   

detector = HandDetector(detectionCon=0.8, maxHands=2)

while True:
    success, img = cap.read()
    if not success:
        continue
    
    img = cv2.flip(img, 1)
    
    hands, img = detector.findHands(img) 
   
    if hands:
        for hand in hands:
            lmlist = hand['lmList']  
            bbox = hand['bbox']  
            centerPoint = hand['center']  
            
            cursor = lmlist[8]
           
            if 100 < cursor[0] < 250 and 100 < cursor[1] < 250:
                color = (0, 255, 0)
            else:
                color = (0, 0, 255)
                
            cv2.rectangle(img, (100, 100), (250, 250), color, cv2.FILLED)

            cv2.circle(img, centerPoint, 10, (255, 0, 255), cv2.FILLED)

            for lm in lmlist:
                cv2.circle(img, (lm[0], lm[1]), 5, (0, 255, 0), cv2.FILLED)
   
    cv2.imshow("Image", img)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
