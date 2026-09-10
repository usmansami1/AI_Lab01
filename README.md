# Designing Using Fractals

A Python-based generative-art project that turns mathematical fractals into a bold T-shirt design. The artwork combines a colourful, mirrored fractal tree with white Dragon-curve patterns on a black background, then exports a high-resolution image suitable for apparel printing.

## Fractals Implemented

- **Symmetric inverted fractal tree** — a recursive branching system that creates the colourful lower canopy. Two mirrored main branches and a central trunk form the balanced tree structure.
- **Heighway Dragon curve** — an iterative, self-similar curve used for the white geometric patterns around the neckline and shoulders. The curve is mirrored to preserve the design's symmetry.

## Tools, Language, and Libraries

- **Language:** Python 3
- **Numerical computation:** NumPy
- **Visualisation and image export:** Matplotlib
  - `matplotlib.pyplot`
  - `matplotlib.collections.LineCollection`
  - `matplotlib.colors`

## Setup and Run

1. Install Python 3.9 or later.
2. Install the required libraries:

   ```bash
   pip install numpy matplotlib
   ```

3. Save the project code in a file such as `fractal_tshirt.py`.
4. Run the program:

   ```bash
   python fractal_tshirt.py
   ```

5. The script opens the generated design and saves a 300 DPI image named `fractal_tshirt_print.png` in the same folder.

## Output

### Generated fractal artwork

![Generated fractal artwork](/fractal_tshirt_print.png)

### T-shirt design mock-up

![Fractal T-shirt mock-up](/Gemini_Generated_Image_dxuzupdxuzupdxuz.jpg)

## Student Details

- **Student name:** Usman Sami
- **Registration number:** 545491

