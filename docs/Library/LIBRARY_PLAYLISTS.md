
# Library Playlists Data Definition

This data dictionary describes the fields in the Apple Music Library Playlists.json data. There are 106 rows and 14 columns. 

## Library Playlists Data

| Column Name | Data Type | Description | Example Value |
|-------------|-----------|-------------|---------------|
| `Container Type` | String | Playlist, Subscribed Playlist, Favorites Playlist | Playlist |
| `Container Identifier` | Integer | Unique Identifier for Playlist | 256001793 |
| `Title` | String | Title of Playlist | DHH |
| `Playlist Item Identifiers` | String | Track Identifiers for songs in the playlist | [182862890, 182860290, 182858018, 182858766, 182859798, 182859830, 182860082, 182862898, 182870570, 182870582, 182870822, 182870834, 182870838, 182871042, 182871050, 182871578, 182872106, 182872114, 182872110, 182880030, 182883862] |
| `Favorite Status - Playlist` | String | If the playlist was favorited | nan |
| `Favorite Date - Playlist` | String | Timestamp of when the playlist was favorited | nan |
| `Added Date` | Datetime | Date when playlist was added | 2022-04-20T10:54:22Z |
| `Name or Description Modified Date` | Datetime | Date when Name or Description was modified | 2022-04-20T10:54:22Z |
| `Playlist Items Modified Date` | Datetime | Date when playlist item was modified | 2023-02-28T14:23:11Z |
| `Public Playlist Identifier` | String | Identifier for playlist that are public | pl.u-d2b0kMWtM0jVEv0 |
| `Playlist Is Shared` | Boolean | If the playlist is shared | True |
| `Playlist Previously Shared` | Boolean | If the playlist was previously shared | True |
| `Description` | String | Description of the Playlist | Desi Hip-Hop |
| `Available On Apple Music Profile` | Boolean | Is visible on Apple Music Profile | True |
