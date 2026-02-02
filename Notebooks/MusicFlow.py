# %%
import pandas as pd
import polars as pl
import os

# %%
DATA_PATH = os.path.join('../Apple Music Activity')
FILE_NAME = 'Apple Music - Play History Daily Tracks.csv'

# %%
lf = (
    pl.scan_csv(os.path.join(DATA_PATH, FILE_NAME))
    .with_columns(
        pl.col("Date Played")
        .cast(pl.Utf8)
        .str.strptime(pl.Date, format="%Y%m%d")
        .alias("date_played"),
        (pl.col("Play Duration Milliseconds")/(1000*60*60))
        .alias("play_duration_hours"),
        (pl.col("Play Duration Milliseconds")/(1000*60))
        .alias("play_duration_minutes")
    )
)

# %%
lf

# %%
pl.scan_csv(os.path.join(DATA_PATH, FILE_NAME)).schema

# %%
lf_2025 = lf.filter(pl.col("date_played").dt.year() == 2025)

# %%
df_2025 = lf_2025.collect()

# %%
df_2025

# %%
# use the collected (eager) DataFrame and Polars group_by/agg syntax
top_songs_2025 = (
    df_2025
    .group_by('Track Description')
    .agg([
        pl.col('play_duration_minutes').sum().alias("total_minutes"),
        pl.col('Play Count').sum().alias('total_play_count')
    ])
    .sort('total_minutes', descending=True)
    .limit(10)
)

# %%
top_songs_2025

# %%
# top = top_songs_2025.collect()

# %%
print (top_songs_2025)

# %% [markdown]
# ### April 2025

# %%
lf_apr = (
    pl.scan_csv(os.path.join(DATA_PATH, 'Apple Music - Play History Daily Tracks April 2025.csv'))
    .with_columns(
        (pl.col("Play Duration Milliseconds")/(1000*60*60))
        .alias("play_duration_hours"),
        (pl.col("Play Duration Milliseconds")/(1000*60))
        .alias("play_duration_minutes")
    )
)

# %%
lf_apr

# %%
top_song_apr = (
    lf_apr
    .group_by('Track Description')
    .agg([
        # pl.col('play_duration_minutes').sum().alias('total_minutes'),
        pl.col('Play Count').sum().alias('total_plays')
    ])
    .sort('total_plays', descending=True)
    .limit(11)
)

# %%
top_song_apr.collect()

# %%
daily_hours = (
    lf_2025
    .group_by('Date Played')
    .agg([
        pl.col('play_duration_hours').sum().alias('total_hours')
    ])
    .sort('Date Played')
)

# %%
print (daily_hours.collect())

# %%



