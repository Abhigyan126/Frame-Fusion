import cv2
from PIL import Image, ImageTk

class VideoStitcherOpenCV:
    def process_video(self, video_path, limit_frames, skip_frames):
        # Read the video
        cap = cv2.VideoCapture(video_path)

        # Initialize a list of images
        imgs = []

        # Read and process frames, skipping every few frames
        frame_count = 0
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            # Skip frames if necessary
            if frame_count % skip_frames != 0:
                frame_count += 1
                continue
            # Resize the frame
            frame = cv2.resize(frame, (0, 0), fx=0.4, fy=0.4)
            imgs.append(frame)
            frame_count += 1

            # Break the loop if enough frames have been captured
            if len(imgs) >= limit_frames:
                break

        # Release the video capture object
        cap.release()

        # Create Stitcher object
        stitcher = cv2.Stitcher_create()

        # Check if stitcher is successfully created
        if stitcher is None:
            print("Error: Failed to create stitcher object")
        else:
            # Stitch the images
            status, output = stitcher.stitch(imgs)

            # Check if stitching is successful
            if status != cv2.Stitcher_OK:
                print("Stitching isn't successful")
            else:
                # Save the stitched panorama as an image
                output_file_path = 'stitched_panorama.jpg'
                cv2.imwrite(output_file_path, output)
                print(f'Stitched panorama saved as {output_file_path}')
