## Table of Contents

- [Documentation](#documentation)
- [Bangladesh Tropical Cyclone Historical Event Hazard Module](#bangladesh-tropical-cyclone-historical-event-hazard-module)
  - [Dataset Overview](#dataset-overview)
  - [Hazard metadata](#hazard-metadata)
    - [Spatial coverage](#spatial-coverage)
      - [loc_0](#loc_0)
    - [Events](#events)
      - [Disaster identifiers](#disaster-identifiers)
      - [Footprints](#footprints)
    - [Hazards](#hazards)
  - [Spatial and Temporal Coverage](#spatial-and-temporal-coverage)
    - [Spatial](#spatial)
  - [Resources and Sources](#resources-and-sources)
    - [Resources](#resources)
      - [Event dictionary](#event-dictionary)
      - [Intensity Bin Dictionary for hazard intensity measures](#intensity-bin-dictionary-for-hazard-intensity-measures)
  - [Ownership and Contacts](#ownership-and-contacts)
    - [Publisher](#publisher)
    - [Creator](#creator)
    - [Contact point](#contact-point)
    - [Attributions](#attributions)
  - [Licensing and Links](#licensing-and-links)
    - [Links](#links)
    - [Referenced by](#referenced-by)
- [Sample property exposure data for testing.](#sample-property-exposure-data-for-testing)
  - [Dataset Overview](#dataset-overview-1)
  - [Exposure metadata](#exposure-metadata)
    - [Exposure metrics](#exposure-metrics)
  - [Spatial and Temporal Coverage](#spatial-and-temporal-coverage-1)
    - [Spatial](#spatial-1)
  - [Resources and Sources](#resources-and-sources-1)
    - [Resources](#resources-1)
      - [Exposure Required Fields](#exposure-required-fields)
      - [Demo location](#demo-location)
  - [Ownership and Contacts](#ownership-and-contacts-1)
    - [Publisher](#publisher-1)
    - [Creator](#creator-1)
    - [Contact point](#contact-point-1)
  - [Licensing and Links](#licensing-and-links-1)
    - [Links](#links-1)
- [Bangladesh Tropical Cyclone Historical Event Vulnerability Module](#bangladesh-tropical-cyclone-historical-event-vulnerability-module)
  - [Dataset Overview](#dataset-overview-2)
  - [Vulnerability metadata](#vulnerability-metadata)
    - [Hazard info](#hazard-info)
    - [Exposure info](#exposure-info)
    - [Vulnerability Impact info](#vulnerability-impact-info)
    - [Vulnerability Spatial info](#vulnerability-spatial-info)
    - [Vulnerability Functions info](#vulnerability-functions-info)
      - [Vulnerability function](#vulnerability-function)
  - [Spatial and Temporal Coverage](#spatial-and-temporal-coverage-2)
    - [Spatial](#spatial-2)
  - [Resources and Sources](#resources-and-sources-2)
    - [Resources](#resources-2)
      - [OED Construction codes](#oed-construction-codes)
      - [OED Occupancy codes](#oed-occupancy-codes)
    - [Sources](#sources)
  - [Ownership and Contacts](#ownership-and-contacts-2)
    - [Publisher](#publisher-2)
    - [Creator](#creator-2)
    - [Contact point](#contact-point-2)
    - [Attributions](#attributions-1)
  - [Licensing and Links](#licensing-and-links-2)
    - [Links](#links-2)
- [Sample ground up loss reports for Bangladesh property exposure data](#sample-ground-up-loss-reports-for-bangladesh-property-exposure-data)
  - [Dataset Overview](#dataset-overview-3)
  - [Spatial and Temporal Coverage](#spatial-and-temporal-coverage-3)
    - [Spatial](#spatial-3)
  - [Resources and Sources](#resources-and-sources-3)
    - [Resources](#resources-3)
      - [Analysis settings for modelled losses](#analysis-settings-for-modelled-losses)
      - [Ground up AAL](#ground-up-aal)
      - [Ground up ELT](#ground-up-elt)
      - [Ground up Aggregate LEC](#ground-up-aggregate-lec)
      - [Ground up Occurrence LEC](#ground-up-occurrence-lec)
      - [Ground up Summary Info](#ground-up-summary-info)
  - [Ownership and Contacts](#ownership-and-contacts-3)
    - [Publisher](#publisher-3)
    - [Creator](#creator-3)
    - [Contact point](#contact-point-3)
  - [Licensing and Links](#licensing-and-links-3)
    - [Links](#links-3)

# Documentation
# Bangladesh Tropical Cyclone Historical Event Hazard Module
## Dataset Overview
**Dataset identifier**: bgwtcss_haz

**Title**: Bangladesh Tropical Cyclone Historical Event Hazard Module

**Description**: The catalogue contains the following tropical cyclones (landfall date): BOB01(30/04/1991) BOB07 (25/11/1995) TC01B (19/05/1997) Akash (14/05/2007) Sidr (15/11/2007) Rashmi (26/10/2008) Aila (25/05/2009) Viyaru (16/05/2013) Roanu (21/05/2016) Mora (30/05/2017) Fani (04/05/2019) Bulbul (09/11/2019). Each tropical cyclone has a 9 member, 3-hourly time-lagged  ensemble and the hazard module comprises of hazard footprints for windspeed at 4.4km resolution and storm surge at 1.5km resolution based on the Met Office Unified Model dynamically downscaling ECMWF ERA5 data. Storm Surge simulation used open source-based Deft3D model. The historical storms occurred over a period of 29 years but in order to model the damage impact of each ensemble member individually they have each been assigned to an extended timeline of 261 years in the model implementation, with each ensemble member occurring once every 29 years in order to preserve the overall frequency of the event with respect to the historical record.

**Risk data type**: hazard

**Dataset version**: 1

**Project title**: Bangladesh tropical cyclone historical catalogue catastrophe model

**Additional details**: The Bangladesh Tropical Cyclone Probabilistic Historical Catalogue catastrophe models were created jointly between the UK Met Office, BUET, Catrisks Solutions and Oasis Palmtree as part of the ‘Oasis Platform for Climate and Catastrophe Risk Assessment – Asia’ project, supported by the International Climate Initiative (IKI) and the Federal Ministry for the Environment, Nature Conservation and Nuclear Safety, based on a decision of the Germany Bundestag. The models comprise an ensemble event catalogue representing the wind and storm surge hazard of 12 Tropical Cyclones that affected Bangladesh between 1991 and 2019. 

## Hazard metadata
| Event set identifier | Hazards | Analysis type | Frequency distribution | Seasonality distribution | Calculation Method | Event count | Occurrence range | Spatial coverage | Temporal coverage | Events |
|---|---|---|---|---|---|---|---|---|---|---|
| BGWTCSS1 | WTC,<br>WSS | probabilistic | user_defined | user_defined | simulated | 108 | 1 to 261 years | loc_0 | Start: 1991-01-01,<br>End date: 2019-12-31,<br>Duration: P29Y | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108 |

### Spatial coverage
#### loc_0
**Spatial scale**: national

**Countries**: BGD

**Bounding box**: [88.02799988, 92.64499664, 20.74389172, 26.59199905]

### Events
| Event identifier | Disaster identifiers | Model calculation method | Hazard | Occurrence | Description | Footprints |
|---|---|---|---|---|---|---|
| 1 | 2009-0204-BGD | simulated | WTC | <details><summary>Expand</summary>{<br>&nbsp;&nbsp;&nbsp;&nbsp;"probabilistic":&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"return_period":&nbsp;29<br>&nbsp;&nbsp;&nbsp;&nbsp;}<br>}</details> |  |  |
| 10 | 2007-0227-BGD | simulated | WTC | <details><summary>Expand</summary>{<br>&nbsp;&nbsp;&nbsp;&nbsp;"probabilistic":&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"return_period":&nbsp;29<br>&nbsp;&nbsp;&nbsp;&nbsp;}<br>}</details> |  |  |
| 100 | 2013-0138-BGD | simulated | WTC | <details><summary>Expand</summary>{<br>&nbsp;&nbsp;&nbsp;&nbsp;"probabilistic":&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"return_period":&nbsp;29<br>&nbsp;&nbsp;&nbsp;&nbsp;}<br>}</details> |  |  |
| 101 | 2013-0138-BGD | simulated | WTC | <details><summary>Expand</summary>{<br>&nbsp;&nbsp;&nbsp;&nbsp;"probabilistic":&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"return_period":&nbsp;29<br>&nbsp;&nbsp;&nbsp;&nbsp;}<br>}</details> |  |  |
| 102 | 2013-0138-BGD | simulated | WTC | <details><summary>Expand</summary>{<br>&nbsp;&nbsp;&nbsp;&nbsp;"probabilistic":&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"return_period":&nbsp;29<br>&nbsp;&nbsp;&nbsp;&nbsp;}<br>}</details> |  |  |
| 103 | 2013-0138-BGD | simulated | WTC | <details><summary>Expand</summary>{<br>&nbsp;&nbsp;&nbsp;&nbsp;"probabilistic":&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"return_period":&nbsp;29<br>&nbsp;&nbsp;&nbsp;&nbsp;}<br>}</details> |  |  |
| 104 | 2013-0138-BGD | simulated | WTC | <details><summary>Expand</summary>{<br>&nbsp;&nbsp;&nbsp;&nbsp;"probabilistic":&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"return_period":&nbsp;29<br>&nbsp;&nbsp;&nbsp;&nbsp;}<br>}</details> |  |  |
| 105 | 2013-0138-BGD | simulated | WTC | <details><summary>Expand</summary>{<br>&nbsp;&nbsp;&nbsp;&nbsp;"probabilistic":&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"return_period":&nbsp;29<br>&nbsp;&nbsp;&nbsp;&nbsp;}<br>}</details> |  |  |
| 106 | 2013-0138-BGD | simulated | WTC | <details><summary>Expand</summary>{<br>&nbsp;&nbsp;&nbsp;&nbsp;"probabilistic":&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"return_period":&nbsp;29<br>&nbsp;&nbsp;&nbsp;&nbsp;}<br>}</details> |  |  |
| 107 | 2013-0138-BGD | simulated | WTC | <details><summary>Expand</summary>{<br>&nbsp;&nbsp;&nbsp;&nbsp;"probabilistic":&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"return_period":&nbsp;29<br>&nbsp;&nbsp;&nbsp;&nbsp;}<br>}</details> |  |  |
| 108 | 2013-0138-BGD | simulated | WTC | <details><summary>Expand</summary>{<br>&nbsp;&nbsp;&nbsp;&nbsp;"probabilistic":&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"return_period":&nbsp;29<br>&nbsp;&nbsp;&nbsp;&nbsp;}<br>}</details> |  |  |
| 11 | 2007-0227-BGD | simulated | WTC | <details><summary>Expand</summary>{<br>&nbsp;&nbsp;&nbsp;&nbsp;"probabilistic":&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"return_period":&nbsp;29<br>&nbsp;&nbsp;&nbsp;&nbsp;}<br>}</details> |  |  |
| 12 | 2007-0227-BGD | simulated | WTC | <details><summary>Expand</summary>{<br>&nbsp;&nbsp;&nbsp;&nbsp;"probabilistic":&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"return_period":&nbsp;29<br>&nbsp;&nbsp;&nbsp;&nbsp;}<br>}</details> |  |  |
| 13 | 2007-0227-BGD | simulated | WTC | <details><summary>Expand</summary>{<br>&nbsp;&nbsp;&nbsp;&nbsp;"probabilistic":&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"return_period":&nbsp;29<br>&nbsp;&nbsp;&nbsp;&nbsp;}<br>}</details> |  |  |
| 14 | 2007-0227-BGD | simulated | WTC | <details><summary>Expand</summary>{<br>&nbsp;&nbsp;&nbsp;&nbsp;"probabilistic":&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"return_period":&nbsp;29<br>&nbsp;&nbsp;&nbsp;&nbsp;}<br>}</details> |  |  |
| 15 | 2007-0227-BGD | simulated | WTC | <details><summary>Expand</summary>{<br>&nbsp;&nbsp;&nbsp;&nbsp;"probabilistic":&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"return_period":&nbsp;29<br>&nbsp;&nbsp;&nbsp;&nbsp;}<br>}</details> |  |  |
| 16 | 2007-0227-BGD | simulated | WTC | <details><summary>Expand</summary>{<br>&nbsp;&nbsp;&nbsp;&nbsp;"probabilistic":&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"return_period":&nbsp;29<br>&nbsp;&nbsp;&nbsp;&nbsp;}<br>}</details> |  |  |
| 17 | 2007-0227-BGD | simulated | WTC | <details><summary>Expand</summary>{<br>&nbsp;&nbsp;&nbsp;&nbsp;"probabilistic":&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"return_period":&nbsp;29<br>&nbsp;&nbsp;&nbsp;&nbsp;}<br>}</details> |  |  |
| 18 | 2007-0227-BGD | simulated | WTC | <details><summary>Expand</summary>{<br>&nbsp;&nbsp;&nbsp;&nbsp;"probabilistic":&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"return_period":&nbsp;29<br>&nbsp;&nbsp;&nbsp;&nbsp;}<br>}</details> |  |  |
| 19 | 1991-0120-BGD | simulated | WTC | <details><summary>Expand</summary>{<br>&nbsp;&nbsp;&nbsp;&nbsp;"probabilistic":&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"return_period":&nbsp;29<br>&nbsp;&nbsp;&nbsp;&nbsp;}<br>}</details> |  |  |
| 2 | 2009-0204-BGD | simulated | WTC | <details><summary>Expand</summary>{<br>&nbsp;&nbsp;&nbsp;&nbsp;"probabilistic":&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"return_period":&nbsp;29<br>&nbsp;&nbsp;&nbsp;&nbsp;}<br>}</details> |  |  |
| 20 | 1991-0120-BGD | simulated | WTC | <details><summary>Expand</summary>{<br>&nbsp;&nbsp;&nbsp;&nbsp;"probabilistic":&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"return_period":&nbsp;29<br>&nbsp;&nbsp;&nbsp;&nbsp;}<br>}</details> |  |  |
| 21 | 1991-0120-BGD | simulated | WTC | <details><summary>Expand</summary>{<br>&nbsp;&nbsp;&nbsp;&nbsp;"probabilistic":&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"return_period":&nbsp;29<br>&nbsp;&nbsp;&nbsp;&nbsp;}<br>}</details> |  |  |
| 22 | 1991-0120-BGD | simulated | WTC | <details><summary>Expand</summary>{<br>&nbsp;&nbsp;&nbsp;&nbsp;"probabilistic":&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"return_period":&nbsp;29<br>&nbsp;&nbsp;&nbsp;&nbsp;}<br>}</details> |  |  |
| 23 | 1991-0120-BGD | simulated | WTC | <details><summary>Expand</summary>{<br>&nbsp;&nbsp;&nbsp;&nbsp;"probabilistic":&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"return_period":&nbsp;29<br>&nbsp;&nbsp;&nbsp;&nbsp;}<br>}</details> |  |  |
| 24 | 1991-0120-BGD | simulated | WTC | <details><summary>Expand</summary>{<br>&nbsp;&nbsp;&nbsp;&nbsp;"probabilistic":&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"return_period":&nbsp;29<br>&nbsp;&nbsp;&nbsp;&nbsp;}<br>}</details> |  |  |
| 25 | 1991-0120-BGD | simulated | WTC | <details><summary>Expand</summary>{<br>&nbsp;&nbsp;&nbsp;&nbsp;"probabilistic":&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"return_period":&nbsp;29<br>&nbsp;&nbsp;&nbsp;&nbsp;}<br>}</details> |  |  |
| 26 | 1991-0120-BGD | simulated | WTC | <details><summary>Expand</summary>{<br>&nbsp;&nbsp;&nbsp;&nbsp;"probabilistic":&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"return_period":&nbsp;29<br>&nbsp;&nbsp;&nbsp;&nbsp;}<br>}</details> |  |  |
| 27 | 1991-0120-BGD | simulated | WTC | <details><summary>Expand</summary>{<br>&nbsp;&nbsp;&nbsp;&nbsp;"probabilistic":&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"return_period":&nbsp;29<br>&nbsp;&nbsp;&nbsp;&nbsp;}<br>}</details> |  |  |
| 28 | 1995-0281-BGD | simulated | WTC | <details><summary>Expand</summary>{<br>&nbsp;&nbsp;&nbsp;&nbsp;"probabilistic":&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"return_period":&nbsp;29<br>&nbsp;&nbsp;&nbsp;&nbsp;}<br>}</details> |  |  |
| 29 | 1995-0281-BGD | simulated | WTC | <details><summary>Expand</summary>{<br>&nbsp;&nbsp;&nbsp;&nbsp;"probabilistic":&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"return_period":&nbsp;29<br>&nbsp;&nbsp;&nbsp;&nbsp;}<br>}</details> |  |  |
| 3 | 2009-0204-BGD | simulated | WTC | <details><summary>Expand</summary>{<br>&nbsp;&nbsp;&nbsp;&nbsp;"probabilistic":&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"return_period":&nbsp;29<br>&nbsp;&nbsp;&nbsp;&nbsp;}<br>}</details> |  |  |
| 30 | 1995-0281-BGD | simulated | WTC | <details><summary>Expand</summary>{<br>&nbsp;&nbsp;&nbsp;&nbsp;"probabilistic":&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"return_period":&nbsp;29<br>&nbsp;&nbsp;&nbsp;&nbsp;}<br>}</details> |  |  |
| 31 | 1995-0281-BGD | simulated | WTC | <details><summary>Expand</summary>{<br>&nbsp;&nbsp;&nbsp;&nbsp;"probabilistic":&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"return_period":&nbsp;29<br>&nbsp;&nbsp;&nbsp;&nbsp;}<br>}</details> |  |  |
| 32 | 1995-0281-BGD | simulated | WTC | <details><summary>Expand</summary>{<br>&nbsp;&nbsp;&nbsp;&nbsp;"probabilistic":&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"return_period":&nbsp;29<br>&nbsp;&nbsp;&nbsp;&nbsp;}<br>}</details> |  |  |
| 33 | 1995-0281-BGD | simulated | WTC | <details><summary>Expand</summary>{<br>&nbsp;&nbsp;&nbsp;&nbsp;"probabilistic":&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"return_period":&nbsp;29<br>&nbsp;&nbsp;&nbsp;&nbsp;}<br>}</details> |  |  |
| 34 | 1995-0281-BGD | simulated | WTC | <details><summary>Expand</summary>{<br>&nbsp;&nbsp;&nbsp;&nbsp;"probabilistic":&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"return_period":&nbsp;29<br>&nbsp;&nbsp;&nbsp;&nbsp;}<br>}</details> |  |  |
| 35 | 1995-0281-BGD | simulated | WTC | <details><summary>Expand</summary>{<br>&nbsp;&nbsp;&nbsp;&nbsp;"probabilistic":&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"return_period":&nbsp;29<br>&nbsp;&nbsp;&nbsp;&nbsp;}<br>}</details> |  |  |
| 36 | 1995-0281-BGD | simulated | WTC | <details><summary>Expand</summary>{<br>&nbsp;&nbsp;&nbsp;&nbsp;"probabilistic":&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"return_period":&nbsp;29<br>&nbsp;&nbsp;&nbsp;&nbsp;}<br>}</details> |  |  |
| 37 | 2019-0550-BGD | simulated | WTC | <details><summary>Expand</summary>{<br>&nbsp;&nbsp;&nbsp;&nbsp;"probabilistic":&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"return_period":&nbsp;29<br>&nbsp;&nbsp;&nbsp;&nbsp;}<br>}</details> |  |  |
| 38 | 2019-0550-BGD | simulated | WTC | <details><summary>Expand</summary>{<br>&nbsp;&nbsp;&nbsp;&nbsp;"probabilistic":&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"return_period":&nbsp;29<br>&nbsp;&nbsp;&nbsp;&nbsp;}<br>}</details> |  |  |
| 39 | 2019-0550-BGD | simulated | WTC | <details><summary>Expand</summary>{<br>&nbsp;&nbsp;&nbsp;&nbsp;"probabilistic":&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"return_period":&nbsp;29<br>&nbsp;&nbsp;&nbsp;&nbsp;}<br>}</details> |  |  |
| 4 | 2009-0204-BGD | simulated | WTC | <details><summary>Expand</summary>{<br>&nbsp;&nbsp;&nbsp;&nbsp;"probabilistic":&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"return_period":&nbsp;29<br>&nbsp;&nbsp;&nbsp;&nbsp;}<br>}</details> |  |  |
| 40 | 2019-0550-BGD | simulated | WTC | <details><summary>Expand</summary>{<br>&nbsp;&nbsp;&nbsp;&nbsp;"probabilistic":&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"return_period":&nbsp;29<br>&nbsp;&nbsp;&nbsp;&nbsp;}<br>}</details> |  |  |
| 41 | 2019-0550-BGD | simulated | WTC | <details><summary>Expand</summary>{<br>&nbsp;&nbsp;&nbsp;&nbsp;"probabilistic":&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"return_period":&nbsp;29<br>&nbsp;&nbsp;&nbsp;&nbsp;}<br>}</details> |  |  |
| 42 | 2019-0550-BGD | simulated | WTC | <details><summary>Expand</summary>{<br>&nbsp;&nbsp;&nbsp;&nbsp;"probabilistic":&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"return_period":&nbsp;29<br>&nbsp;&nbsp;&nbsp;&nbsp;}<br>}</details> |  |  |
| 43 | 2019-0550-BGD | simulated | WTC | <details><summary>Expand</summary>{<br>&nbsp;&nbsp;&nbsp;&nbsp;"probabilistic":&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"return_period":&nbsp;29<br>&nbsp;&nbsp;&nbsp;&nbsp;}<br>}</details> |  |  |
| 44 | 2019-0550-BGD | simulated | WTC | <details><summary>Expand</summary>{<br>&nbsp;&nbsp;&nbsp;&nbsp;"probabilistic":&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"return_period":&nbsp;29<br>&nbsp;&nbsp;&nbsp;&nbsp;}<br>}</details> |  |  |
| 45 | 2019-0550-BGD | simulated | WTC | <details><summary>Expand</summary>{<br>&nbsp;&nbsp;&nbsp;&nbsp;"probabilistic":&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"return_period":&nbsp;29<br>&nbsp;&nbsp;&nbsp;&nbsp;}<br>}</details> |  |  |
| 46 | 2019-0164-BGD | simulated | WTC | <details><summary>Expand</summary>{<br>&nbsp;&nbsp;&nbsp;&nbsp;"probabilistic":&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"return_period":&nbsp;29<br>&nbsp;&nbsp;&nbsp;&nbsp;}<br>}</details> |  |  |
| 47 | 2019-0164-BGD | simulated | WTC | <details><summary>Expand</summary>{<br>&nbsp;&nbsp;&nbsp;&nbsp;"probabilistic":&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"return_period":&nbsp;29<br>&nbsp;&nbsp;&nbsp;&nbsp;}<br>}</details> |  |  |
| 48 | 2019-0164-BGD | simulated | WTC | <details><summary>Expand</summary>{<br>&nbsp;&nbsp;&nbsp;&nbsp;"probabilistic":&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"return_period":&nbsp;29<br>&nbsp;&nbsp;&nbsp;&nbsp;}<br>}</details> |  |  |
| 49 | 2019-0164-BGD | simulated | WTC | <details><summary>Expand</summary>{<br>&nbsp;&nbsp;&nbsp;&nbsp;"probabilistic":&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"return_period":&nbsp;29<br>&nbsp;&nbsp;&nbsp;&nbsp;}<br>}</details> |  |  |
| 5 | 2009-0204-BGD | simulated | WTC | <details><summary>Expand</summary>{<br>&nbsp;&nbsp;&nbsp;&nbsp;"probabilistic":&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"return_period":&nbsp;29<br>&nbsp;&nbsp;&nbsp;&nbsp;}<br>}</details> |  |  |
| 50 | 2019-0164-BGD | simulated | WTC | <details><summary>Expand</summary>{<br>&nbsp;&nbsp;&nbsp;&nbsp;"probabilistic":&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"return_period":&nbsp;29<br>&nbsp;&nbsp;&nbsp;&nbsp;}<br>}</details> |  |  |
| 51 | 2019-0164-BGD | simulated | WTC | <details><summary>Expand</summary>{<br>&nbsp;&nbsp;&nbsp;&nbsp;"probabilistic":&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"return_period":&nbsp;29<br>&nbsp;&nbsp;&nbsp;&nbsp;}<br>}</details> |  |  |
| 52 | 2019-0164-BGD | simulated | WTC | <details><summary>Expand</summary>{<br>&nbsp;&nbsp;&nbsp;&nbsp;"probabilistic":&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"return_period":&nbsp;29<br>&nbsp;&nbsp;&nbsp;&nbsp;}<br>}</details> |  |  |
| 53 | 2019-0164-BGD | simulated | WTC | <details><summary>Expand</summary>{<br>&nbsp;&nbsp;&nbsp;&nbsp;"probabilistic":&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"return_period":&nbsp;29<br>&nbsp;&nbsp;&nbsp;&nbsp;}<br>}</details> |  |  |
| 54 | 2019-0164-BGD | simulated | WTC | <details><summary>Expand</summary>{<br>&nbsp;&nbsp;&nbsp;&nbsp;"probabilistic":&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"return_period":&nbsp;29<br>&nbsp;&nbsp;&nbsp;&nbsp;}<br>}</details> |  |  |
| 55 | 2017-0152-BGD | simulated | WTC | <details><summary>Expand</summary>{<br>&nbsp;&nbsp;&nbsp;&nbsp;"probabilistic":&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"return_period":&nbsp;29<br>&nbsp;&nbsp;&nbsp;&nbsp;}<br>}</details> |  |  |
| 56 | 2017-0152-BGD | simulated | WTC | <details><summary>Expand</summary>{<br>&nbsp;&nbsp;&nbsp;&nbsp;"probabilistic":&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"return_period":&nbsp;29<br>&nbsp;&nbsp;&nbsp;&nbsp;}<br>}</details> |  |  |
| 57 | 2017-0152-BGD | simulated | WTC | <details><summary>Expand</summary>{<br>&nbsp;&nbsp;&nbsp;&nbsp;"probabilistic":&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"return_period":&nbsp;29<br>&nbsp;&nbsp;&nbsp;&nbsp;}<br>}</details> |  |  |
| 58 | 2017-0152-BGD | simulated | WTC | <details><summary>Expand</summary>{<br>&nbsp;&nbsp;&nbsp;&nbsp;"probabilistic":&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"return_period":&nbsp;29<br>&nbsp;&nbsp;&nbsp;&nbsp;}<br>}</details> |  |  |
| 59 | 2017-0152-BGD | simulated | WTC | <details><summary>Expand</summary>{<br>&nbsp;&nbsp;&nbsp;&nbsp;"probabilistic":&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"return_period":&nbsp;29<br>&nbsp;&nbsp;&nbsp;&nbsp;}<br>}</details> |  |  |
| 6 | 2009-0204-BGD | simulated | WTC | <details><summary>Expand</summary>{<br>&nbsp;&nbsp;&nbsp;&nbsp;"probabilistic":&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"return_period":&nbsp;29<br>&nbsp;&nbsp;&nbsp;&nbsp;}<br>}</details> |  |  |
| 60 | 2017-0152-BGD | simulated | WTC | <details><summary>Expand</summary>{<br>&nbsp;&nbsp;&nbsp;&nbsp;"probabilistic":&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"return_period":&nbsp;29<br>&nbsp;&nbsp;&nbsp;&nbsp;}<br>}</details> |  |  |
| 61 | 2017-0152-BGD | simulated | WTC | <details><summary>Expand</summary>{<br>&nbsp;&nbsp;&nbsp;&nbsp;"probabilistic":&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"return_period":&nbsp;29<br>&nbsp;&nbsp;&nbsp;&nbsp;}<br>}</details> |  |  |
| 62 | 2017-0152-BGD | simulated | WTC | <details><summary>Expand</summary>{<br>&nbsp;&nbsp;&nbsp;&nbsp;"probabilistic":&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"return_period":&nbsp;29<br>&nbsp;&nbsp;&nbsp;&nbsp;}<br>}</details> |  |  |
| 63 | 2017-0152-BGD | simulated | WTC | <details><summary>Expand</summary>{<br>&nbsp;&nbsp;&nbsp;&nbsp;"probabilistic":&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"return_period":&nbsp;29<br>&nbsp;&nbsp;&nbsp;&nbsp;}<br>}</details> |  |  |
| 64 | 2008-0648-BGD | simulated | WTC | <details><summary>Expand</summary>{<br>&nbsp;&nbsp;&nbsp;&nbsp;"probabilistic":&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"return_period":&nbsp;29<br>&nbsp;&nbsp;&nbsp;&nbsp;}<br>}</details> |  |  |
| 65 | 2008-0648-BGD | simulated | WTC | <details><summary>Expand</summary>{<br>&nbsp;&nbsp;&nbsp;&nbsp;"probabilistic":&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"return_period":&nbsp;29<br>&nbsp;&nbsp;&nbsp;&nbsp;}<br>}</details> |  |  |
| 66 | 2008-0648-BGD | simulated | WTC | <details><summary>Expand</summary>{<br>&nbsp;&nbsp;&nbsp;&nbsp;"probabilistic":&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"return_period":&nbsp;29<br>&nbsp;&nbsp;&nbsp;&nbsp;}<br>}</details> |  |  |
| 67 | 2008-0648-BGD | simulated | WTC | <details><summary>Expand</summary>{<br>&nbsp;&nbsp;&nbsp;&nbsp;"probabilistic":&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"return_period":&nbsp;29<br>&nbsp;&nbsp;&nbsp;&nbsp;}<br>}</details> |  |  |
| 68 | 2008-0648-BGD | simulated | WTC | <details><summary>Expand</summary>{<br>&nbsp;&nbsp;&nbsp;&nbsp;"probabilistic":&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"return_period":&nbsp;29<br>&nbsp;&nbsp;&nbsp;&nbsp;}<br>}</details> |  |  |
| 69 | 2008-0648-BGD | simulated | WTC | <details><summary>Expand</summary>{<br>&nbsp;&nbsp;&nbsp;&nbsp;"probabilistic":&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"return_period":&nbsp;29<br>&nbsp;&nbsp;&nbsp;&nbsp;}<br>}</details> |  |  |
| 7 | 2009-0204-BGD | simulated | WTC | <details><summary>Expand</summary>{<br>&nbsp;&nbsp;&nbsp;&nbsp;"probabilistic":&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"return_period":&nbsp;29<br>&nbsp;&nbsp;&nbsp;&nbsp;}<br>}</details> |  |  |
| 70 | 2008-0648-BGD | simulated | WTC | <details><summary>Expand</summary>{<br>&nbsp;&nbsp;&nbsp;&nbsp;"probabilistic":&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"return_period":&nbsp;29<br>&nbsp;&nbsp;&nbsp;&nbsp;}<br>}</details> |  |  |
| 71 | 2008-0648-BGD | simulated | WTC | <details><summary>Expand</summary>{<br>&nbsp;&nbsp;&nbsp;&nbsp;"probabilistic":&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"return_period":&nbsp;29<br>&nbsp;&nbsp;&nbsp;&nbsp;}<br>}</details> |  |  |
| 72 | 2008-0648-BGD | simulated | WTC | <details><summary>Expand</summary>{<br>&nbsp;&nbsp;&nbsp;&nbsp;"probabilistic":&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"return_period":&nbsp;29<br>&nbsp;&nbsp;&nbsp;&nbsp;}<br>}</details> |  |  |
| 73 | 2016-0175-BGD | simulated | WTC | <details><summary>Expand</summary>{<br>&nbsp;&nbsp;&nbsp;&nbsp;"probabilistic":&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"return_period":&nbsp;29<br>&nbsp;&nbsp;&nbsp;&nbsp;}<br>}</details> |  |  |
| 74 | 2016-0175-BGD | simulated | WTC | <details><summary>Expand</summary>{<br>&nbsp;&nbsp;&nbsp;&nbsp;"probabilistic":&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"return_period":&nbsp;29<br>&nbsp;&nbsp;&nbsp;&nbsp;}<br>}</details> |  |  |
| 75 | 2016-0175-BGD | simulated | WTC | <details><summary>Expand</summary>{<br>&nbsp;&nbsp;&nbsp;&nbsp;"probabilistic":&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"return_period":&nbsp;29<br>&nbsp;&nbsp;&nbsp;&nbsp;}<br>}</details> |  |  |
| 76 | 2016-0175-BGD | simulated | WTC | <details><summary>Expand</summary>{<br>&nbsp;&nbsp;&nbsp;&nbsp;"probabilistic":&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"return_period":&nbsp;29<br>&nbsp;&nbsp;&nbsp;&nbsp;}<br>}</details> |  |  |
| 77 | 2016-0175-BGD | simulated | WTC | <details><summary>Expand</summary>{<br>&nbsp;&nbsp;&nbsp;&nbsp;"probabilistic":&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"return_period":&nbsp;29<br>&nbsp;&nbsp;&nbsp;&nbsp;}<br>}</details> |  |  |
| 78 | 2016-0175-BGD | simulated | WTC | <details><summary>Expand</summary>{<br>&nbsp;&nbsp;&nbsp;&nbsp;"probabilistic":&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"return_period":&nbsp;29<br>&nbsp;&nbsp;&nbsp;&nbsp;}<br>}</details> |  |  |
| 79 | 2016-0175-BGD | simulated | WTC | <details><summary>Expand</summary>{<br>&nbsp;&nbsp;&nbsp;&nbsp;"probabilistic":&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"return_period":&nbsp;29<br>&nbsp;&nbsp;&nbsp;&nbsp;}<br>}</details> |  |  |
| 8 | 2009-0204-BGD | simulated | WTC | <details><summary>Expand</summary>{<br>&nbsp;&nbsp;&nbsp;&nbsp;"probabilistic":&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"return_period":&nbsp;29<br>&nbsp;&nbsp;&nbsp;&nbsp;}<br>}</details> |  |  |
| 80 | 2016-0175-BGD | simulated | WTC | <details><summary>Expand</summary>{<br>&nbsp;&nbsp;&nbsp;&nbsp;"probabilistic":&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"return_period":&nbsp;29<br>&nbsp;&nbsp;&nbsp;&nbsp;}<br>}</details> |  |  |
| 81 | 2016-0175-BGD | simulated | WTC | <details><summary>Expand</summary>{<br>&nbsp;&nbsp;&nbsp;&nbsp;"probabilistic":&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"return_period":&nbsp;29<br>&nbsp;&nbsp;&nbsp;&nbsp;}<br>}</details> |  |  |
| 82 | 2007-0556-BGD | simulated | WTC | <details><summary>Expand</summary>{<br>&nbsp;&nbsp;&nbsp;&nbsp;"probabilistic":&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"return_period":&nbsp;29<br>&nbsp;&nbsp;&nbsp;&nbsp;}<br>}</details> |  |  |
| 83 | 2007-0556-BGD | simulated | WTC | <details><summary>Expand</summary>{<br>&nbsp;&nbsp;&nbsp;&nbsp;"probabilistic":&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"return_period":&nbsp;29<br>&nbsp;&nbsp;&nbsp;&nbsp;}<br>}</details> |  |  |
| 84 | 2007-0556-BGD | simulated | WTC | <details><summary>Expand</summary>{<br>&nbsp;&nbsp;&nbsp;&nbsp;"probabilistic":&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"return_period":&nbsp;29<br>&nbsp;&nbsp;&nbsp;&nbsp;}<br>}</details> |  |  |
| 85 | 2007-0556-BGD | simulated | WTC | <details><summary>Expand</summary>{<br>&nbsp;&nbsp;&nbsp;&nbsp;"probabilistic":&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"return_period":&nbsp;29<br>&nbsp;&nbsp;&nbsp;&nbsp;}<br>}</details> |  |  |
| 86 | 2007-0556-BGD | simulated | WTC | <details><summary>Expand</summary>{<br>&nbsp;&nbsp;&nbsp;&nbsp;"probabilistic":&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"return_period":&nbsp;29<br>&nbsp;&nbsp;&nbsp;&nbsp;}<br>}</details> |  |  |
| 87 | 2007-0556-BGD | simulated | WTC | <details><summary>Expand</summary>{<br>&nbsp;&nbsp;&nbsp;&nbsp;"probabilistic":&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"return_period":&nbsp;29<br>&nbsp;&nbsp;&nbsp;&nbsp;}<br>}</details> |  |  |
| 88 | 2007-0556-BGD | simulated | WTC | <details><summary>Expand</summary>{<br>&nbsp;&nbsp;&nbsp;&nbsp;"probabilistic":&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"return_period":&nbsp;29<br>&nbsp;&nbsp;&nbsp;&nbsp;}<br>}</details> |  |  |
| 89 | 2007-0556-BGD | simulated | WTC | <details><summary>Expand</summary>{<br>&nbsp;&nbsp;&nbsp;&nbsp;"probabilistic":&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"return_period":&nbsp;29<br>&nbsp;&nbsp;&nbsp;&nbsp;}<br>}</details> |  |  |
| 9 | 2009-0204-BGD | simulated | WTC | <details><summary>Expand</summary>{<br>&nbsp;&nbsp;&nbsp;&nbsp;"probabilistic":&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"return_period":&nbsp;29<br>&nbsp;&nbsp;&nbsp;&nbsp;}<br>}</details> |  |  |
| 90 | 2007-0556-BGD | simulated | WTC | <details><summary>Expand</summary>{<br>&nbsp;&nbsp;&nbsp;&nbsp;"probabilistic":&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"return_period":&nbsp;29<br>&nbsp;&nbsp;&nbsp;&nbsp;}<br>}</details> |  |  |
| 91 | 1997-0114-BGD | simulated | WTC | <details><summary>Expand</summary>{<br>&nbsp;&nbsp;&nbsp;&nbsp;"probabilistic":&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"return_period":&nbsp;29<br>&nbsp;&nbsp;&nbsp;&nbsp;}<br>}</details> |  |  |
| 92 | 1997-0114-BGD | simulated | WTC | <details><summary>Expand</summary>{<br>&nbsp;&nbsp;&nbsp;&nbsp;"probabilistic":&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"return_period":&nbsp;29<br>&nbsp;&nbsp;&nbsp;&nbsp;}<br>}</details> |  |  |
| 93 | 1997-0114-BGD | simulated | WTC | <details><summary>Expand</summary>{<br>&nbsp;&nbsp;&nbsp;&nbsp;"probabilistic":&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"return_period":&nbsp;29<br>&nbsp;&nbsp;&nbsp;&nbsp;}<br>}</details> |  |  |
| 94 | 1997-0114-BGD | simulated | WTC | <details><summary>Expand</summary>{<br>&nbsp;&nbsp;&nbsp;&nbsp;"probabilistic":&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"return_period":&nbsp;29<br>&nbsp;&nbsp;&nbsp;&nbsp;}<br>}</details> |  |  |
| 95 | 1997-0114-BGD | simulated | WTC | <details><summary>Expand</summary>{<br>&nbsp;&nbsp;&nbsp;&nbsp;"probabilistic":&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"return_period":&nbsp;29<br>&nbsp;&nbsp;&nbsp;&nbsp;}<br>}</details> |  |  |
| 96 | 1997-0114-BGD | simulated | WTC | <details><summary>Expand</summary>{<br>&nbsp;&nbsp;&nbsp;&nbsp;"probabilistic":&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"return_period":&nbsp;29<br>&nbsp;&nbsp;&nbsp;&nbsp;}<br>}</details> |  |  |
| 97 | 1997-0114-BGD | simulated | WTC | <details><summary>Expand</summary>{<br>&nbsp;&nbsp;&nbsp;&nbsp;"probabilistic":&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"return_period":&nbsp;29<br>&nbsp;&nbsp;&nbsp;&nbsp;}<br>}</details> |  |  |
| 98 | 1997-0114-BGD | simulated | WTC | <details><summary>Expand</summary>{<br>&nbsp;&nbsp;&nbsp;&nbsp;"probabilistic":&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"return_period":&nbsp;29<br>&nbsp;&nbsp;&nbsp;&nbsp;}<br>}</details> |  |  |
| 99 | 1997-0114-BGD | simulated | WTC | <details><summary>Expand</summary>{<br>&nbsp;&nbsp;&nbsp;&nbsp;"probabilistic":&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"return_period":&nbsp;29<br>&nbsp;&nbsp;&nbsp;&nbsp;}<br>}</details> |  |  |

