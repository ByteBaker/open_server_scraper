# open_server_scraper
Utility to scrape open web servers with only file listing ("index of" type)

## Usage
open_server_scraper can be used from the command line or imported as a python package.

### Command line usage
To use the script from command line
```
  $open_server_scraper
  Enter url: http://xyz.xyz.xyz.xyz/
  .
  .
  .
  Application output
  .
  .
  .
  Finally
  ...
  Total 17083 files were found.

  RAR - 3556 files.
  MKV - 10406 files.
  ZIP - 2334 files.
  MP4 - 787 files.
```

### Python Package Usage

The function **open_server_scraper** takes no arguments:

Calling the function asks for an OPEN SERVER URL. 
If the URL is not an open server URL, the utility will blow up, since exceptions have not been handled yet.

```
  >>>from open_server_scraper import web_scraper
  
  >>>web_scraper()
```

## License
This project is released under [GNU GENERAL PUBLIC LICENSE V3](https://www.gnu.org/licenses/gpl-3.0.en.html).
