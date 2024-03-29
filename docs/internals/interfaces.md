---
layout: template
title: Interfaces
permalink: /internals/interfaces
link_group: internals
---
# :information_desk_person: Table of Contents
{:.no_toc}
* TOC
{:toc}

# Interfaces

This page covers topics regarding the public interface provided to developers using pyatv.

# External Interfaces

The external interface is documented in the [developer documentation](https://pyatv.dev/development/api_reference/) (no need do duplicate it here). Everything else should be considered private.

In general these interfaces shall not be altered in such a way that it breaks conformity with released versions of pyatv. It is however OK to change an interface on `master` that has not yet been released as part of the development cycle.

If a breaking change must be made:

* Create issue describing the breaking change, add the `breaking change` label
* Update the [Migration](https://pyatv.dev/support/migration/) page
* Make sure this change is clearly marked in `CHANGES.md` (responsibility of @postlund)

When adding a new interface or updating an existing one, consider the following:

* Make necessary changes in {% include code file="interface.py" %}
* Is your addition a [feature](#features)?
* Reflect your changes in the protocols (e.g. {% include code file="dmap/__init__.py" %} and {% include code file="mrp/__init__.py" %})
* Update [documentation](documentation#interfaces)
* Generate API reference (`./scripts/api.py generate`)

## Adding a new Interface

Add a new interface by defining it in {% include code file="interface.py" %}. In general you need to add one interface (class) and also add a property to `interface.AppleTV` used to access the interface. General considerations mentioned above must also be taken into account. You can look at [this](https://github.com/postlund/pyatv/pull/498/commits/bba5a4f03b4dc087f5d8ef44d48c06c3a2360759) commit for some inspiration. The [PR](https://github.com/postlund/pyatv/pull/498) is also a good resource for how the feature was implemented and documented.

## Changing Existing Interface

Changing an already existing interface is generally simpler than adding a new one. Follow the same guidelines as above and there should be no problems.

## Features

When adding something with varying availability or something that is device/OS dependent, it should be considered a "feature" and conform to {% include api i="interface.Features" %}. In practice this means that a user should be able to ask if a certain feature is supported by the device or its availability.

This is done by adding the `@feature` decorator to your method or property (*only* in {% include code file="interface.py" %}):

```python
    @abstractmethod
    @feature(6, "Pause", "Pause playing media.")
    def pause(self) -> None:
        """Press key play."""
        raise exceptions.NotSupportedError()
```

The decorator takes three arguments:

* An index that is unique for the feature
* Feature name - creates a constant in `const.FeatureName.<name>`
* Description of the feature - shown in API reference

All features need a unique index and it doesn't really matter what it is, but common practice is to use the "next free". pyatv will fail to load if there is a collision. More about this below.

When a new feature has been added, the {% include api i="const.FeatureName" %} enum must be updated. You do this simply by running:

```shell
$ python ./scripts/features.py
# This enum is generated by scripts/features.py
class FeatureName(Enum):
    """All supported features."""

    Up = 0
    """Up button on remote."""

    Down = 1
    """Down button on remote."""

    Left = 2
    """Left button on remote."""
...

Next free index: 35
```

Then just copy-paste the generated code. As seen at the bottom of the input, the next free index is printed. So you can just run this script before adding a new feature to get a new index.

Next step is to make sure {% include api i="interface.Features.get_feature" %} returns the correct state for your feature. Refer to each protocol implementation and make sure to add tests.

## Adding to facade

All new interfaces must all be added to {% include code file="support/facade.py" %}. It should in most cases be
fairly straight-forward: just use one of the other implementations as an example. You can read
more about the facade pattern under [design](design#facade).