#### Disaster identifiers
| Scheme | Classification identifier | Description | URI |
|---|---|---|---|
| EMDAT | 1991-0120-BGD | BOB01 ensemble 1 |  |
| EMDAT | 1995-0281-BGD | BOB07 ensemble 1 |  |
| EMDAT | 1997-0114-BGD | TC01B ensemble 1 |  |
| EMDAT | 2007-0227-BGD | AKASH ensemble 1 |  |
| EMDAT | 2007-0556-BGD | SIDR ensemble 1 |  |
| EMDAT | 2008-0648-BGD | RASHMI ensemble 1 |  |
| EMDAT | 2009-0204-BGD | AILA ensemble 1 |  |
| EMDAT | 2013-0138-BGD | VIYARU ensemble 1 |  |
| EMDAT | 2016-0175-BGD | ROANU ensemble 1 |  |
| EMDAT | 2017-0152-BGD | MORA ensemble 1 |  |
| EMDAT | 2019-0164-BGD | FANI ensemble 1 |  |
| EMDAT | 2019-0550-BGD | BULBUL ensemble 1 |  |

#### Footprints
| Footprint identifier | Hazard intensity measurement | Data uncertainty |
|---|---|---|

### Hazards
| Hazard identifier | Hazard type | Hazard processes | Intensity measure | Trigger |
|---|---|---|---|---|
| WSS | flood | storm_surge | fl_wd:m | Hazard type: strong_wind,<br>Hazard processes: ['tropical_cyclone'] |
| WTC | strong_wind | tropical_cyclone | PGWS_tcy:m/s |  |

