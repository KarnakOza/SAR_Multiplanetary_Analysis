# Correct RDN file paths
hdr = HDR_FILE_PATH
img = HDR_FILE_PATH

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
