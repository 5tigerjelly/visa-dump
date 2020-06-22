# visa-dump

## ℹ️ Overview
The US Department of Labor, Office of Foreign Labor Certification publishes working visa petitions on their [website](https://www.foreignlaborcert.doleta.gov/). However, the files are published as indivisual xlsx files. It is difficult to download all the files and process the data. This repo tackles this issue by sharing python scripts to download all data files and converting them to the desired file format and also sharing the converted files nicely packaged. The packaged OFLC Performance data is downloadable in JSON, CSV, and XLSX. Check the Data section to download files.

The dump was generated on June 21, 2020. 

## 📋 File List
Check [files.md](files.md) to view all files that are in the zip


## 📦 Data

| Format | Link                                                                         | File Size |
|--------|------------------------------------------------------------------------------| ----------|
| CSV    | https://archive.org/download/us-dol-visa-petition-data-csv-20200621/csv.zip  |  839.3M   |
| JSON   | https://archive.org/download/us-dol-visa-petition-data-csv-20200621/json.zip |  1.3G     |
| XLSX   | https://archive.org/download/us-dol-visa-petition-data-csv-20200621/xlsx.zip |   2.3G    |

Due to the size of the files, the dataset is hosted via [Internet Archive](https://archive.org)

### Example CSV Data
| CASE_NO       | DECISION_DATE | VISA_CLASS | CASE_RECEIVED_DATE | CASE_STATUS      | REQUESTED_START_DATE_OF_NEED | REQUESTED_END_DATE_OF_NEED | CERTIFICATION_BEGIN_DATE | CERTIFICATION_END_DATE | EMPLOYER_NAME             | EMPLOYER_ADDRESS1                  | EMPLOYER_ADDRESS2 | EMPLOYER_CITY  | EMPLOYER_STATE | EMPLOYER_POSTAL_CODE | AGENT_ATTORNEY_NAME | AGENT_ATTORNEY_CITY | AGENT_ATTORNEY_STATE | JOB_TITLE                             | NBR_WORKERS_REQUESTED | NBR_WORKERS_CERTIFIED | BASIC_NUMBER_OF_HOURS | BASIC_RATE_OF_PAY | BASIC_UNIT_OF_PAY | ALIEN_WORK_CITY | ALIEN_WORK_STATE | ORGANIZATION_FLAG | PRIMARY_CROP       | 
|---------------|---------------|------------|--------------------|------------------|------------------------------|----------------------------|--------------------------|------------------------|---------------------------|------------------------------------|-------------------|----------------|----------------|----------------------|---------------------|---------------------|----------------------|---------------------------------------|-----------------------|-----------------------|-----------------------|-------------------|-------------------|-----------------|------------------|-------------------|--------------------| 
| C-11046-27747 | 2011-10-05    | H-2A       | 2011-02-15         | Certified - Full | 2011-04-01                   | 2011-11-15                 | 2011-04-01               | 2011-11-15             | STAN WARD FARM            | 917 E 470 S                        |                   | DIETRICH       | ID             | 83324                | MICHAELENE ROWE     | HEYBURN             | ID                   | "FARMWORKERS AND LABORERS, CROP"      | 2.0                   | 2.0                   | 48                    | 9.9               | HR                | DIETRICH        | ID               | S                 | General Farm Labor | 
| C-11130-29271 | 2012-09-06    | H-2A       | 2011-05-10         | Certified - Full | 2011-07-10                   | 2012-07-09                 | 2011-07-10               | 2012-07-09             | WESTERN RANGE ASSOCIATION | "1245 E BRICKYARD ROAD, SUITE 190" |                   | SALT LAKE CITY | UT             | 84106                |                     |                     |                      | "FARMWORKERS, FARM AND RANCH ANIMALS" | 45.0                  | 45.0                  | 60                    | 750.0             | MTH               | SALT LAKE CITY  | UT               | A                 | Sheepherder        | 

### Example JSON Data
```json
[
  {
    "CASE_NO": "C-09163-19902",
    "DECISION_DATE": 1254410541000,
    "CASE_RECEIVED_DATE": 1244764800000,
    "CASE_STATUS": "Certified - Partial",
    "REQUESTED_START_DATE_OF_NEED": 1254355200000,
    "REQUESTED_END_DATE_OF_NEED": 1280534400000,
    "CERTIFICATION_BEGIN_DATE": 1254355200000,
    "CERTIFICATION_END_DATE": 1280534400000,
    "EMPLOYER_NAME": "KELLER FARMS, INC.",
    "EMPLOYER_ADDRESS1": "435 SOUTH BLUFF ROAD",
    "EMPLOYER_ADDRESS2": null,
    "EMPLOYER_CITY": "COLLINSVILLE",
    "EMPLOYER_STATE": "IL",
    "EMPLOYER_POSTAL_CODE": "62234",
    "AGENT_ATTORNEY_NAME": "RAY WILCOXSON, INC.",
    "AGENT_ATTORNEY_ADDRESS1": "424 NEW STREET",
    "AGENT_ATTORNEY_ADDRESS2": null,
    "AGENT_ATTORNEY_CITY": "HORSE CAVE",
    "AGENT_ATTORNEY_STATE": "KY",
    "AGENT_ATTORNEY_POSTAL_CODE": "42749-1804",
    "JOB_TITLE": "FARMWORKERS AND LABORERS, CROP, NURSERY, AND GREEN",
    "NBR_WORKERS_CERTIFIED": 29,
    "BASIC_RATE_OF_PAY": 8.02,
    "BASIC_UNIT_OF_PAY": "HR",
    "ALIEN_WORK_CITY": "COLLINSVILLE",
    "ALIEN_WORK_STATE": "IL",
    "ORGANIZATION_FLAG": "S"
  }
]
```                                      

## 🏃‍♀️ Running scripts
Run the `download.py` python script which will download all `.xlsx` files found on the DOL homepage and download them to the `data/xlsx` location. Run the `transform.py` python script to transform the downloaded files to JSON or CSV formats. 

## 🧑‍💻 Projects Using Data Dump
- [Visatopia](https://visatopia.fyi/) - Search millions of work visa application history. 