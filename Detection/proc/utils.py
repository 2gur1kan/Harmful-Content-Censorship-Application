from PySide6.QtGui import QImage, QPixmap
import cv2 
import torch 


def is_cuda_available():
    return torch.cuda.is_available()


def cv2qimage(cv2image): 
    rgb_image = cv2.cvtColor(cv2image, cv2.COLOR_BGR2RGB)
    h, w, ch = rgb_image.shape
    bytes_per_line = ch * w
    qimage = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)
    return QPixmap.fromImage(qimage)


def cv2blur(frame, x1, x2, y1, y2, k_size):
    crop_obj = frame[int(y1):int(y2),int(x1):int(x2)]
    blur = cv2.blur(crop_obj,(k_size,k_size))
    frame[int(y1):int(y2),int(x1):int(x2)] = blur
    return frame

def cv2rect(frame, x1, x2, y1, y2):

    return frame  # bu kısım etrafını çizmemesi için çıkarılmıştır

    cv2.rectangle(frame, 
                  (int(x1), int(y1)), 
                  (int(x2), int(y2)), 
                  (56, 56, 255), 
                  2)
    
    return frame 
            

def cv2label(frame, x1, x2, y1, y2, label):

    return frame  # bu kısım etiketi atmaması için çıkarılmıştır

    t_size = cv2.getTextSize(label, 
                             0, 
                             fontScale=0.6, 
                             thickness=1)[0]
    
    cv2.rectangle(
                frame, 
                (int(x1), int(y1) - t_size[1] - 3), 
                (int(x1) + t_size[0], int(y1) + 3), 
                (56, 56, 255), 
                -1)
    
    cv2.putText(frame, 
                label, 
                (int(x1), int(y1) - 2), 
                0, 
                0.6, 
                [255, 255, 255], 
                thickness=1, 
                lineType=cv2.LINE_AA)
    
    return frame 