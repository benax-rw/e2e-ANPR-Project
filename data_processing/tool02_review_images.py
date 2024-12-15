import cv2
import os
import sys

def get_image_paths(directory):
    # Get all image file paths in the directory
    supported_formats = ('.png', '.jpg', '.jpeg', '.bmp', '.tiff', '.gif')
    return sorted([os.path.join(directory, f) for f in os.listdir(directory) if f.lower().endswith(supported_formats)])

def image_viewer(directory):
    # Get the list of images
    image_paths = get_image_paths(directory)
    if not image_paths:
        print("No images found in the directory.")
        return
    
    index = 0
    while True:
        # Check if the list of images is empty
        if not image_paths:
            print("No more images left.")
            break

        # Read and display the current image
        image = cv2.imread(image_paths[index])
        if image is None:
            print(f"Error loading image: {image_paths[index]}")
            break

        cv2.imshow("Image Viewer", image)
        
        # Wait for a key press
        key = cv2.waitKey(0) & 0xFF
        
        if key == ord('q') or key == 27:  # Quit on 'q' or 'ESC'
            print("Exiting...")
            break
        elif key == ord('x'):  # Delete the current image
            print(f"Deleting: {image_paths[index]}")
            os.remove(image_paths[index])
            del image_paths[index]
            if not image_paths:
                print("No more images left.")
                break
            index = index % len(image_paths)  # Stay at the current index, moving to the next image if available
        elif key == ord('p'):  # Previous image
            index = (index - 1) % len(image_paths)
        elif key == ord('n'):  # Next image
            index = (index + 1) % len(image_paths)

    cv2.destroyAllWindows()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python tool02_review_images.py <directory_path>")
        sys.exit(1)

    directory = sys.argv[1]
    if not os.path.isdir(directory):
        print("The provided path is not a directory.")
        sys.exit(1)

    image_viewer(directory)