## Spatial and Temporal Coverage
**Temporal resolution**: No temporal information found in json.

### Spatial
**Spatial scale**: national

**Countries**: BGD

## Resources and Sources
### Resources
| Resource identifier | Resource title | Resource description | Media type | Format | Spatial resolution | Coordinate reference system | Access Url | Download Url | Temporal coverage | Temporal resolution |
|---|---|---|---|---|---|---|---|---|---|---|
| hc_oasis_event_dict | Event dictionary | Contains the definition of the event ids in the model. | text/csv | csv |  |  |  | resources/haz/hc_oasis_event_dict.csv |  |  |
| Intensity_bin_dict | Intensity Bin Dictionary for hazard intensity measures | Contains the definition of bins of hazard intensity ranges for each peril. | text/csv | csv |  |  |  | resources/haz/Intensity_bin_dict.csv |  |  |

#### Event dictionary
File (hc_oasis_event_dict.csv) found [here](resources/haz/hc_oasis_event_dict.csv)

First 10 rows displayed only

| EVENT_ID | DESCRIPTION |
|---|---|
| 1 | AILA ensemble 1 |
| 2 | AILA ensemble 2 |
| 3 | AILA ensemble 3 |
| 4 | AILA ensemble 4 |
| 5 | AILA ensemble 5 |
| 6 | AILA ensemble 6 |
| 7 | AILA ensemble 7 |
| 8 | AILA ensemble 8 |
| 9 | AILA ensemble 9 |
| 10 | AKASH ensemble 1 |

