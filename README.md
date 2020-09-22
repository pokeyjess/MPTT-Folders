# Hierarchical Data demonstration

This is just a simple demonstration of how Modified Preorder Tree Traversal (MPTT) works.

Here, we are mimicking a Dropbox-like app which would store and maintain folders of information. Using the MPTT system, we can easily manipulate these folders from the admin panel.

Our homepage displays the "tree" of folders contained in the database.

## Requirements

python = "^3.8"
django-mptt = "^0.11.0"
django = "3.1.1"
poetry>=0.12
build-backend = "poetry.masonry.api"

## Credits

Thanks to Joe for the informative demo, and some help from this tutorial: https://django-mptt.readthedocs.io/en/latest/tutorial.html

