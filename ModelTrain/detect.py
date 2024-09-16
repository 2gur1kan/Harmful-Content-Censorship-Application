import argparse
from pathlib import Path

import cv2
from sahi import AutoDetectionModel
from sahi.predict import get_sliced_prediction 

from ultralytics.utils.files import increment_path


def run( source="test.mp4"):
    """
    Run object detection on a video using YOLOv8 and SAHI.

    Args: 
        source (str): Video file path. 
    """

    # Check source path
    if not Path(source).exists():
        raise FileNotFoundError(f"Source path '{source}' does not exist.")

    yolov8_model_path = f"models/sigarav8s.pt" 
    detection_model = AutoDetectionModel.from_pretrained(
        model_type="yolov8", model_path=yolov8_model_path, confidence_threshold=0.3, device="cuda:0"
    ) # device= "cpu" or "cuda:0"

    # Video setup
    videocapture = cv2.VideoCapture(source)
    frame_width = int(videocapture.get(3))
    frame_height = int(videocapture.get(4))
    fps = int(videocapture.get(5))
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    save_dir = "output/"
    video_writer = cv2.VideoWriter(str(save_dir + f"{Path(source).stem}.mp4"), 
                                   fourcc, fps, (frame_width, frame_height))

    while videocapture.isOpened():
        success, frame = videocapture.read()
        if not success:
            break

        results = get_sliced_prediction(
            frame, detection_model, 
            slice_height=640, slice_width=640, 
            overlap_height_ratio=0.02, 
            overlap_width_ratio=0.02
        )

        object_prediction_list = results.object_prediction_list

        boxes_list = []
        clss_list = []
        for ind, _ in enumerate(object_prediction_list):
            boxes = (
                object_prediction_list[ind].bbox.minx,
                object_prediction_list[ind].bbox.miny,
                object_prediction_list[ind].bbox.maxx,
                object_prediction_list[ind].bbox.maxy,
            )
            clss = object_prediction_list[ind].category.name
            boxes_list.append(boxes)
            clss_list.append(clss)

        for box, cls in zip(boxes_list, clss_list):
            x1, y1, x2, y2 = box

             # bulanıklaştırma işlemi
            crop_obj = frame[int(y1):int(y2),int(x1):int(x2)]
            blur = cv2.blur(crop_obj,(30,30))
            frame[int(y1):int(y2),int(x1):int(x2)] = blur

            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (56, 56, 255), 2)
            label = str(cls)
            t_size = cv2.getTextSize(label, 0, fontScale=0.6, thickness=1)[0]
            cv2.rectangle(
                frame, (int(x1), int(y1) - t_size[1] - 3), (int(x1) + t_size[0], int(y1) + 3), (56, 56, 255), -1
            )
            cv2.putText(
                frame, label, (int(x1), int(y1) - 2), 0, 0.6, [255, 255, 255], thickness=1, lineType=cv2.LINE_AA
            )

           

 
        cv2.imshow(Path(source).stem, frame)
        video_writer.write(frame) 
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    video_writer.release()
    videocapture.release()
    cv2.destroyAllWindows()


 


def main():
    """Main function."""
    run()


if __name__ == "__main__": 
    main()