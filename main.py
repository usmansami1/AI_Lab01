import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
import matplotlib.colors as mcolors

def generate_dragon_path(order=14, length=1.0):
    """Generates 2D coordinates for a Heighway Dragon curve via rotation mapping."""
    pts = np.array([0 + 0j, length + 0j], dtype=complex)
    for _ in range(order):
        # Rotate around the end-point by 90 degrees
        tip = pts[-1]
        next_pts = (pts[:-1] - tip) * 1j + tip
        pts = np.concatenate([pts, next_pts[::-1]])
    return pts.real, pts.imag

def build_inverted_tree(x, y, length, angle, depth, segments, depths, max_depth):
    """Recursively computes line segments for an upside-down fractal canopy."""
    if depth == 0 or length < 0.4:
        return
    
    rad = np.radians(angle)
    x_end = x + length * np.cos(rad)
    y_end = y + length * np.sin(rad)
    
    segments.append([(x, y), (x_end, y_end)])
    depths.append(depth)
    
    # Branch downwards with tapering angle spread
    spread = 28 + (max_depth - depth) * 2.2
    scale = 0.74
    
    build_inverted_tree(x_end, y_end, length * scale, angle - spread, depth - 1, segments, depths, max_depth)
    build_inverted_tree(x_end, y_end, length * scale, angle + spread, depth - 1, segments, depths, max_depth)
    if depth > 4:
        # Central filling sub-branches
        build_inverted_tree(x_end, y_end, length * (scale * 0.8), angle, depth - 2, segments, depths, max_depth)

# ---------------- Canvas Setup ----------------
fig, ax = plt.subplots(figsize=(12, 18), facecolor='black')
ax.set_facecolor('black')

# ---------------- Part 1: Inverted Fractal Tree (Bottom) ----------------
tree_segments = []
tree_depths = []
max_d = 10

# Left main trunk & branch system (angle points downwards: -90 deg)
build_inverted_tree(x=0, y=-50, length=75, angle=-125, depth=max_d, 
                    segments=tree_segments, depths=tree_depths, max_depth=max_d)
# Right main trunk & branch system
build_inverted_tree(x=0, y=-50, length=75, angle=-55, depth=max_d, 
                    segments=tree_segments, depths=tree_depths, max_depth=max_d)

# Central trunk downward extension
tree_segments.append([(0, 40), (0, -50)])
tree_depths.append(max_d)

# Colorize tree branches across horizontal spread (rainbow gradient)
tree_segs_arr = np.array(tree_segments)
x_coords = tree_segs_arr[:, :, 0].mean(axis=1)
norm_x = (x_coords - x_coords.min()) / (x_coords.max() - x_coords.min() + 1e-5)
tree_colors = plt.cm.turbo(norm_x)

# Thickness decreases with recursion depth
tree_depths = np.array(tree_depths)
linewidths = 0.8 + 5.5 * (tree_depths / max_d)**1.8

tree_collection = LineCollection(tree_segments, colors=tree_colors, linewidths=linewidths, capstyle='round')
ax.add_collection(tree_collection)

# ---------------- Part 2: Dragon Curves (Top / Neckline) ----------------
dx, dy = generate_dragon_path(order=15, length=0.012)

# Center and orient base curve
dx = dx - dx[0]
dy = dy - dy[0]

# Left branch curling toward collar
rad_left = np.radians(110)
rx_l = dx * np.cos(rad_left) - dy * np.sin(rad_left)
ry_l = dx * np.sin(rad_left) + dy * np.cos(rad_left)

scale_factor = 2300
shift_x = 0
shift_y = 40

dragon_left_x = rx_l * scale_factor + shift_x
dragon_left_y = ry_l * scale_factor + shift_y

# Right branch mirrored horizontally
dragon_right_x = -dragon_left_x
dragon_right_y = dragon_left_y

# Plot white dragon curves
ax.plot(dragon_left_x, dragon_left_y, color='white', lw=0.9, alpha=0.92)
ax.plot(dragon_right_x, dragon_right_y, color='white', lw=0.9, alpha=0.92)

# Secondary shoulder tendrils
ax.plot(dragon_left_x * 0.65 - 90, dragon_left_y * 0.65 + 110, color='white', lw=0.6, alpha=0.75)
ax.plot(dragon_right_x * 0.65 + 90, dragon_right_y * 0.65 + 110, color='white', lw=0.6, alpha=0.75)

# ---------------- Boundaries & Export ----------------
ax.set_xlim(-260, 260)
ax.set_ylim(-260, 280)
ax.set_aspect('equal')
ax.axis('off')

plt.subplots_adjust(left=0, right=1, top=1, bottom=0)

# Export at 300 DPI for high-resolution apparel printing
plt.savefig("fractal_tshirt_print.png", dpi=300, facecolor='black', edgecolor='none')
plt.show()