# Correct RDN file paths
hdr = HDR_FILE_PATH
img = IMG_FILE_PATH

# Load image
m3_data = io.envi.open(hdr, image=img)
cube = m3_data.load()

# Confirm shape
print("✅ Loaded cube shape:", cube.shape)  # Expecting (1182, 304, 85)


transposed_cube = np.transpose(cube, (1, 2, 0))
#Assuming 'cube' is your data with shape (1182, 304, 3)
#Transpose the data to shape (304, 3, 1182)
band_index = 45
if band_index < transposed_cube.shape[2]:
    band_image = transposed_cube[:, :, band_index]
    plt.imshow(band_image, cmap='gray')
    plt.title(f"Band {band_index}")
    plt.axis('off')
    plt.show()
else:
    print(f"Band index {band_index} is out of range.")


##For Band Depth Index analysis 
def compute_band_depth(cube, center_band, left_band, right_band):
    # Ensure band indices are within range
    if max(center_band, left_band, right_band) >= cube.shape[0]:
        raise IndexError("Band index out of range.")
    
    left = cube[left_band, :, :]
    center = cube[center_band, :, :]
    right = cube[right_band, :, :]
    
    continuum = (left + right) / 2.0
    bdi = 1 - (center / continuum)
    return np.nan_to_num(bdi)

# Example usage:
bdi_map = compute_band_depth(cube, center_band=45, left_band=40, right_band=50)

plt.imshow(bdi_map, cmap='viridis')
plt.title("Band Depth Index (950 nm)")
plt.axis('off')
plt.show()


###FOR LUNAR SLOPE MAP
# Paths to the HDR and IMG
hdr_path = HDR_FILE_PATH
img_path = IMG_FILE_PATH
# Load the file
obs_cube = io.envi.open(hdr_path, img_path)

print("Shape:", obs_cube.shape)
print("Band Names:", obs_cube.metadata.get('band names', 'Not found'))

# Example: Display the Slope band (Band 7 or 8 depending on 0-index)
slope_band = obs_cube.read_band(7)  # Band 8 is usually slope

plt.figure(figsize=(6, 6))
plt.imshow(slope_band, cmap='terrain')
plt.colorbar(label='Slope (degrees?)')
plt.title("Lunar Slope Map (from OBS)")
plt.axis('off')
plt.show()