#### Intensity Bin Dictionary for hazard intensity measures
File (Intensity_bin_dict.csv) found [here](resources/haz/Intensity_bin_dict.csv)

First 10 rows displayed only

| bin_index | bin_from | bin_to | interpolation | Peril | IMT |
|---|---|---|---|---|---|
| 1 | 0 | 0.1 | 0.05 | WTC | PGWS_tcy:m/s |
| 2 | 0.1 | 0.2 | 0.15 | WTC | PGWS_tcy:m/s |
| 3 | 0.2 | 0.3 | 0.25 | WTC | PGWS_tcy:m/s |
| 4 | 0.3 | 0.4 | 0.35 | WTC | PGWS_tcy:m/s |
| 5 | 0.4 | 0.5 | 0.45 | WTC | PGWS_tcy:m/s |
| 6 | 0.5 | 0.6 | 0.55 | WTC | PGWS_tcy:m/s |
| 7 | 0.6 | 0.7 | 0.65 | WTC | PGWS_tcy:m/s |
| 8 | 0.7 | 0.8 | 0.75 | WTC | PGWS_tcy:m/s |
| 9 | 0.8 | 0.9 | 0.85 | WTC | PGWS_tcy:m/s |
| 10 | 0.9 | 1 | 0.95 | WTC | PGWS_tcy:m/s |

