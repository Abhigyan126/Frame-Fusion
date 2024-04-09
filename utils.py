import cv2
from PIL import Image, ImageTk

class VideoStitcherOpenCV:
    def process_video(self, video_path, limit_frames, skip_frames):
        cap = cv2.VideoCapture(video_path)

        imgs = []

        frame_count = 0
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            if frame_count % skip_frames != 0:
                frame_count += 1
                continue
   
            frame = cv2.resize(frame, (0, 0), fx=0.4, fy=0.4)
            imgs.append(frame)
            frame_count += 1

     
            if len(imgs) >= limit_frames:
                break

        cap.release()

        stitcher = cv2.Stitcher_create()

        if stitcher is None:
            print("Error: Failed to create stitcher object")
        else:
            status, output = stitcher.stitch(imgs)

            if status != cv2.Stitcher_OK:
                print("Stitching isn't successful")
            else:
                output_file_path = 'stitched_panorama.jpg'
                cv2.imwrite(output_file_path, output)
                print(f'Stitched panorama saved as {output_file_path}')
