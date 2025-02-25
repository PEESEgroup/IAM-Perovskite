# IAM-Perovskite

### 1. Overall Use Instructions
This repository was prepared for the analysis of perovskite tandem PV development, incorporating spatiotemporal characteristics.

#### - Future Scenarios:

- The **IMAGE 3.2 model** was selected as the primary source of Integrated Assessment Model (IAM) scenarios.
- The **Premise tool** was used to integrate IAM scenario information into the Life Cycle Assessment (LCA) database.
LCA Database:

#### - LCA Databse:
The baseline LCA database is based on Ecoinvent 3.8.
Subsequent LCA analyses were conducted **using the IAM-enhanced LCA databases generated with Premise, Python, and Brightway**.
Database Features:

#### - Database Features:
The generated databases incorporate temporal (year-specific) and regional characteristics, facilitating comprehensive analyses about the production of PV modules.


### 2. Section Descriptions:
#### - Code
This section provides the code for integrating IAM scenarios with the LCA database using Premise and Brightway.
Key features of the code include:
- Integration of IAM and LCA
  - We provide the code in the Code section for integrating IAM scenarios with the LCA database using Premise and Brightway, with support from the Premise documentation (https://github.com/polca/premise).
- Perovskite Tandem Market Penetration:
  - We model the gradual market entry of perovskite tandem PV into the silicon PV market following the diffusion of innovation framework.
  - The target share in the code ranges from 0% to 100%, reflecting a wide spectrum of future adoption scenarios.
  - Certain information is compressed into .txt files for direct use by Python during execution.
- Transition Pathways:
  - The code also simulates the transition **from silicon PV to perovskite-silicon tandem PV, and eventually to all-perovskite tandem PV as a mainstream market component**.
  - Both **fast and slow transition scenarios are considered** to capture diverse future possibilities.
  - The final target share aligns with the assumed market penetration levels for perovskite tandem technologies.
  
This section is designed to provide flexible modeling options, reflecting various market adoption pathways and technological transition speeds.

#### - Data

We present the main data underlying the results of this study, including annual carbon emission outcomes under both long-lifetime and short-lifetime scenarios, with varying perovskite tandem shares. Our analysis considers the differences in outcomes resulting from fast and slow transitions to all-perovskite tandem photovoltaics, as well as the impact of lifetime evolution patterns.

In addition, we provide the corresponding changes in material demand, covering key materials such as tin, lead, and solar glass.

As the foundation for these industry-level results, we also share the unit emission results, which were derived from analyses based on the updated Ecoinvent database integrated with IAM information. These results include LCA outcomes across different years. The tools used for these analyses are listed in the section below.

#### - Map

In the Map section, we provide the files used to construct the relevant maps. The data utilized for map construction is stored in the Data section, and the tools employed for this purpose are listed below.

### 3. Tool Utilization:

Python 3.8 or higher

IMAGE 3.2

Premise 1.5 or higher (Compatibility with Python versions should be considered)

Brightway 2.5

Ecoinvent 3.8 or higher (Compatibility with Premise versions should be considered)

Arc GIS Map 10.8

Microsoft Office 365

Microsoft Excel for Microsoft 365 MSO (Version 2501 Build 16.0.18429.20132)