## Ownership and Contacts
### Publisher
| Name | Email address | URL |
|---|---|---|
| Oasis LMF | support@oasislmf.org | https://oasislmf.org/ |

### Creator
| Name | Email address | URL |
|---|---|---|
| OasisLMF | support@oasislmf.org | https://oasislmf.org/ |

### Contact point
| Name | Email address | URL |
|---|---|---|
| OasisLMF | support@oasislmf.org | https://oasislmf.org/ |

### Attributions
| Attribution identifier | Entity | Role |
|---|---|---|
| bgwtcss_haz_wtc | UK Met Office,<br>https://www.metoffice.gov.uk | collaborator |
| bgwtcss_haz_wss | Bangladesh University of Engineering and Technology (BUET),<br>https://www.buet.ac.bd/web/ | collaborator |
| bgwtcss_col | Oasis PalmTree Limited,<br>info@oasispalmtree.co.uk,<br>http://oasispalmtree.co.uk/ | collaborator |
| bgwtcss_dist | Oasis Loss Modelling Framework,<br>support@oasislmf.org,<br>https://oasislmf.org/ | distributor |
| bgwtcss_spns | Federal Ministry for the Environment, Nature Conservation and Nuclear Safety,<br>https://www.bmuv.de/ | sponsor |
| bgwtcss_fund | International Climate Initiative (IKI),<br>https://www.international-climate-initiative.com/ | funder |

