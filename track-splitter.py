from bs4 import BeautifulSoup

with open("Porto-Ceresio_Caserta.gpx", "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file, "xml")

# Extract metadata and remove author
metadata = soup.find("metadata")
old_author = metadata.find("author")
old_author.decompose()

trkpts   = soup.find("trkseg").find_all("trkpt")
wpts     = soup               .find_all("wpt")

segment_length = 500
segment_count = len(trkpts) // segment_length + 1
for i in range(segment_count):
    curr_seg_trkpts = trkpts[i * segment_length: (i + 1) * segment_length]
    curr_seg_wpts = []
    if i != segment_count - 1:
        curr_seg_wpts = [wpt for wpt in wpts
            if float(wpt["lat"]) >  float(curr_seg_trkpts[segment_length - 1]["lat"])]
        wpts          = [wpt for wpt in wpts
            if float(wpt["lat"]) <= float(curr_seg_trkpts[segment_length - 1]["lat"])]
    else:
        curr_seg_wpts  = wpts

    # Crate new gpx
    curr_seg_gpx = BeautifulSoup("<gpx></gpx>", "xml")
    curr_seg_gpx.gpx.attrs = soup.gpx.attrs
    curr_seg_trk = curr_seg_gpx.new_tag("trk")
    curr_seg_trkseg = curr_seg_gpx.new_tag("trkseg")

    # Add metadata
    curr_seg_gpx.gpx.append(metadata)

    # Add track name
    curr_seg_trk_name = curr_seg_gpx.new_tag("name")
    curr_seg_trk_name.append(f"Porto Ceresio to Caserta Segment {i + 1}")
    curr_seg_trk.append(curr_seg_trk_name)

    # Add wpt's (wpt's need to go before trkpt's)
    for wpt in curr_seg_wpts:
        curr_seg_gpx.gpx.append(wpt)

    # Add trkpt's
    for trkpt in curr_seg_trkpts:
        curr_seg_trkseg.append(trkpt)
    curr_seg_trk.append(curr_seg_trkseg)
    curr_seg_gpx.gpx.append(curr_seg_trk)

    filename = f"track-segments/Porto-Ceresio_Caserta_{i + 1}.gpx"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(curr_seg_gpx.prettify())
    print(f"Saved segment to {filename}.")

