from sahi import AutoDetectionModel
from sahi.predict import get_sliced_prediction

class YOLODetector():

    def __init__(self, model_type, model_weights, device ): 
        
        self.detection_model = AutoDetectionModel.from_pretrained(
            model_type=model_type, 
            model_path=model_weights,
            confidence_threshold=0.3,
            device=device 
        )

        self.slice_height = 640
        self.slice_width = 640
        self.overlap_height_ratio = 0.02
        self.overlap_width_ratio = 0.02


    def setSlice(self, height, width):
        self.slice_height = height
        self.slice_width = width
    

    def setOverlap(self, height_ratio, width_ratio):
        self.overlap_height_ratio = height_ratio
        self.overlap_width_ratio = width_ratio


    def predict_frame(self, frame):

        results=get_sliced_prediction(frame,
                                self.detection_model,
                                slice_height=self.slice_height,
                                slice_width=self.slice_width,
                                overlap_height_ratio=self.overlap_height_ratio,
                                overlap_width_ratio=self.overlap_width_ratio)
        
        return results.object_prediction_list

        

        


