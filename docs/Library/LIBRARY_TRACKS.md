# Library Tracks Data Definition

This data dictionary describes the fields in the Apple Music Library Tracks.json data. There are 2761 rows and 52 columns. 

## Library Track Data

| Column Name | Data Type | Description | Example Value |
|-------------|-----------|-------------|---------------|
| `Content Type` | String | Categorical variable showing the type of Content (Song or Music Video) | Song |
| `Track Identifier` | Integer | Unique 9 digit Track Identifier | 182889262 |
| `Title` | String | Title of song | HYAENA |
| `Sort Name` | String | Title of song used for sorting (Articles like The and A are skipped for this title) | HYAENA |
| `Artist` | String | Artist Name | Travis Scott |
| `Sort Artist` | String | Artist Name used for sorting | Travis Scott |
| `Composer` | String | Composers of the tracks | Jacques Webster, Ebony Oshunrinde, MIKE DEAN, Noah Goldstein, Jahaan Sweet, George Clinton, Edward Hazel, Derek Shulman, Ray Shulman, Andy Votel & Kerry Minnear |
| `Is Part of Compilation` | Boolean | Is part of compilation or not | False |
| `Album` | String | Album of the song | UTOPIA |
| `Sort Album` | String | Album name used for sorting | UTOPIA |
| `Album Artist` | String | Album Artist denotes the main performer associated with an entire album | Travis Scott |
| `Genre` | String | Genre of the song | Hip-Hop/Rap |
| `Track Year` | Float | Year the track was released | 2023.0 |
| `Track Number On Album` | Float | The position of Track in the album | 1.0 |
| `Track Count On Album` | Float | Total number of Tracks in the album | 19.0 |
| `Disc Number Of Album` | Float | Disc number of the album | 1.0 |
| `Disc Count Of Album` | Float | Total disc count of the album | 1.0 |
| `Track Duration` | Float | Duration of song in milliseconds | 222085.0 |
| `Track Play Count` | Integer | Number of times the track is played | 44 |
| `Date Added To Library` | Datetime | Timestamp of when the song was added to library | 2023-07-28T05:04:34Z |
| `Date Added To iCloud Music Library` | Datetime | Timestamp of when the song was added to iCloud library | 2023-07-28T05:04:34Z |
| `Last Modified Date` | Datetime | Date the song was last modified | 2023-07-28T05:04:34Z |
| `Last Played Date` | Datetime | Date the song was last played | 2024-08-02T21:36:11Z |
| `Skip Count` | Integer | Number of times the song was skipped | 12 |
| `Date of Last Skip` | Datetime | Last time the song was skipped | 2024-08-14T03:21:19Z |
| `Is Purchased` | Boolean | If the song is purchased or not | False |
| `Audio File Extension` | String | File extension | m4a |
| `Is Checked` | Boolean | No idea about this field but all values are false | False |
| `Copyright` | String | Music Label under which the song is released | ℗ 2023 Cactus Jack Records under exclusive license to Epic Records, a division of Sony Music Entertainment |
| `Release Date` | Datetime | Date the track was released | 2023-07-28T07:00:00Z |
| `Purchased Track Identifier` | Float | Identifier for Purchased Track | 1699712637.0 |
| `Apple Music Track Identifier` | Float | Identifier for Apple Music Track | 1699712637.0 |
| `Track Like Rating` | String | "liked" if the track was liked | liked |
| `Favorite Status - Track` | Boolean | True if the track was like | True |
| `Favorite Date - Track` | Datetime | Date on which the track was liked | 2024-03-02T05:59:53Z |
| `Album Like Rating` | String | Album which were liked | none |
| `Favorite Status - Album` | Boolean | Status of album that were liked | nan |
| `Grouping` | String |  |  |
| `Comments` | String | Comments on song |  |
| `Beats Per Minute` | Float | Beats per minute of song | 0.0 |
| `Rating` | Float | Rating of songs | 0.0 |
| `Album Rating` | Float | Rating of albums | 0.0 |
| `Remember Playback Position` | Boolean | Starts from the position where left off | False |
| `Album Rating Method` | String | How album was rated. Contains "Calculated" or none | Calculated |
| `Work Name` | String |  |  |
| `Movement Name` | String |  |  |
| `Movement Number` | Float |  | 0.0 |
| `Movement Count` | Float |  | 0.0 |
| `Display Work Name` | Boolean |  | False |
| `Playlist Only Track` | Boolean | If True that the track is present only in Playlist and not added in Library. "False" and nan aren't useful here. | nan |
| `Sort Album Artist` | String | Album Artist name to be sorted | nan |
| `Tag Matched Track Identifier` | Float |  | nan |


### Transformations
- `Track Name` from float to Int64.
- `Track Number On Album` from float to Int64
- `Track Count On Album` from float to Int64
- `Disc Number On Album` from float to Int64
- `Disc Count On Album` from float to Int64

## Schema Changes (Version History)
### Version 1.1

---
