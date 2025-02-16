# viafrancigena

Contains parsed results waypoints for navigation of loggings from Porto Ceresio (first official stop on route in Pavia) to Dragoni (near Caserta, which is north of Napoli).

Please note the following, when using these files:
* The accomodations from Porto Ceresio to Pavia are not part of the Via
    Francigena, neither is the path between these two places the one the Via
    Francigena takes.
* The first version of this list was aggregated using the PDFs on the
    viefrancigene.org website. These PDFs can be found here:
    * https://www.viefrancigene.org/wp-content/uploads/2025/02/02-Accoglienza-Pavia-Lucca-2.pdf
    * https://www.viefrancigene.org/wp-content/uploads/2025/02/03-Accoglienza-Lucca-Radicofani.pdf
    * https://www.viefrancigene.org/wp-content/uploads/2025/02/04-Accoglienza-Radicofani-Roma.pdf
    * https://www.viefrancigene.org/wp-content/uploads/2025/02/05-Accoglienza-Roma-Benevento.pdf
* That list was then refined and some more information added where available
    (like price and opening season) using the accomodation catalogue on
    viefrancigene.org: https://www.viefrancigene.org/en/detailed-catalogue-of-accommodations-facilities/
* For some of the accomodations' addresses I couldn't find a proper location on
    Google Maps for. These accomodations contain "[Coordinates]" in the
    coordinate column, but are then removed from the list when parsing to the
    waypoint XML and latex overview.
* Some of the accomodation has a question mark in front of the town name. For
    these accomodations something is unclear. The most common reason I marked
    an accomodation like that, is because I wasn't sure where they were
    located.
* It costs something to entertain accomodations like these. If the price says
    "donation" that doesn't mean you should just walk away not having given
    anything. Please give at the very least 10EUR as a donation where at all
    possible.

The gpx files are separated into sections, becase Garmin BaseCamp can't seem to
handle the entire route. It crashes when trying to transfer the route to a GPS
device. 

