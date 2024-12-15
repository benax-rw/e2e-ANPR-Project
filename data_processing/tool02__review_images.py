import cv2
import os
import sys

def get_image_paths(directory):
    # Get all image file paths in the directory
    supported_formats = ('.png', '.jpg', '.jpeg', '.bmp', '.tiff', '.gif')
    return sorted([os.path.join(directory, f) for f in os.listdir(directory) if f.lower().endswith(supported_formats)])

def overlay_info_with_box(image, metadata, box_position=(10, 10), box_width=300, box_height=100, font_scale=0.6, color=(0, 255, 0), thickness=1):
    """
    Overlays information on the image with a black box as background.
    :param image: The image to annotate
    :param metadata: List of metadata strings
    :param box_position: Top-left corner of the box
    :param box_width: Width of the box
    :param box_height: Height of the box
    :param font_scale: Font scale for the text
    :param color: Color of the text (BGR format)
    :param thickness: Thickness of the text
    """
    x, y = box_position
    bottom_right = (x + box_width, y + box_height)
    
    # Draw the black box
    cv2.rectangle(image, (x, y), bottom_right, (0, 0, 0), -1)

    # Overlay the metadata text
    line_height = 20
    for i, line in enumerate(metadata):
        cv2.putText(image, line, (x + 10, y + 25 + i * line_height),
                    cv2.FONT_HERSHEY_SIMPLEX, font_scale, color, thickness, lineType=cv2.LINE_AA)

def display_image_with_info(image_path, index, total_images):
    """
    Displays the image with overlaid information such as name, dimensions, index, and instructions.
    """
    image = cv2.imread(image_path)
    if image is None:
        print(f"Error loading image: {image_path}")
        return None

    # Get image details
    height, width, channels = image.shape
    filename = os.path.basename(image_path)
    metadata = [
        f"File: {filename}",
        f"Dimensions: {width}x{height} px",
        f"Channels: {channels}",
        f"Image: {index + 1} / {total_images}"
    ]

    # Instructions for the user
    instructions = [
        "Actions:",
        "n: Next image   p: Previous image",
        "x: Delete image q: Quit"
    ]

    # Overlay metadata at the top-left
    overlay_info_with_box(image, metadata, box_position=(10, 10), box_width=380, box_height=100)
    
    # Overlay instructions at the bottom-left
    overlay_info_with_box(image, instructions, box_position=(10, height - 80), box_width=380, box_height=80)

    return image

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

        # Display the current image with metadata and instructions
        image = display_image_with_info(image_paths[index], index, len(image_paths))
        if image is None:
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