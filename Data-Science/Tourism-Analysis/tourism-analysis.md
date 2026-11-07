# Tourism Data Analysis and Recommendation Engine

Author: Gresa Hisa

---

## Overview

Analysis of Indonesian tourism data covering visitor demographics, attraction categories, rating patterns, and a content-based recommendation engine. The goal was to understand visitor behavior and build a system that recommends similar tourist destinations based on user ratings.

**Datasets used:**

| File | Description |
|---|---|
| user.csv | Visitor demographics: User_Id, Location, Age |
| tourism_rating.csv | User ratings: User_Id, Place_Id, Place_Ratings (1-5) |
| tourism_with_id.xlsx | Place metadata: name, category, city, price, rating, coordinates |

---

## Exploratory Data Analysis

### Age Distribution

The majority of visitors fall between 20 and 40 years old. This aligns with the demographic most likely to travel for leisure. The tourism market is largely driven by young adults and early professionals.

### Top User Locations

The highest number of ratings came from visitors based in:

1. Yogyakarta
2. Bandung
3. Jakarta
4. Semarang
5. Surabaya

Strong domestic tourism concentrated in major urban centers.

### Tourist Place Categories

| Category | Description |
|---|---|
| Taman Hiburan | Amusement Parks |
| Budaya | Cultural Heritage |
| Cagar Alam | Natural Reserve |
| Bahari | Marine Attractions |
| Tempat Ibadah | Religious Sites |
| Pusat Perbelanjaan | Shopping Centers |

The most common categories are Taman Hiburan, Budaya, and Cagar Alam — reflecting Indonesia's cultural and natural diversity.

### Cities with Most Attractions

Yogyakarta, Bandung, and Jakarta dominate as tourism hubs with the highest number of listed attractions.

---

## Top Rated Tourist Spots

Average rating calculated per place across all user ratings. Top results:

- Keraton Surabaya
- Puncak Gunung Api Purba - Nglanggeran
- Kampung Cina

---

## Recommendation Engine

Two approaches implemented:

### Pearson Correlation

Built a user-place pivot table, then computed Pearson correlation between places using a minimum of 20 shared ratings. Places with high correlation scores are considered similar.

```python
pivot = merged.pivot_table(index='User_Id', columns='Place_Name', values='Place_Ratings')
similarity = pivot.corr(method='pearson', min_periods=20)

def recommend(place_name, n=5):
    sim_scores = similarity[place_name].dropna().sort_values(ascending=False)
    return sim_scores.iloc[1:n+1]
```

### Cosine Similarity

Filled missing ratings with 0, then computed cosine similarity between place vectors using scikit-learn.

```python
from sklearn.metrics.pairwise import cosine_similarity

pivot_filled = pivot.fillna(0)
cosine_sim = cosine_similarity(pivot_filled.T)
cosine_sim_df = pd.DataFrame(cosine_sim, index=pivot_filled.columns, columns=pivot_filled.columns)

def recommend_cosine(place_name, n=5):
    sim_scores = cosine_sim_df[place_name].sort_values(ascending=False)
    return sim_scores.iloc[1:n+1]
```

Both methods allow querying by place name and returning the top N most similar destinations.

---

## Tools and Stack

- Python, Pandas, NumPy
- Matplotlib for visualization
- scikit-learn for cosine similarity
- Google Colab for development and execution

---

## Files

| File | Description |
|---|---|
| tourism-analysis.ipynb | Full notebook with code, outputs, and visualizations |
| user.csv | Visitor demographics dataset |
| tourism_rating.csv | User-place rating dataset |
| tourism_with_id.xlsx | Tourist place metadata |
