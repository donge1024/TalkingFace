import numpy as np
import cv2
import torch
import audio

class TemporalConsistency:
    def __init__(self, audio, video_generated, video_input, video_ground_truth):
        
        self.audio = audio
        self.video_generated = video_generated
        self.video_input = video_input
        self.video_ground_truth = video_ground_truth

    def forced_alignment(self):
        
        phoneme_sequences = []
       
        for i in range(len(self.audio)):
            phoneme_sequences.append("p_" + str(i + 1))
        return phoneme_sequences

    def construct_temporal_module(self, phoneme_sequences):
       
        temporal_modules = {}
        
        for i, phoneme in enumerate(phoneme_sequences):
            temporal_module = []
          
            for j in range(len(self.video_generated)):
                temporal_module.append("d_" + str(j + 1))
            temporal_modules[phoneme] = temporal_module
        return temporal_modules

    def calculate_lip_loss(self, phoneme, temporal_module):
        
        lip_loss = sum(temporal_module)  
        return lip_loss

    def update_lip_weight(self, phoneme, temporal_module):
      
        lip_similarity = temporal_module  
        delta_max = max(lip_similarity)
        delta_min = min(lip_similarity)
        if delta_min < delta_max:
            w_lip = delta_max
        else:
            w_lip = sum(lip_similarity) / len(lip_similarity)
        return w_lip


if __name__ == '__main__':
    video_path = "video.mp4" 
    audio_path = "audio.wav"  