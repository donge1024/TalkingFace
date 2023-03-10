# Talking Face
This paper proposes a novel Talking Face model, which is based on time-spatial consistency, can adapt to multi-pose and multi-angle input faces, and generate high-quality lip-synced talking face videos. Specifically, for time consistency, a continuous frame sequence of the same phoneme is used as a time-continuous module to constrain the mouth shape changes of the same phoneme to improve the accuracy of audio to lips. For spatial consistency, an adaptive face encoder-decoder network is constructed by aligning the spatial positions of detected faces to remove visual artifacts from video frames.
![overview](https://user-images.githubusercontent.com/114487375/209749662-98aaffc1-09ed-4e0f-aa91-cdf87006c3f6.jpg)

# Video Samples
Video [samples](demo) generated by this implementation can be found above.

# Highlights
Time consistency (TC) takes the continuous frame sequence of the same phoneme as a time-continuous module to constrain the lip-shape changes of the same phoneme. It improves the accuracy of audio-driven lips.

Spatial consistency (SC) constructing an adaptive face encoder-decoder network by aligning the spatial positions of detected faces can effectively eliminate visual artifacts.

# Evaluation
Regarding the consistency of judging lip sync, we use LSE-D (Lip Sync Error - Distance) and LSE-C (Lip Sync Error - Confidence) to indicate the correlation of audio and video. The lower the LSE-D, the better, and the higher the LSE-C, the better.

Regarding the evaluation of the generated quality of video frames, we use methods including FID (Fréchet Inception Distance) and SSIM (Structural SIMilarity), which represent the similarity of generated images to real images. The smaller the FID value, the better, and the larger the SSIM, the better.
