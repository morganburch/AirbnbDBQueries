# Airbnb Listings Analysis – Sample Queries

This repository demonstrates **MongoDB queries for analyzing Airbnb listings**.

## Overview

The scripts include queries to explore patterns in:

- Property features (e.g., accessibility, size, waterfront)  
- Pricing and top-priced listings  
- Review scores (e.g., cleanliness vs. location)  
- Geographic trends (e.g., most reviewed listings in Portugal)  
- Host activity (e.g., hosts with large portfolios and response rates below 90%)  

All queries are written in Python using `pymongo`.  

## Sample Data

`sample_airbnb.json` contains a **small, representative sample** of the Airbnb dataset used for analysis. It illustrates the structure and types of data in the original dataset, including fields such as:

- `_id`, `name`, `property_type`, `beds`, `bathrooms`  
- `amenities`, `price`, `reviews`, `review_scores`  
- `address` (country) and `host` information  

> Note: This JSON is **for reference only**

## Skills Demonstrated

- MongoDB querying and aggregation pipelines  
- Filtering, sorting, and analysis of structured datasets  
- Data exploration and feature-driven insights  
- Clear, commented Python scripts for reproducibility
