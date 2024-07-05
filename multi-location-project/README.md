# multi-location-project

This example shows how to create a dagster project with two code locations. Each code location has a different set of dependencies. Both code locations share some code.

## Directory structure

```
# dagster_cloud.yaml at the top level defines two code locations
./dagster_cloud.yaml

# shared-dir contains shared code in a package called 'shared' and its own setup.py
./shared-dir
./shared-dir/shared
./shared-dir/shared/__init__.py
./shared-dir/setup.py

# location1-dir contains code for one code location in a module called 'location1'
./location1-dir
./location1-dir/requirements.txt  # this includes ../shared-dir
./location1-dir/setup.py          # this includes location1 specific dependencies
./location1-dir/location1
./location1-dir/location1/__init__.py
./location1-dir/location2/assets.py


./location2-dir
./location2-dir/requirements.txt  # this includes ../shared-dir
./location2-dir/setup.py          # this includes location2 specific dependencies
./location2-dir/location2
./location2-dir/location2/__init__.py
./location2-dir/location2/assets.py
```

## Running locally
To run locally via `dagster dev`, pip install the two projects:

```
cd ./location1-dir
pip install -e .[dev] -r requirements.txt
cd ../location2-dir
pip install -e .[dev] -r requirements.txt
```

And run `dagster dev` in this folder, which will use the `workspace.yaml` file to load both Dagster projects in the Dagster UI:

```
dagster dev
```