## Licensing and Links
**License**: CC-BY-NC-SA-4.0

### Links
- https://docs.riskdatalibrary.org/en/0__2__0/rdls_schema.json

### Referenced by
| Related resource identifier | Name | Author names | Publication date | URL | Digital object identifier |
|---|---|---|---|---|---|
| bgwtcss_haz_1 | Bangladesh Tropical Cyclone Historical Event Set:Data Description Documentation | Hamish Steptoe | 2019-10-07 | https://github.com/OasisLMF/BangladeshCyclone/docs/referencedBy/HistoricalCatalogueDataDescription.pdf |  |
| bgwtcss_haz_2 | Oasis Platform to Support Cyclone and Storm Surge
Risk Assessment for Bangladesh - Gobeshona conference presentation | Prof. A.K.M. Saiful Islam,<br> Nahruma Mehzabeen,<br> Dr. Mohan Kumar Das,<br>
Faruque Abdullah,<br> Maruf Billah | 2021-01-22 | https://github.com/OasisLMF/BangladeshCyclone/docs/referencedBy/Gobeshona_Oasis_22January2021.pdf |  |
| bgwtcss_haz_3 | Risk Modelling for Improved Disaster Risk Governance in Bangladesh - webinar presentation | Prof. A.K.M. Saiful Islam,<br> Nahruma Mehzabeen,<br> Dr. Mohan Kumar Das,<br>
Faruque Abdullah,<br> Maruf Billah | 2021-05-05 | https://github.com/OasisLMF/BangladeshCyclone/docs/referencedBy/BUET-Storm-Surge-Modelling-Oasis-October2020.pdf |  |
| bgwtcss_haz_4 | Tropical cyclone simulations over Bangladesh at convection permitting 4.4 km & 1.5 km resolution | Hamish Steptoe,<br> Nicholas Henry Savage,<br> Saeed Sadri,<br> Kate Salmon,<br> Zubair Maalick,<br>Stuart Webster  | 2021-02-16 | https://www.nature.com/articles/s41597-021-00847-5 | 10.1038/s41597-021-00847-5 |



# Sample property exposure data for testing.
## Dataset Overview
**Dataset identifier**: bgwtcss_exp

**Title**: Sample property exposure data for testing.

**Description**: A sample exposure location file of 20 properties is provided as an example of the required input format for running the model, along with a table describing the required fields and valid values.

**Risk data type**: exposure

**Dataset version**: 1

**Project title**: Bangladesh tropical cyclone historical catalogue catastrophe model

**Additional details**: The Bangladesh Tropical Cyclone Probabilistic Historical Catalogue catastrophe models were created jointly between the UK Met Office, BUET, Catrisks Solutions and Oasis Palmtree as part of the ‘Oasis Platform for Climate and Catastrophe Risk Assessment – Asia’ project, supported by the International Climate Initiative (IKI) and the Federal Ministry for the Environment, Nature Conservation and Nuclear Safety, based on a decision of the Germany Bundestag. The models comprise an ensemble event catalogue representing the wind and storm surge hazard of 12 Tropical Cyclones that affected Bangladesh between 1991 and 2019. 

## Exposure metadata
**Exposure category**: buildings

**Exposure taxonomy scheme**: OED

### Exposure metrics
| Identifier | Metric dimension | Metric quantity kind |
|---|---|---|
| 1 | structure | currency |
| 3 | content | currency |

## Spatial and Temporal Coverage
**Temporal resolution**: No temporal information found in json.

### Spatial
**Spatial scale**: national

**Countries**: BGD

## Resources and Sources
### Resources
| Resource identifier | Resource title | Resource description | Media type | Format | Spatial resolution | Coordinate reference system | Access Url | Download Url | Temporal coverage | Temporal resolution |
|---|---|---|---|---|---|---|---|---|---|---|
| ExposureRequiredFields | Exposure Required Fields | Describes the exposure format and fields required for modelling. | text/csv | csv |  |  |  | resources/exp/ExposureRequiredFields.csv |  |  |
| demo_location | Demo location | A sample exposure location file which can be run through the model. | text/csv | csv |  |  |  | resources/exp/demo_location.csv |  |  |

#### Exposure Required Fields
File (ExposureRequiredFields.csv) found [here](resources/exp/ExposureRequiredFields.csv)

First 10 rows displayed only

| Field | Scheme | File | Description | Valid values |
|---|---|---|---|---|
| LocPerilsCovered | OED | location | The perils to which the location is at risk. | WTC' ,'WSS', 'WW1','AA1' |
| Latitude | OED | location | The latitude of the location (decimal) | Floating point number |
| Longitude | OED | location | The longitude of the location (decimal) | Floating point number |
| OccupancyCode | OED | location | The OED code describing the occupancy type of the location | A subset of the standard OED OccupancyCodes:  1000;1050;1051;1052;1053;1054;1055;1056;1100;1101;1102;1103;1104;1105;1106;1107;1108;1109;1110;1111;1112;1113;1114;1115;1116;1117;1118;1119;1120;1121;1122;1123;1150;1151;1152;1153;1154;1155;1156;1157;1158;1159
 |
