from io import StringIO
import pandas as pd

with open("lodgings.csv", "r") as f:
    lines = list(map(lambda l: l.replace(",", "_").replace(";", ","), f.readlines()))
df = pd.read_csv(
    StringIO("\n".join(lines)),
    header=None,
    skip_blank_lines=True,
)
df = df.rename(columns={
    0: "town",
    1: "address",
    2: "name",
    3: "coordinates",
    4: "phone_numbers",
    5: "description",
    6: "src",
})
df["coordinates"] = df["coordinates"].str.replace("_", ",")
df["phone_numbers"] = df["phone_numbers"].str.replace("_", ",")
df = df.astype(str)
df["name"] = df["name"].apply(str.strip)
df["address"] = df["address"].apply(str.strip)
df["phone_numbers"] = df["phone_numbers"].apply(str.strip)
df["description"] = df["description"].apply(str.strip)
df["src"] = df["src"].apply(str.strip)

# Remove rows that don't have coordinates.
df = df[~df["coordinates"].str.contains(r"\[Coordinates\]", na=False)]

df[["lat", "lon"]] = df["coordinates"].str.split(", ", expand=True)
df["lat"] = df["lat"].astype(float)
df["lon"] = df["lon"].astype(float)
df = df.drop(columns=["coordinates"])

df["wpt"] = df.apply(
    lambda row: f"""<wpt lat="{row["lat"]}" lon="{row["lon"]}"><name>{row.name} {row["name"]}</name><cmt>{row["description"]};{row["phone_numbers"]};{row["src"]}</cmt><desc>{row["description"]};{row["phone_numbers"]};{row["src"]}</desc></wpt>""",
    axis=1
)

with open("lodging-waypoints.xml", "w") as f:
    for row in df.itertuples(index=False):
        f.write(row.wpt + "\n")
# pd.set_option("display.max_columns", None)
# print(df.head())

