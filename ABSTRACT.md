The authors of the **KFuji RGB-DS Database: Fuji Apple Multi-Modal Images for Fruit Detection with Color, Depth and Range-Corrected IR Data** introduce 967 multi-modal images capturing Fuji apples on trees using Microsoft Kinect v2. Each image incorporates information from three distinct modalities: color (RGB), depth (D), and range-corrected (IR) infrared intensity (S). The dataset includes manually annotated ground truth fruit locations, totaling 12,839 apples across all images.

The images, sized at 548 x 373 pixels, are saved in three different modalities:

- **RGBhr (High-Resolution Color Image):** Raw color images saved in 8-bit JPG files (*original_images*).
- **RGBp (Projected Color Image):** Projection of the color 3D point cloud onto the camera focal plane. Both RGBp and D-S modalities undergo the same procedure, enabling a comparison for fruit detection. (*cropped-*).
- **DS (Depth and Range-Corrected IR Image):** Projection of the range-corrected IR 3D point cloud onto the camera focal plane. The D channel corresponds to depth values, while the S channel corresponds to range-corrected IR intensity values. (*cropped-*).

<img src="https://github.com/dataset-ninja/kfuji/assets/78355358/c7e4f310-621b-4809-aadc-ba8d4a0fd4fd" alt="image" width="800">

<span style="font-size: smaller; font-style: italic;">Selection of 3 multi-modal images and the corresponding ground truth fruit locations (red bounding boxes). Each image column corresponds to a different image modality: RGB, S and D, respectively.</span>

The S and D data undergo normalization between 0 and 255, similar to RGB images, to achieve comparable mean and variance between channels, facilitating faster learning convergence for machine learning algorithms, including deep convolutional neural networks.

## Data Annotation

All images are manually annotated with rectangular bounding boxes, identifying a total of 12,839 apples across the dataset. The data acquisition occurred in a commercial Fuji apple orchard, utilizing two Microsoft Kinect v2 RGB-D sensors. The acquisition took place three weeks before harvesting, ensuring apples were at the 85 BBCH growth stage. Due to the depth sensor's sensitivity to direct sunlight, data acquisition occurred at night with artificial lighting.

## Data Processing

Data preprocessing involved various steps, including range correction of IR intensity data, projection of 3D point clouds onto the camera focal plane, geometric wrapping, registration with high-resolution RGB images, and image splitting to reduce the number of fruits per image.

<img src="https://github.com/dataset-ninja/kfuji/assets/78355358/a22e016c-1196-4641-83b0-68f64931aaa3" alt="image" width="800">

<span style="font-size: smaller; font-style: italic;">Data preparation outline.</span>

The above figure provides a visual representation of the data preparation steps, emphasizing the significance of overcoming IR signal attenuation and ensuring pixel-wise correspondence between different image modalities.