| ConstructionCode | OED | location | The OED code describing the construction type of the location | A subset of the standard OED ConstructionCodes:
5051;5052;5101;5151;5053;5054;5055;5102;5103;5104;5152 |

#### Demo location
File (demo_location.csv) found [here](resources/exp/demo_location.csv)

First 10 rows displayed only

| PortNumber | AccNumber | LocNumber | Longitude | Latitude | CountryCode | ConstructionCode | OccupancyCode | GeogScheme1 | GeogName1 | LocPerilsCovered | BuildingTIV | OtherTIV | ContentsTIV | BITIV | LocCurrency |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 1 | 1 | 89.95416667 | 22.6375 | BGD | 5051 | 1109 | CRSL2 |  | WSS | 1000 | 0 | 200 | 0 | USD |
| 1 | 1 | 2 | 89.29583333 | 22.67916667 | BGD | 5101 | 1110 | CRSL2 |  | WSS | 1000 | 0 | 200 | 0 | USD |
| 1 | 1 | 3 | 90.25416667 | 22.42916667 | BGD | 5151 | 1111 | CRSL2 |  | WSS | 1000 | 0 | 200 | 0 | USD |
| 1 | 1 | 4 | 89.99583333 | 22.4375 | BGD | 5052 | 1112 | CRSL2 |  | WSS | 1000 | 0 | 200 | 0 | USD |
| 1 | 1 | 5 | 90.27083333 | 22.42083333 | BGD | 5051 | 1113 | CRSL2 |  | WSS | 1000 | 0 | 200 | 0 | USD |
| 1 | 1 | 6 | 90.9375 | 25.15416667 | BGD | 5101 | 1114 | CRSL2 |  | WSS | 1000 | 0 | 200 | 0 | USD |
| 1 | 1 | 7 | 90.87916667 | 25.14583333 | BGD | 5151 | 1115 | CRSL2 |  | WSS | 1000 | 0 | 200 | 0 | USD |
| 1 | 1 | 8 | 90.1625 | 25.17916667 | BGD | 5052 | 1116 | CRSL2 |  | WSS | 1000 | 0 | 200 | 0 | USD |
| 1 | 1 | 9 | 89.9375 | 25.14583333 | BGD | 5051 | 1117 | CRSL2 |  | WSS | 1000 | 0 | 200 | 0 | USD |
| 1 | 1 | 10 | 90.04583333 | 25.0875 | BGD | 5101 | 1118 | CRSL2 |  | WSS | 1000 | 0 | 200 | 0 | USD |

## Ownership and Contacts
### Publisher
| Name | Email address | URL |
|---|---|---|
| Oasis LMF | support@oasislmf.org | https://oasislmf.org/ |

### Creator
| Name | Email address | URL |
|---|---|---|
| OasisLMF | support@oasislmf.org | https://oasislmf.org/ |

### Contact point
| Name | Email address | URL |
|---|---|---|
| OasisLMF | support@oasislmf.org | https://oasislmf.org/ |

## Licensing and Links
**License**: CC-BY-NC-SA-4.0

### Links
- https://docs.riskdatalibrary.org/en/0__2__0/rdls_schema.json



# Bangladesh Tropical Cyclone Historical Event Vulnerability Module
## Dataset Overview
**Dataset identifier**: bgwtcss_vln

**Title**: Bangladesh Tropical Cyclone Historical Event Vulnerability Module

**Description**: A set of 22 vulnerability functions were developed by BUET and CatRisk Solutions for the model based on the predominant construction types of residential buildings found Bangladesh. A list of supported Construction and Occupancy codes and additional attibutes and descriptions can be found in vulnerability resources.

**Risk data type**: vulnerability

**Dataset version**: 1

**Project title**: Bangladesh tropical cyclone historical catalogue catastrophe model

**Additional details**: The Bangladesh Tropical Cyclone Probabilistic Historical Catalogue catastrophe models were created jointly between the UK Met Office, BUET, Catrisks Solutions and Oasis Palmtree as part of the ‘Oasis Platform for Climate and Catastrophe Risk Assessment – Asia’ project, supported by the International Climate Initiative (IKI) and the Federal Ministry for the Environment, Nature Conservation and Nuclear Safety, based on a decision of the Germany Bundestag. The models comprise an ensemble event catalogue representing the wind and storm surge hazard of 12 Tropical Cyclones that affected Bangladesh between 1991 and 2019. 

## Vulnerability metadata
### Hazard info
| Key | Value |
|---|---|
| Primary hazard type | strong_wind |
| Secondary hazard type | coastal_flood |
| Primary hazard process | tropical_cyclone |
| Secondary hazard process | storm_surge |
| Hazard analysis type | empirical |
| Hazard intensity measurement | PGWS_tcy:m/s |

### Exposure info
**Exposure category**: buildings

**Exposure taxonomy scheme**: OED

| Cost identifier | Cost dimension | Cost unit |
|---|---|---|
| 1 | structure | USD |
| 3 | content | USD |

### Vulnerability Impact info
**Impact type**: direct

**Impact metric**: economic_loss_value

**Impact unit**: percentage

**Impact base data type**: observed

### Vulnerability Spatial info
**Spatial scale**: national

**Countries**: BGD

### Vulnerability Functions info
#### Vulnerability function
| Key | Value |
|---|---|
| Vulnerability function approach | hybrid |
| Vulnerability impact relationship type | discrete |

## Spatial and Temporal Coverage
**Temporal resolution**: No temporal information found in json.

### Spatial
**Spatial scale**: national

**Countries**: BGD

## Resources and Sources
### Resources
| Resource identifier | Resource title | Resource description | Media type | Format | Spatial resolution | Coordinate reference system | Access Url | Download Url | Temporal coverage | Temporal resolution |
|---|---|---|---|---|---|---|---|---|---|---|
| OED_CONSTRUCTION_CLASS | OED Construction codes | Describes attributes associated with OED construction code for vulnerability function mapping. | text/csv | csv |  |  |  | resources/vln/OED_CONSTRUCTION_CLASS.csv |  |  |
| OED_OCCUPANCY_CLASS | OED Occupancy codes | Describes attributes associated with OED occupancy code for vulnerability function mapping. | text/csv | csv |  |  |  | resources/vln/OED_OCCUPANCY_CLASS.csv |  |  |

#### OED Construction codes
File (OED_CONSTRUCTION_CLASS.csv) found [here](resources/vln/OED_CONSTRUCTION_CLASS.csv)

First 10 rows displayed only

| CONSTRUCTION CLASS | VULNERABILITY STRUCTURAL TYPE | VULNERABILITY STRUCTURAL HEIGHT | VULNERABILITY QUALITY CODE | Peril | Description |  |  |  |
|---|---|---|---|---|---|---|---|---|
| 5051 | TIM | WSS | LQU | Storm Surge | Rural houses with walls and/or roofs made of  Straw/Babboo/Polythene/Plastic/Canvas and Tin (CI sheet) |  |  |  |
| 5052 | TIM | WSS | MQU | Storm Surge | House with walls made of mud or unburnt brick and roofs made of  Straw/Babboo/Polythene/Plastic/Canvas |  |  |  |
| 5101 | MAS | WSS | GQU | Storm Surge | Masonary or timber house with roofs made of Tin (CI sheet ) or Tally |  |  |  |
| 5151 | CON | WSS | MQU | Storm Surge | Masonry and concerate  houses with Roofs made of solid material  |  |  |  |
| 5053 | TIM | WTC | GQU | Tropical Cyclone | Rural houses with walls and/or roofs made of  Straw/Babboo/Polythene/Plastic/Canvas and Tin (CI sheet) |  |  |  |
| 5054 | TIM | WTC | MQU | Tropical Cyclone | House with walls made of wood or Tin (CI sheet) and roofs made of Tin (CI sheet) or Tally |  |  |  |
| 5055 | TIM | WTC | LQU | Tropical Cyclone | House with walls made of mud or unburnt brick and roofs made of  Straw/Babboo/Polythene/Plastic/Canvas |  |  |  |
| 5102 | MAS | WTC | GQU | Tropical Cyclone | House with walls made of mud or unburnt brick and roofs made of  Tin (CI sheet) or Tally  |  |  |  |
| 5103 | MAS | WTC | MQU | Tropical Cyclone | Masonary or timber house with roofs made of Tally |  |  |  |
| 5104 | MAS | WTC | LQU | Tropical Cyclone | Concerte buildings with roofs made of Tin (CI sheet) or Telly |  |  |  |

