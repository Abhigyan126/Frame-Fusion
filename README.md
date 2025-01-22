# Frame-Fusion
 Utilizing image stitching techniques to merge frames from a video into a cohesive image, effectively encapsulating the entire video in a single panoramic representation.

 ## Flow Chart
```mermaid
flowchart TB
    Upload["Upload Video Button"] --> VideoCapture["Video Capture\n(OpenCV)"]
    
    subgraph UI["Tkinter Interface"]
        VideoCapture --> Preview["Preview Window"]
        Controls["Control Panel"]
        Controls --> |"Play/Pause"| Preview
        Controls --> |"Limit Frames"| Process
        Controls --> |"Skip Frames"| Process
    end
    
    subgraph Processing["Video Processing"]
        Process["Process Video"] --> Stitcher["OpenCV Stitcher"]
        Stitcher --> Panorama["Panorama Image"]
    end
    
    Preview --> Process
    Panorama --> Save["Save Panorama"]
 ```
