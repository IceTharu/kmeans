# kmeans
A Kmeans algorithm created for Alpaca Japan. All functions used are in the file kmeans_functions.py, while two test cases are in the file kmeans.py.

## With 4 normally distributed point distributions randomly generated.
- After initializing 4 normal distributions with 4 randomly generated cluster centres, this was the output result. Needing only 3 iterations.

- The opaque stars show initial cluster centres. Some cluster centres didn't move a lot from their initial starting position.

![Kmeans output with 4 random clusters created and 4 random initial cluster centres.](https://github.com/IceTharu/kmeans/blob/main/fig1.png
)

## With a random number generator.
- Using a random number generator for both generating the point distribution and cluster centres. This one converged after 6 iterations.

- The opaque stars show initial cluster centres. Some cluster centres didn't move a lot from their initial starting position.
![Kmeans output with a completely random distribution and 4 random initial cluster centres.](https://github.com/IceTharu/kmeans/blob/main/fig2.png
)


