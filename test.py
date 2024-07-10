import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw_mickey():
    fig, ax = plt.subplots()

    # Draw face
    face = patches.Circle((0.5, 0.5), 0.3, facecolor='black', edgecolor='black')
    ax.add_patch(face)

    # Draw ears
    left_ear = patches.Circle((0.2, 0.8), 0.15, facecolor='black', edgecolor='black')
    right_ear = patches.Circle((0.8, 0.8), 0.15, facecolor='black', edgecolor='black')
    ax.add_patch(left_ear)
    ax.add_patch(right_ear)

    ax.set_aspect('equal')
    plt.axis('off')
    plt.show()

if __name__ == "__main__":
    draw_mickey()
