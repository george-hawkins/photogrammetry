Light sources
-------------

There are no end of people building there own ring flashes - see below for some examples.

However, I've come to the conclusion that this looks cooler than it works out in practice (see more below).

There appear to be a number of typical issues with the designs on YouTube:

* They seriously address heat dissipation or current limiting.
* They treat the LEDs as it they were "ideal" components, i.e. they need a current of 1A at 9V and have a resistence of 1ohm and that's it. In practice tho' such LEDs will display non-ideal characteristics (e.g. they won't share current equally).
* They use power sources that are completely incapable of providing 200W or of providing it safely.

Most videos have someone in the comments pointing up the shortcomings. I've included the best comments below.

A more realistic option is using an LED strip or a number of bright LED bulbs - see down below for more on these options.

DIY 10 x 20W LED right lights
-----------------------------

https://www.youtube.com/watch?v=xsd5b9p19nM

Fabian Feilcke comments:

Interesting project but from a engineering point of view a bit weird. Here a few suggestions to make the design better:
- If you run the LEDs@ 24V-25V they run at 3.xx Watts rather than 10W, so you might use 5W LEDs to begin with..
- 6 AA Battieries can only supply around 100W safely. If you draw more power thy might explode. Not exacly safe to carry around in your pocket.
- Usually you should run LED with a current source not an voltage source. Leds don't like voltage sources. The 5W version runs on 8V@700mA so no need for an inefficient voltage booster
This might even work without current source (Directly connected to 6 AA Batteries) as the internal resistance would limit the current automatically.
- Why on earth would you use paper clips?? Just use 2mm-copper wire, wrap it around an bottle and solder the ends - done...
- You can get small LED Heat-sinks with sticky-pads on them to cool the LEDs this will increase their lifetime greatly. Good cooling is imperative if you run LEDs in parallel mode as they tend to destroy themselves (LED gets warmer - draws more current away from the other LEDs - gets warmer- melts....)
- There are plenty of plugs you cannot connect the wrong way (Like Molex). No risk of burning anything...
- Just use a racing-battery pack. They are more stable and easy to charge. Usually they already come with a Molex connector.

Then in response to someone else (whose comment is now gone), he says:

- I already adressed the Issue with the batteries.. The problem is that you draw too much power from the Battery pack. This setup is close to a short circuit. If your LEDs draw around 300mA@25V the Batteries have to provide 1,25A, wich is way too much for an AA-cell. The only way around this is a more powerful battery pack (e.G. racing battery-pack from an RC-car) or to use more batteries.  If you put 14AA-Cells (2x7 ) in series you have 21V from the batteries -> around 350mA current draw ->Ok
-The second issue is more serious. LEDs have a manufacturing tolerance, so some will always draw more current if given the chance. As they are all connected in paralell there is no way to stop this. Only thing you can do is to glue small heatsinks on the back (Somehting like this: http://images.thecoolingshop.com/product_images/large/29/34096_01.jpg)

---

A simialar design that at least tries to disipate more of the heat (via an aluminum disk cut from a frying pan) can be found [here](https://www.youtube.com/watch?v=bcIdqdecKDI).

You can find the designs to go with this video [here](https://www.facebook.com/photo?fbid=645114522288869).

---

https://www.youtube.com/watch?v=eYr75LEEj50

FlyingShotsman comments:

Nice experiment!  LEDs are a blast to play around with.  Very cheap for the amount of light you can get. 

Just a few comments for anyone who might want to duplicate this build: 

1. You should never touch the yellow phosphor gel over a COB LED. If you press a little too hard, you can easily break bond wires, destroying the LED. 

2. Running this many LEDs in parallel isn't a good idea, as they won't share current equally. LED temperature will be inversely proportional to forward voltage, and since the LEDs won't be identical, the LED with the lowest Vf will tend to get hotter (this effect is somewhat mitigated by having the LEDs thermally coupled so closely on the heat sink). The problem is mostly solved by running them in series strings, and the strings in parallel. In this case, with 15 LEDs, wire them in series strings of three with five strings in parallel, or better yet, series strings of five with three strings in parallel. The longer your series strings, the better the current sharing. The limiting factor is the maximum voltage of your driver.

3. Using a constant-voltage power supply like the ATX unit used in this video isn't the best technique. LEDs are current-dependent devices and should always be driven by a constant-current driver. The ATX supply will allow an LED that goes into thermal runaway to pull as much current as it can, resulting in rapid failure. There are plenty of inexpensive LED drivers available on eBay, Banggood, Deal Extreme, AliExpress, etc.  Just look for the current output you need, with a maximum voltage that's at least as high as your series strings require.  Remember to multiply LED current by the number of parallel strings.  Voltage adds in series, current adds in parallel.

4. It's not necessary to run LEDs at their maximum current to get plenty of useful light from them. You can actually run them at <50% of their rated current and you'll barely see the difference in light output. The advantage is that the LED will require a lot less heat sink and will be much more reliable long-term.  The 10W LEDs used in this video are probably rated at ~700mA.  You could run them with a 300-350mA driver and they'll still blind you, but a piece of cheap aluminum bar from the local hardware store is enough to keep them cool.

200W power source
-----------------

How could you at least address the power aspect of such projects?

### Li-Po

Perhaps you could use a large Li-Po like the [5000mAh 11.1V 50C battery](https://www.gensace.de/gens-ace-5000mah-11-1v-3s1p-50c-lipo-battery-pack-with-xt-90-plug-bashing-series.html) from Gens Ace to power such a project.

Note: you'll need a battery where the mAh and C values combine such that the battery is capable of providing the 20a needed to provide 200W.

### A/C

200W power source: https://www.ebay.co.uk/itm/163585361443

Question what's LED specific about the power source? It can hardly limit current if it doesn't know how many LEDs it's driving or what kind of LEDs. Or can it?

Properly powering a 20W LED
---------------------------

Running a single LED _properly_ with a current limiter:

https://www.youtube.com/watch?v=WsGKk24h6Wo

Maybe, I should just buy 20 limiters - this would also have the advantage of spreading out the heat dissipation (vs one large step-down regulator).

TODO: ask "how to _properly_ drive strip of 20 10W LEDs?" Are individual drivers the only way to go?

Voltage regulators
------------------

Step down voltage regulator

10A max / 5A continuous: https://www.banggood.com/Geekcreit-8A-DC5-30V-to-DC1_25-30V-150KHz-Automatic-Step-Up-Step-Down-Adjustable-Power-Module-Voltage-Regulation-With-Short-Circuit-or-Overtemperature-Protection-p-969195.html

But it doesn't sound like voltage is _the_ issue (if you put them in series/paralled you'll have different voltage requirements) but that current limiting is the real problem.

5A max (so probably much less realistically): https://www.ebay.com/itm/272834659085

Pololu:

* 5A continuous - https://www.pololu.com/product/2851
* 15A continuous - https://www.pololu.com/product/2884

10W LEDs
--------

* https://www.ebay.com/itm/10pcs-10W-Neutral-White-LED-Lamp-Chip-4000-4500K-High-power-LED-9-12V-DC-/261409999817
* https://www.ebay.com/itm/113407778024
* https://www.ebay.com/itm/232756436516
* https://www.ebay.com/itm/122162355012

10W LEDs with individual drivers
---------------------------------

* https://www.ebay.com/itm/113172493944
* https://www.ebay.com/itm/113711683121

There drivers run directly off AC - sounds scary.

LED strips
----------

A more realistic option, with all the driver issues etc. sorted out, is an LED strip - connect it up to a 12V source and you're good to go.

These strips typically feature 60 LEDs per meter.

There are several LED types - 3528, 5050 and 5630. The 5630 is by far the most powerful (generates ~45lm vs 6lm for the 3528 and consumes ~500mW vs 60mW for the 3528).

For more see <https://www.12vmonster.com/blogs/product-questions/7698543-so-what-the-the-difference-between-a-3528-led-5050-led-and-5630-5730-led>

There are also less common 5730 LEDs which are somewhat more powerful that the 5630.

A 1m strip of 60 5360 LEDs costs around $3 on eBay - https://www.ebay.co.uk/itm/174468022497

Such a strip should consume about 30W.

This doesn't seem so impressive compared e.g. a few cheap lamps with something like the 1521lm bulbs from Philips covered below.

And it's a long way off from the 400W of the Godox Witstro AR400 which seems to be the go to right flash for photogrammetry.

But it's a lot more than the typical ring light used by influencers - such as these from Neewer (see below).

And how does it compare with e.g. Bolt VM-160 which some hobbyists are using for photogrammetry?

Note: see the [main page](README.md) for a link for the AR400 and the VM-160.

Maybe you could use the VM-160 in combination with a strip.

You need a reasonably hefty powersupply to handle such strips - e.g. a 12V 50W supply for around $20 from here https://www.ebay.co.uk/itm/163585361443 (note postage from UK to Switzerland costs GBP 50).

Above 50W these supplies start having multiple outputs, i.e. they only support a maximum of 50W per connected LED strip.

Alternatives with cheaper shipping to Switzerland are this [12V 5A unit](https://www.ebay.ch/itm/142624863834) and this similar [Mean Well unit](https://www.ebay.ch/itm/151182302253) (Mean Well seems to be a brand that a number of German eBay sellers are supplying) - after factoring in shipping, both are about Fr. 35.

Note: you can get even cheaper non-enclosed supplies but I'd be unhappy using them without some kind of enclosure.

Adafruit and Sparkfun have guides for soldering strips:

* https://learn.adafruit.com/make-it-glow-how-to-solder-neopixels-a-beginners-guide/soldering-strips
* https://learn.sparkfun.com/tutorials/non-addressable-rgb-led-strip-hookup-guide/modifying-rgb-led-strip

The strips in these guides aren't quite the same as the basic 12V non-addressable white LED covered here - the main thing seems to be make sure you use hot-glue or heat shrink for strain relief and to cover any exposed wiring at the joint.

Note: Blinkinlabs produce solder kits for providing a more stable and easier to solder connection - but these kits are only for addressable strips (dotstar or neopixels). 

Bright cold white bulbs
-----------------------

The brightest cold white / neutral white LED E27 bulbs that I've found that are easily available are the 1521lm CorePro bulbs from Philips.

See [here](https://www.lighting.philips.com/main/prof/led-lamps-and-tubes/led-bulbs/corepro-ledbulbs). However, the 4000K variants seem much more readily available than the 6000K variants (but 4000K is still better than the common 2700K warm white).

E.g. here are the 4000K variants from [Brack](https://www.brack.ch/philips-professional-lampe-corepro-ledbulb-12-5-100w-a60-e27-840-700751) and [Microspot](https://www.microspot.ch/de/wohnen-licht/leuchtmittel/leuchtmittel-pro--c489400/philips-corepro-ledbulb-lampe-led-e27-12-5-w--p0001863627).

Note: the more expensive influencer ring lights (see next section) seem to typically have a color temperature of 5500K.

Influencer ring lights
----------------------

Most of the cheap ring lights from manufacturers like Neewer are USB powered and so can't be expected to put out much in terms of light.

See [here](https://neewer.com/collections/ring-light) for Neewer ring lights.

Some of their more expensive ones, such as this [14" $110 one](https://neewer.com/collections/ring-light/products/led-ring-lights10087109) consume 36W and claim to generate 4800lm.

They typically either have a fixed color temperature of 5500K or are adjustable between 3200K and 5600K.
