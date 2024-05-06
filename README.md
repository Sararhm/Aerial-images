# Image Scraping Script

This Python script allows you to gather images from Google Images based on specified class keywords and angle-related keywords. It utilizes web scraping techniques to search for images, extract their URLs, and save them to a local directory.

## Features

- Search for images of various classes (e.g., helicopters, aircraft, birds) from specific angles (e.g., top view, side view, front view).
- Customizable parameters such as the number of images per class and the save directory.
- Automatic creation of the save directory if it does not exist.
- Error handling for invalid URLs and missing directories.

## Prerequisites

- Python 3.x
- Required Python libraries: `requests`, `beautifulsoup4`

## Usage

1. Clone or download the repository to your local machine.
2. Install the required Python libraries using pip:

    ```bash
    pip install requests beautifulsoup4
    ```

3. Open the `scrape_images.py` file in a text editor.
4. Modify the `class_keywords`, `angle_keywords`, `num_images_per_class`, and `save_directory` variables according to your requirements.
5. Run the script:

    ```bash
    python scrape_images.py
    ```

6. The script will search for images, download them, and save them to the specified directory.

## Customization

- **class_keywords**: Specify the classes and their corresponding keywords for image search.
- **angle_keywords**: Define angle-related keywords for different perspectives.
- **num_images_per_class**: Set the number of images to download per class.
- **save_directory**: Choose the directory where the images will be saved.

## License

This project is licensed under the MIT License - see the [LICENSE][ChooseALicense.com](https://choosealicense.com/licenses/mit/)file for details.

## Acknowledgments

- This script was inspired by the need to gather diverse image datasets for machine learning projects.
- Special thanks to the authors of the `requests` and `beautifulsoup4` libraries for their contributions.
