# Load the OBS data
hdr_obs = HDR_FILE_PATH
img_obs = IMG_FILE_PATH
obs_cube = io.envi.open(hdr_obs, img_obs)

print("OBS Shape:", obs_cube.shape)

# Read bands
slope = obs_cube.read_band(7)    # Band 8: Slope
aspect = obs_cube.read_band(8)   # Band 9: Aspect
cos_i = obs_cube.read_band(9)    # Band 10: Cos(i)

# -----------------------------
# 🔸 1. Curvature (second derivative using Laplacian)
curvature = gaussian_laplace(slope, sigma=1)

# 🔸 2. Roughness (standard deviation over 3x3 window)
roughness = generic_filter(slope, np.std, size=3)

# -----------------------------
# 🔸 3. Display All Maps
fig, axs = plt.subplots(1, 3, figsize=(18, 6))

axs[0].imshow(curvature, cmap='coolwarm')
axs[0].set_title("Curvature (Laplacian of Slope)")
axs[0].axis('off')

axs[1].imshow(roughness, cmap='viridis')
axs[1].set_title("Surface Roughness (Std Dev of Slope)")
axs[1].axis('off')

im = axs[2].imshow(cos_i, cmap='inferno')
axs[2].set_title("Cosine of Incidence Angle (Band 10)")
axs[2].axis('off')

fig.colorbar(im, ax=axs.ravel().tolist(), shrink=0.6)
fig, axs = plt.subplots(1, 3, figsize=(18, 6), constrained_layout=True)


plt.show()
