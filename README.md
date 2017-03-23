## spotifav

### Relevant blog post: [Dimitris Spathis](https://medium.com/p/fe50c94b8af3)

The idea is simple. After I found out that I have access to some interesting features (danceability, loudness etc) on my Spotify playlists, I decided to crunch some numbers in order to discover some patterns of my favorite songs. For reality check, I compared my songs with the [Today's Top Hits](https://open.spotify.com/user/spotify/playlist/5FJXhjdILmRA2z5bvz4nzf) playlist, leading to some fun observations. You can get the aforementioned features for your playlists by this clever [Echonest app](http://static.echonest.com/SortYourMusic/).

This repository contains the necessary code, data, and Jupyter Notebooks to estimate histograms, correlation heatmaps, dimensionality reduction and visualization with t-SNE and outlier detection with One-Class SVM visualized in contour plots. 

To run you should set up the usual sci-Python gang: Matplotlib, Numpy, Pandas, Seaborn and Sklearn. 

### Steps
1. Log in to [Echonest app](http://static.echonest.com/SortYourMusic/) and choose your playlist.
2. Copy the table to a spreadsheet.
3. Save it as csv.
4. Run ``spotify_favorites.py`` to find correlations and estimate t-SNE and SVM
5. Comment out [line 199](https://github.com/nn1k1kvn/spotifav/blob/master/spotify_favorites.py#L199) to draw a projection of a specific artist.
6. Run ``today_top_hits.py`` to compare step's 4. data with today top hits.

As an alternative, you can query your playlists through the [Spotify API](https://developer.spotify.com/web-api/get-audio-features/), getting access to even more features. 

### Histograms & Correlations

| Histograms of my playlist's features | Compared to the most popular Spotify playlist |
| ------------- | ------------- |
| ![PICTURE](https://github.com/nn1k1kvn/spotifav/blob/master/Figures/histograms.png)  | ![PICTURE](https://github.com/nn1k1kvn/spotifav/blob/master/Figures/histograms_comparison.png)  |

|   |   | 
| ------------- | ------------- |
| ![PICTURE](https://github.com/nn1k1kvn/spotifav/blob/master/Figures/acousticness_loudness_corr.png)  | ![PICTURE](https://github.com/nn1k1kvn/spotifav/blob/master/Figures/danceability_valence_corr.png)  |

|   |   | 
| ------------- | ------------- |
| ![PICTURE](https://github.com/nn1k1kvn/spotifav/blob/master/Figures/energy_acousticness_corr.png)  | ![PICTURE](https://github.com/nn1k1kvn/spotifav/blob/master/Figures/energy_loudness_correlation.png)  |

|   |   | 
| ------------- | ------------- | 
| ![PICTURE](https://github.com/nn1k1kvn/spotifav/blob/master/Figures/energy_valence_corr.png)  | ![PICTURE](https://github.com/nn1k1kvn/spotifav/blob/master/Figures/popularity_energy_corr.png)  |

### t-SNE Dimensionality Reduction

| Cléa Vincent songs | Eurythmics songs |
| ------------- | ------------- |
| ![PICTURE](https://github.com/nn1k1kvn/spotifav/blob/master/Figures/tsne_clea_vincent.png)  | ![PICTURE](https://github.com/nn1k1kvn/spotifav/blob/master/Figures/tsne_eurythmics.png)  |

### Outlier Detection 

| Contour plot of fitted one-class SVM  |
| -------------  |
| ![PICTURE](https://github.com/nn1k1kvn/spotifav/blob/master/Figures/one_class_plot.png)  |
