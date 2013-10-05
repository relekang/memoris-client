memoris-client
==============

A client for [memoris a key-value store api](http://github.com/relekang/memoris)

### Usage
There is two possible ways to use the client. Command line or by python code

    $ memoris <key> #get
    $ memoris <key> <value> #set
    $ memoris h <name> #get all in hash
    $ memoris h <name> <key> #get key in hash
    $ memoris h <name> <key> <value> #set key i hash
    
If you are using the client in your own python code just import the helper and initialize it.

    from memoris.helpers import Memoris
    m = Memoris()

### Configuration
Memoris will look for configuration in `~/.memorisrc`

#### Sample configuration
    [memoris]
    url=http://n.lkng.me
