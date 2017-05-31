# asyncioplus

Additions to Python 3's asyncio module.

If you think this could be useful, please consider assisting by:

* Doing the standard packaging magic that would allow installing via pip.
* Suggesting these additions should be included in the Python standard library.
* Coding TODOs you find in the code.

## Example

To run the [example](example.py), clone the repo and run:

```bash
python3 example.py
```

This illustrates using `limited_as_completed` to run 100 tasks asynchronously,
limiting the number of in-progress tasks to a set limit (10 in this example).

## Copying

Copyright(c) 2017 Andy Balaam and the asyncioplus contributors.

Released under the [Python Software Foundation Licence](https://docs.python.org/3/license.html).
See [LICENSE.txt](LICENSE.txt) for details.