#### OED Occupancy codes
No file found at /home/anish/Documents/github/BangladeshCyclone/docs/resources/vln/OED_OCCUPANCY_CLASS.csv, could not display data

### Sources
| Source identifier | Name | URL | type | Component |
|---|---|---|---|---|
| bgwtcss_vln | Global flood depth-damage functions (2017) | https://publications.jrc.ec.europa.eu/repository/bitstream/JRC105688/copy_of_global_flood_depth-damage_functions__30102017.xlsx | dataset | vulnerability |

## Ownership and Contacts
### Publisher
| Name | Email address | URL |
|---|---|---|
| Oasis LMF | support@oasislmf.org | https://oasislmf.org/ |

### Creator
| Name | Email address | URL |
|---|---|---|
| OasisLMF | support@oasislmf.org | https://oasislmf.org/ |

### Contact point
| Name | Email address | URL |
|---|---|---|
| OasisLMF | support@oasislmf.org | https://oasislmf.org/ |

### Attributions
| Attribution identifier | Entity | Role |
|---|---|---|
| bgwtcss_vln_wtc | CatRisk Solutions,<br>https://catrisks.com/ | collaborator |
| bgwtcss_vln_wss | Bangladesh University of Engineering and Technology (BUET),<br>http://oasispalmtree.co.uk/ | collaborator |

## Licensing and Links
**License**: CC-BY-NC-SA-4.0

### Links
- https://docs.riskdatalibrary.org/en/0__2__0/rdls_schema.json



# Sample ground up loss reports for Bangladesh property exposure data
## Dataset Overview
**Dataset identifier**: bgwtcss_los

**Title**: Sample ground up loss reports for Bangladesh property exposure data

**Description**: A set of ground up loss results for the sample property exposure is provided as an example of model output.

**Risk data type**: loss

**Dataset version**: 1

**Project title**: Bangladesh tropical cyclone historical catalogue catastrophe model

**Additional details**: The Bangladesh Tropical Cyclone Probabilistic Historical Catalogue catastrophe models were created jointly between the UK Met Office, BUET, Catrisks Solutions and Oasis Palmtree as part of the ‘Oasis Platform for Climate and Catastrophe Risk Assessment – Asia’ project, supported by the International Climate Initiative (IKI) and the Federal Ministry for the Environment, Nature Conservation and Nuclear Safety, based on a decision of the Germany Bundestag. The models comprise an ensemble event catalogue representing the wind and storm surge hazard of 12 Tropical Cyclones that affected Bangladesh between 1991 and 2019. 

## Spatial and Temporal Coverage
**Temporal resolution**: No temporal information found in json.

### Spatial
**Spatial scale**: national

**Countries**: BGD

## Resources and Sources
### Resources
| Resource identifier | Resource title | Resource description | Media type | Format | Spatial resolution | Coordinate reference system | Access Url | Download Url | Temporal coverage | Temporal resolution |
|---|---|---|---|---|---|---|---|---|---|---|
| analysis_settings | Analysis settings for modelled losses | The Oasis analysis settings file for modelled losses of sample exposure location file. | application/json | json |  |  |  | resources/los/analysis_settings.json |  |  |
| gul_S1_aalcalc | Ground up AAL | Ground up Average Annual Loss report for the sample exposure file. | text/csv | csv |  |  |  | resources/los/gul_S1_aalcalc.csv |  |  |
| gul_S1_eltcalc | Ground up ELT | Ground up Event Loss Table report for the sample exposure file. | text/csv | csv |  |  |  | resources/los/gul_S1_eltcalc.csv |  |  |
| gul_S1_leccalc_full_uncertainty_aep | Ground up Aggregate LEC | Aggregate Exceedance Probability report for the sample exposure file. | text/csv | csv |  |  |  | resources/los/gul_S1_leccalc_full_uncertainty_aep.csv |  |  |
| gul_S1_leccalc_full_uncertainty_oep | Ground up Occurrence LEC | Occurrence Loss Exceedance Curve report for the sample exposure file. | text/csv | csv |  |  |  | resources/los/gul_S1_leccalc_full_uncertainty_oep.csv |  |  |
| gul_S1_summary-info | Ground up Summary Info | Describes the summary level for the Ground Up loss reports. | text/csv | csv |  |  |  | resources/los/gul_S1_summary-info.csv |  |  |

#### Analysis settings for modelled losses
File (analysis_settings.json) found [here](resources/los/analysis_settings.json)

Cannot display preview for json files

#### Ground up AAL
File (gul_S1_aalcalc.csv) found [here](resources/los/gul_S1_aalcalc.csv)

First 10 rows displayed only

| summary_id | type | mean | standard_deviation |
|---|---|---|---|
| 1 | 1 | 48.217884 | 143.206922 |
| 1 | 2 | 49.664581 | 171.403816 |

#### Ground up ELT
File (gul_S1_eltcalc.csv) found [here](resources/los/gul_S1_eltcalc.csv)

First 10 rows displayed only

| summary_id | type | event_id | mean | standard_deviation | exposure_value |
|---|---|---|---|---|---|
| 1 | 1 | 1 | 46.550529 | 0.000000 | 40000.000000 |
| 1 | 2 | 1 | 31.357672 | 22.617233 | 40000.000000 |
| 1 | 1 | 2 | 45.532219 | 0.000000 | 40000.000000 |
| 1 | 2 | 2 | 20.240250 | 11.486238 | 40000.000000 |
| 1 | 1 | 3 | 253.289307 | 0.000000 | 40000.000000 |
| 1 | 2 | 3 | 178.524994 | 133.533371 | 40000.000000 |
| 1 | 1 | 4 | 252.728577 | 0.000000 | 40000.000000 |
| 1 | 2 | 4 | 266.524200 | 232.544098 | 40000.000000 |
| 1 | 1 | 5 | 992.356262 | 0.000000 | 40000.000000 |
| 1 | 2 | 5 | 1181.176514 | 432.259186 | 40000.000000 |

#### Ground up Aggregate LEC
File (gul_S1_leccalc_full_uncertainty_aep.csv) found [here](resources/los/gul_S1_leccalc_full_uncertainty_aep.csv)

First 10 rows displayed only

| summary_id | type | return_period | loss |
|---|---|---|---|
| 1 | 1 | 30.000000 | 360.428162 |
| 1 | 1 | 20.000000 | 282.219452 |
| 1 | 1 | 10.000000 | 90.211884 |
| 1 | 1 | 5.000000 | 45.688251 |
| 1 | 1 | 2.000000 | 0.000000 |
| 1 | 2 | 30.000000 | 450.006836 |
| 1 | 2 | 20.000000 | 283.058990 |
| 1 | 2 | 10.000000 | 85.143616 |
| 1 | 2 | 5.000000 | 35.261196 |
| 1 | 2 | 2.000000 | 0.000000 |

#### Ground up Occurrence LEC
File (gul_S1_leccalc_full_uncertainty_oep.csv) found [here](resources/los/gul_S1_leccalc_full_uncertainty_oep.csv)

First 10 rows displayed only

| summary_id | type | return_period | loss |
|---|---|---|---|
| 1 | 1 | 30.000000 | 290.157440 |
| 1 | 1 | 20.000000 | 252.604279 |
| 1 | 1 | 10.000000 | 46.782780 |
| 1 | 1 | 5.000000 | 45.616920 |
| 1 | 1 | 2.000000 | 0.000000 |
| 1 | 2 | 30.000000 | 390.677429 |
| 1 | 2 | 20.000000 | 240.727402 |
| 1 | 2 | 10.000000 | 78.639381 |
| 1 | 2 | 5.000000 | 34.062618 |
| 1 | 2 | 2.000000 | 0.000000 |

#### Ground up Summary Info
File (gul_S1_summary-info.csv) found [here](resources/los/gul_S1_summary-info.csv)

First 10 rows displayed only

| summary_id | _not_set_ | tiv |
|---|---|---|
| 1 | All-Risks | 20000.0 |

## Ownership and Contacts
### Publisher
| Name | Email address | URL |
|---|---|---|
| Oasis LMF | support@oasislmf.org | https://oasislmf.org/ |

### Creator
| Name | Email address | URL |
|---|---|---|
| OasisLMF | support@oasislmf.org | https://oasislmf.org/ |

### Contact point
| Name | Email address | URL |
|---|---|---|
| OasisLMF | support@oasislmf.org | https://oasislmf.org/ |

## Licensing and Links
**License**: CC-BY-NC-SA-4.0

### Links
- https://docs.riskdatalibrary.org/en/0__2__0/rdls_schema.json



