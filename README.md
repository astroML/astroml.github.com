astroML web page repository for https://www.astroml.org

__Please do not submit pull requests to this repository, but directly to the source code!__
This repo is just hosting the rendered version of the webpage, the source code for the documentation
and figure scripts can be found in the [astroML](https://github.com/astroML/astroML), 
and [astroML_figures](https://github.com/astroML/astroML_figures)
repositories, respectively.

To build the website, clone both repos, define the `BOOK_FIGURES_PATH` env variable to point to the
`astroML_figures` clone, and use `make html` in the `doc` directory in the `astroML` clone.
