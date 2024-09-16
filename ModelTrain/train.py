from ultralytics import YOLO
import torch

def train(weights, data, epochs,batch):
    model = YOLO(weights)#.to('cuda' if torch.cuda.is_available() else 'cpu')
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model.train(data=data, epochs=epochs, imgsz=640, batch=batch, device=device)
 

if __name__ == '__main__':
    print(torch.cuda.is_available())
    train('yolov5mu.pt', 'sigara.yaml',epochs=20,batch=16)