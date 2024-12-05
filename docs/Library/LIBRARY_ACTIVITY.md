
# Library Activity Data Definition

This data dictionary describes the fields in the Apple Music Library Activity.json data. There are 6072 rows and 29 columns. 

## Library Activity Data

| Column Name | Data Type | Description | Example Value |
|-------------|-----------|-------------|---------------|
| `Transaction Type` | String |  | startPlaylistCollaboration |
| `Transaction Identifier` | Integer |  | 20001175 |
| `Transaction Date` | Datetime |  | 2023-11-22T01:26:53Z |
| `UserAgent` | String |  | MZDaap |
| `Subscription Start Date` | String |  | nan |
| `Subscription Type` | String |  | nan |
| `User` | String |  | nan |
| `Country` | String |  | USA |
| `Language` | String |  | nan |
| `Tracks` | String |  | nan |
| `Public Playlist Identifier` | String |  | pl.u-e98lky5TzxJLqDx |
| `Track Identifiers` | String |  | nan |
| `Playlist` | String |  | nan |
| `Playlist Identifier` | Float |  | nan |
| `Playlist Item Identifiers Appended` | String |  | nan |
| `Playlists` | String |  | nan |
| `Subscription End Date` | String |  | nan |
| `Subscription Types` | String |  | nan |
| `Modified Container Identifiers` | String |  | nan |
| `Playlist Identifiers Removed From Profile` | String |  | nan |
| `Playlist Identifiers Set From Profile` | String |  | nan |
| `Playlist Identifiers Added From Profile` | String |  | nan |
| `Artist Catalog Identifier` | String |  | nan |
| `Favorite Type` | String |  | nan |
| `Liked Status` | String |  | nan |
| `Artists` | String |  | nan |
| `Collaboration Identifier` | String |  | pl.c-e98lky5TzxJLqDx@1 |
| `Source Playlist Identifier` | Float |  | 256002053.0 |
| `Collaboration Playlist Identifier` | Float |  | 256004613.0 |

## Data Description

- **Transaction Type:** 

| Value | Count |
|-------|-------|
| updateItems | 2358 |
| addItems | 1835 |
| deleteItems | 678 |
| appendContainerItems | 486 |
| updateContainer | 368 |
| updateUser | 108 |
| subscribeToPlaylist | 51 |
| updateArtistAdamIdsLikedStatus | 50 |
| addContainer | 49 |
| updateArtists | 34 |
| deleteContainer | 24 |
| updateFavoriteArtistAdamIds | 13 |
| addContainers | 5 |
| setProfileContainerIds | 4 |
| optInUser | 3 |
| backfillAlbumArtists | 2 |
| optOutUser | 2 |
| startPlaylistCollaboration | 2 |

