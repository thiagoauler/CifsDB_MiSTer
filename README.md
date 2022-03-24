# CifsDB_MiSTer

## Introduction
After taking a closer look in the "MiSTer Downloader" documentation, especifically about [custom databases](https://github.com/MiSTer-devel/Downloader_MiSTer/blob/main/docs/custom-databases.md), I kept wondering if it'd be possible to set a *shared folder in my network* containing all necessary ROMs and use "downloader.sh" to do all the work for me.

I made some experimentation and could finally set it done. Three steps are necessary to accomplish this:

1. As I wanted to a shared folder as a provider, it's first necessary to setup a cifs folder directly in MiSTer. This is easily achievable using "cifs_mount.sh" script provided officially by [Scripts_MiSTer Repository](https://github.com/MiSTer-devel/Scripts_MiSTer). Just download "cifs_mount.sh", copy it to Scripts folder in /media/fat and configure it accordingly (the script is well documents and should not be any trouble). Execute it to have /media/fat/cifs folder available as your personal ROM repository.
2. It's necessary a custom dabase in JSON format (which is generated using this script, see next section)
3. Now it's necessary to make "donwloader.sh" aware of the custom datase. For this, edit "/media/fat/downloader.ini" file. As we put the custom database in the shared folder (which is mounted as /media/fat/cifs on MiSTer) we can add the following lines:
```
[cifs_roms_db]
db_url = '../cifs/cifs_roms_db.json'
```
As it's not an *http* URL, the script will use it as a relative path.

## Usage
To genarate the custom database for "downloader.sh" is quite simple. Just download this script and run it as follows:

```
./build_database.py <path_to_shared_folder>
```

It will parse the folder and generate "cifs_rom_db.json" in that folder.
