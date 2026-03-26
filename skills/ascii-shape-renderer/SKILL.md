
---
name: ascii-shape-renderer
description: Converts images to high-quality ASCII art using Alex Harri's shape-based 6D vector rendering technique instead of pixel lightness. Use when user asks to "convert image to ascii", "make ascii art", "generate shape-based ascii", "render ascii", or "create ascii art".
---

# ASCII Shape-Based Renderer

## Overview
Generate high-quality, anti-aliased ASCII art from images. Instead of using traditional nearest-neighbor lightness (which causes blurry edges), implement Alex Harri's approach: map the visual weight of image cells into 6-dimensional shape vectors and match them to character geometries using Euclidean distance or k-d trees.

## Step 1: Context & Dependencies

First, verify the environment has the required libraries and locate potential input images:

```bash
# Check for required python packages
python -c "import PIL, numpy" 2>/dev/null || echo "MISSING_DEPS: pip install Pillow numpy"

# Find available images in the current directory
find . -maxdepth 1 -type f \( -iname \*.jpg -o -iname \*.jpeg -o -iname \*.png \) | head -n 5 || echo "No images found."
```

If dependencies are missing, install them. If no image was specified by the user, ask which of the found images to use.

## Step 2: Implement the Harri Algorithm

If a shape-based ASCII script does not exist in the workspace, create `shape_ascii.py`. You must strictly follow these architectural rules to replicate the Harri method:

1. **The 6D Vector Structure:** Divide a standard terminal character bounding box (aspect ratio ~1:2) into 6 regions: `[Top-Left, Top-Right, Mid-Left, Mid-Right, Bottom-Left, Bottom-Right]`.
2. **Character Pre-computation:** Build a dictionary of allowed ASCII characters mapping to their specific 6D visual weight vectors. 
3. **Image Sampling:** Divide the target image into a grid. For each cell, calculate its 6D shape vector based on the underlying pixel densities.
4. **Contrast Enhancement (Crucial):**
   - *Global Exponent:* Apply an exponent to the 6D cell vectors to exaggerate contrast.
   - *Directional Sampling:* Sample a slight margin *outside* the grid cell to detect continuing geometric boundaries (prevents staircasing on diagonals).
5. **Character Matching:** Calculate the Euclidean distance between the grid cell's 6D vector and the character vectors to find the best geometric match.

## Step 3: Execution

Run the script on the target image. Default to an output width of 100 characters unless the user specified a different size.

```bash
# Replace $IMAGE_FILE with the actual filename
python shape_ascii.py --input "$IMAGE_FILE" --output ascii_output.txt --width 100
```

Confirm the file was generated and preview the output:

```bash
echo "ASCII art written: $(wc -l < ascii_output.txt) lines"
head -n 25 ascii_output.txt
```

## Step 4: Quality Verification

Review the previewed output snippet against these criteria:
- [ ] Are structural directional characters (`/`, `\`, `_`, `|`, `-`) heavily utilized on edges?
- [ ] Is the output free from looking like a traditional "density blob" (mostly `#`, `@`, `%` clustered together)?
- [ ] Does the aspect ratio look correct?

