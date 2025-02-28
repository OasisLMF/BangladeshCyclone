
---

# Bangladesh Tropical Cyclone Probabilistic Historical Catalogue Models

## Overview

The **Bangladesh Tropical Cyclone Probabilistic Historical Catalogue** catastrophe models were developed through a collaboration between:

- **UK Met Office**
- **BUET** (Bangladesh University of Engineering and Technology)
- **Catrisks Solutions**
- **Oasis Palmtree**

These models were created as part of the **Oasis Platform for Climate and Catastrophe Risk Assessment – Asia** project, which is supported by the **International Climate Initiative (IKI)** and the **Federal Ministry for the Environment, Nature Conservation and Nuclear Safety** (BMU), based on a decision of the German Bundestag.

The models consist of an ensemble event catalogue representing the wind and storm surge hazards of 12 tropical cyclones that impacted Bangladesh between 1991 and 2019.

## Repository Contents

This repository contains:

- A **Bash script** to download the required footprint data for the **Bangladesh Wind Tropical Cyclone (BGWTCSS1)** open model from an AWS S3 bucket.
- Other model files stored directly in the GitHub repository.

## Prerequisites

Before you begin, ensure you have the following installed on your system:

- **wget**: This tool is needed to download files from the S3 bucket.

You can install it using your system’s package manager (e.g., `apt`, `yum`, or `brew`).

## Instructions

Follow these steps to download the model data:

1. **Clone the repository** (if you haven't already):

    ```bash
    git clone <git@github.com:OasisLMF/BangladeshCyclone.git>
    cd BangladeshCyclone
    ```

    Then run the script:

    ```bash
    ./download_bgwtcss1.sh

    ```

## Structure of Downloaded Data

After running the script, the `model_data/` directory should contain the following files:

```
footprint.bin.z & footprint.idx.z
```

## Troubleshooting

If you encounter any issues, try the following:

- **Download fails**: Check your internet connection and try again.
- **wget not installed**: Ensure wget is installed using your system’s package manager.
- **Permission errors**: If you receive permission errors, try running the script with `sudo`:

    ```bash
    sudo ./download_bgwtcss1.sh
    ```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
