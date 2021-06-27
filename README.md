Photogrammetry
==============

Below you'll find miscellaneous notes related in some way to photogrammetry.

See also here:

* [`glasses.md`](glasses.md)
* [`lighting.md`](lighting.md)
* [`nikon-firmware-upgrade.md`](nikon-firmware-upgrade.md)
* [`pifuhd`](pifuhd)
* [`turntable-request-for-quote.md`](turntable-request-for-quote.md)
* [`scanning-sprays.md`](scanning-sprays.md)
* [`photogrammetry-course-notes.md`](photogrammetry-course-notes.md)
* [`base-pattern`](base-pattern)
* [`projects`](projects)

Videos
------

* [Scanning in the void](https://www.youtube.com/watch?v=Il6LVXqSlRg) by Erik Christensen (the Witstro AR400 that he uses shows up all the time in photogrammetry videos).
* [Scanning featureless objects](https://www.youtube.com/watch?v=krm9vDlTaxU) also by Erik Christensen.
* [Cross polarization explained](https://www.youtube.com/watch?v=yhjKO1a99OQ) - he buys his _linear_ polarization film from [Polarization.com](http://polarization.com/polarshop/product_info.php?cPath=21&products_id=28) - 43cm x 61cm for $30 and then uses a _circular_ polarization filter on his camera and discuss the effect seen when rotating one relative to the other.

Erik Christensen rotates his subject on an amazingly expensive [Syrp Genie Mini II panning motion control system](https://www.bhphotovideo.com/c/product/1483069-REG/syrp_sy0033_0001_genie_mini_ii_panning.html). You can get much cheaper devices like the [Movo Photo MTP-11](https://www.bhphotovideo.com/c/product/1624190-REG/movo_photo_mtp_11_motorized_panoramic_time.html) but why not just use an electric turntable from AliExpress (see section below).

Erik Christensen doesn't discuss how he made the polarizing film mount he uses so, Exitaph created one himself and released the 3D model and details [here](https://cults3d.com/en/3d-model/gadget/flashpoint-rf-400-godox-ar400-90-degree-magnetic-polarizing-film-mount). Viz Guru (see next paragraphs) also makes a similar 3D model available [here](https://www.patreon.com/posts/ar400-filter-for-45493702).

For an amazing automated scanning-in-the-void system in action see [here](https://www.youtube.com/watch?v=dyPn5lmq9B4&t=329s) (link starts 5m 29s in to the video - the first 5 minutes show building the system).

The guy (Viz Guru) who made this system also has a [5 part series](https://www.youtube.com/watch?v=010lAKpr7JE) on photogrammetry where he answers all the questions others barely mention, e.g. how mnay photos do you _really_ need, what kind of lens do you need. He compares all different kinds of equipment so at the end you have a much clearer idea of what impacts you results and what price point you want to go for.

Note: [part 2](https://www.patreon.com/posts/photogrammetry-2-37039151) and the subsequent parts are available on Patreon rather than YouTube. You need to subscribe at the $3 per month tier to access this content. Partreon have a very fair cancelation process - i.e. _if you want_, you can pay for one month up front and then cancel immediatelly and you have access for that month with no auto-renewal (but renewals occurs at the start of calendar months - so if you subscribe on e.g. June 24th, you'll only get 7 days access until renewal). He also says he'll make the videos available on Gumroad but they aren't available under [his account](https://gumroad.com/vizguru) there at the moment.

There are many similar builds including this [one](https://www.youtube.com/watch?v=Fj7wGGXPM0A) that he's since scaled down into something far smaller that's open source and available as a kit [here](https://en.openscan.eu/shop).

Ben Kreimer has a nice [page](http://www.immersiveshooter.com/2020/05/11/photogrammetry-photography-guide-ring-flash-photography/) on choosing a ring flash for photogrammetry - as with everyone else he goes with the Witstro AR400. He specifically doesn't recommend the much cheaper ring _lights_ available from many sources. He mentions that "I consistently shoot at 200 ISO, f/16, 1/200th of a second".

Ring flash/light
----------------

* $500 - [Witstro AR400](https://www.bhphotovideo.com/c/product/1341907-REG/godox_ar400_witstro_ring_flash.html).
* $70 - [Bolt VM-160](https://www.bhphotovideo.com/c/product/750878-REG/bolt_vm_160_led_macro_ring.html).

For more on lighting - building your own ring light with 10W LEDs or, more realistically, lighting with an LED strip or bright LED bults - see [`lighting.md`](lighting.md).

Polarizing film and polarizer filters
-------------------------------------

Polarizing film isn't particularly cheap:

* $26 - [200 x 200 x 0.3mm](https://www.bhphotovideo.com/c/product/1484365-REG/b_w_1083862_polarizing_film_linear_200.html) (B+H).
* EUR 35 - [250 x 250 x 0.3mm](https://www.amazon.de/Polfolie-linear-Beleuchtungszwecke-kreative-Aufnahmen/dp/B07GLR2DLD/) (Amazon).
* EUR 30 - [300 x 300 x 0.2mm](https://www.amazon.de/Polarisationsfolie-linear-90%C2%B0-Polfilter-ST-38-20/dp/B07CLXHT31/) (Amazon).
* $14 - [2 pieces of 300 x 200 x 0.13mm](https://www.aliexpress.com/item/32809585908.html) (AliExpress).

See also the link up above for a 43cm x 61cm sheet for $30 (they don't mention if they ship internationally).

The polarizer filter for the camera is actually in a similar price range - starting at around $16 for an OK one (Tiffen, Kenko and Hoya seem to be the brands recommended for entry level).

Here's the [range](https://www.bhphotovideo.com/c/products/Polarizer/ci/115/N/4026728357?sort=PRICE_LOW_TO_HIGH&filters=fct_polarizing-type_35%3Acircular) sold by B+H - they have Tiffen and Hoya (and some odd reason seem to sell some Tiffen lenses under the brand _General Brand_).

Shutter release (and GPS)
-------------------------

Single page guide to pinouts for shutter release ports for all cameras: <https://www.doc-diy.net/photo/remote_pinout/>

Even more complete pinout specifically for Nikon MC-DC2 connector (which they also descibe as a proprietary mini-USB connector): <https://pinoutguide.com/DigitalCameras/nikon_d90_pinout.shtml>

This site also has pinout pages for a large range of other cameras: <https://pinouts.ru/DigitalCameras/>

Various sites describe DIY devices for this port - none of them is what I'd call perfect but they pictures and discussions that cover everything (while often being unclear and/or including extraneous or incorrect information):

* <https://www.cloudynights.com/topic/457536-usb-corded-shutter-control-for-nikon/>
* <https://www.otelescope.com/forums/topic/505-another-usb-cable-for-nikon-its-working/> (slightly bizarre - uses a relay to pull signals high and low).
* <https://www.instructables.com/ESP8266Smartphone-Wireless-Remote-for-DSLR-with-po/>
* <https://grink.com/2010/12/05/nikon-d90-homemade-gps/>
* <https://www.diyphotography.net/build-a-bluetooth-gps-unit-for-nikon/>

The last two involve connecting GPS rather than shutter release but cover taking apart the same connector as is used for shutter release.

It might also be fun to hook up something like the super cheap [Beitian BN-220](https://www.banggood.com/Beitian-Dual-BN-220-GPS-GLONASS-Antenna-Module-TTL-Level-RC-Drone-Airplane-p-1208588.html).

After much searching, I can't find any obvious difference between the BN-220 and the identically priced BN-220T. Neither the Beitian or the wider web offers anything obvious (each is shown in different situations with different cable types and with and without a clear heatshrink cover - so it doesn't seem to be that). The BN-220 seems to be much more common in terms of pages mentioning it and Ardupilot has a [page](https://ardupilot.org/copter/docs/common-beitian-gps.html) covering it (where it notes that such small modules can be very slow to acquire a good enough signal to allow a copter to arm). Note: the Beitian modules feature Ublox chips - the BN-220 can apparently be flashed with the latest firmware from Ublox while the similarly priced BN-180 cannot.

### Level shifter

If controlling the 5V shutter port of a Nikon with a 3.3V MCU board then you need a level shifter such as the [TI 74AHCT125](https://www.adafruit.com/product/1787). All interaction with the camera is unidirectional (even for GPS) so you do not need a more expensive bi-directional level shifter.

While such a level shifter is an annoying additional component (vs using a 5V capable MCU board) it does have the nice characteristic of providing a degree of electrical separation between camera and board.

Wiring up the 74AHCT125 is very simple and described [here](https://learn.adafruit.com/neopixels-on-raspberry-pi/raspberry-pi-wiring#raspberry-pi-wiring-with-level-shifting-chip-3006459-3) by Adafruit for the Raspberry Pi and a Neopixel strip.

### N3 connectors (and WiFi shutter releases)

The MC-DC2 is available for $35 from Nikon - <https://www.nikonusa.com/en/nikon-products/product/remote-cords/mc-dc2-remote-release-cord-%281-meter%29.html>

The basic MC-DC2 PDF manual is available from the amazingly dated looking Nikon [product manuals](https://www.nikonimgsupport.com/ni/NI_article?articleNo=000002351&lang=en_US) support page.

Companies like B&H sell the MC-DC2 for around $27 - see [here](https://www.bhphotovideo.com/c/product/580879-REG/Nikon_25395_MC_DC2_Remote_Release_Cord.html).

Companies of AliExpress sell similar devices for around $2 - e.g. see [here](https://www.aliexpress.com/item/4001115307637.html).

If you just want the connector, you unfortunately have to buy something like this and cut the connector off it as the connector is proprietary and not easily available on its own.

Note: the connector used on the MC-DC2 is often referred to as an N3 connector.

An alternative to the MC-DC2 style shutter release is a simple N3 connector to 2.5mm jack - e.g. see [here](https://www.aliexpress.com/item/32962277670.html). Surprisingly, this isn't particularly cheaper than an MC-DC2 knock-off but maybe there's less waste involved if all you want is the connector (though the MC-DC2 knock-offs come with a straight cable while the N3 to 2.5mm cables are usually spiral - which may be relevant if you want to keep the cable connected to the N3 connector).

Note: you can get shutter control systems that can be connected to many different camera types via a 2.5mm socket - hence the market for 2.5mm to various connector types.

You can also find significantly more expensive such N3-to-2.5mm cables from name-brands:

* $10 - [Neewer](https://www.amazon.co.uk/Neewer-Photography-Accessories-2-5mm-N3-Control/dp/B00OHDARXG/).
* $18 - [Ubertronix](https://www.bhphotovideo.com/c/product/887416-REG/Ubertronix_mc_dc2_MCDC2_Cable_for_Strike.html).

If you're genuinely interested in a shutter release (rather than just the connector), you can also get wireless ones (an option not offered by Nikon). There seem to be two main brands:

* The YouPro MC-292 N3 - e.g. [here](https://www.aliexpress.com/item/32915209731.html).
* The Pixel TW-283 N3 - e.g. [here](https://www.aliexpress.com/item/1005001677529230.html).

Turntables for photogrammetry
-----------------------------

* Fr. 20 - [Hama 25cm turntable](https://www.galaxus.ch/en/s14/product/hama-turntable-255-x-2-cm-tv-furniture-9811823) (also available in 32cm and 40cm variants).
* Fr. 13 - [Ikea 39cm Lazy Susan](https://www.ikea.com/ch/en/p/snudda-lazy-susan-solid-wood-90074483/).
* $26 - [25cm electric turntable](https://www.aliexpress.com/item/32996372258.html).
* $20 - [20cm electric turntable](https://www.aliexpress.com/item/1005001896028502.html).
* $14 - [138mm electric turntable](https://www.aliexpress.com/item/4000338632699.html).
* $19 to $22 - [138mm to 146mm electric turntables](https://www.aliexpress.com/item/1005001923447660.html) (with battery and non-battery options).

The most popular turntables on AliExpress have a 138mm base but obviously, you can put a larger disc on top (at some cost to stability).

For controlling the 5V input for such turntables with an MCU dev board, it looks like a [MOSFET](https://www.adafruit.com/product/355) is the thing to use. It took  a lot of googling to convince myself of this - there were surpringly few convincing sources. The best I found was this Adafruit [tutorial](https://learn.adafruit.com/use-dc-stepper-servo-motor-solenoid-rp2040-pico/solenoids) on controlling a 5V 1.1A solenoid. The Fritzing diagram shows that it's a very simple setup. For a turntable though, I suspect the capacitor and diode aren't needed (as all that will be taken care of within the electronics of the turntable). As usually, other sources also commonly feature a "magic" capacitor for filtering out power supply spikes - with values between 10uF to 47uF (as in the Adafruit tutorial).

Note: the voltage dropped by such MOSFETs is determined by their Rds(on) value, i.e. the size of resistor they behave as at a given voltage - for the Adafruit IRLB8721 that appears to be in the order of milliohms at 5V, i.e. minimal. 

Laser cut aluminum
------------------

Services that that offer online laser cutting for aluminum:

* [Ponoko](https://www.ponoko.com/designs)
* [Oshcut](https://app.oshcut.com/cart)
* [LaserBoost](https://www.laserboost.com/en/create)
* [Xometry](https://xometry.eu/en/laser-cutting/) (its web service failed to load, last time I tried).

Sculpteo only offer woods, plastics and cardboard.

TODO: this section is related to [`turntable-request-for-quote.md`](turntable-request-for-quote.md) (laser cutting a turntable disk) **and** to [`lighting.md`](lighting.md) (laser cutting a disk with holes on which to mount and LED strip).

Green/black/etc. screens
------------------------

Green/black/etc. screens on AliExpress:

* Cotton - https://www.aliexpress.com/item/33035611637.html
* Synthetic - https://www.aliexpress.com/item/33041042045.html

Material is from same store - the synthetic material is considerably cheaper than the cotton but the comments seem to reflect this difference (the synthetic is often described as thin, having a distinctive smell and other issues).

Stands of the type used by Erik Christensen cost serious money even from AliExpress, e.g. [here](https://www.aliexpress.com/item/4000057161419.html) for the obvious reason that they need to be strong and well balanced not to topple over.

T-shaped stands, like this [one](https://www.aliexpress.com/item/32890532311.html), are considerably cheaper.

PiFuHD
------

See the [`pifuhd`](pifuhd) subdirectory for information on:

* Creating a human model with PiFuHD.
* Texturing the resulting model in Blender.
* UV unwrapping a human shaped mesh (automatically and by hand).

Meshroom/AliceVision
--------------------

AliceVision seems to be the name of the project while Meshroom is the name of the application.

Peter France (from Corridor) discusses taking photos (of a rock wall), pulling these into Meshroom and then into Blender - <https://www.youtube.com/watch?v=6VjA9EfkFSc>

On the Meshroom [download page](https://alicevision.org/#meshroom), they link to various other tutorials, including this [one](https://blog.prusaprinters.org/photogrammetry-2-3d-scanning-simpler-better-than-ever_29393/) from the Prusa 3D Printer people. Their other YouTube [link](https://youtu.be/k4NTf0hMjtY) has much more than Peter's video on bump mapping and basically getting your textures looking right (reducing shininess etc.) in Blender - CG Geek also shows how powerful the Sketchfab viewer is (so perhaps the cost vs a thee.js or babylon.js viewer is worth it for certain use-cases). Finally, the link to non-video [tutorial](https://sketchfab.com/blogs/community/tutorial-meshroom-for-beginners) that goes into using the node setup in Meshroom (all the other tutorials just use the default workflow).

As various sources note, Meshroom doesn't like images with any blurriness - you can automate detecting blurry image with OpenCV and Python (all based on Laplace filter):

* <https://www.pyimagesearch.com/2015/09/07/blur-detection-with-opencv/>
* <https://www.analyticsvidhya.com/blog/2020/09/how-to-perform-blur-detection-using-opencv-in-python/>
* <https://pysource.com/2019/09/03/detect-when-an-image-is-blurry-opencv-with-python/>
* <https://stackoverflow.com/a/7767755/245602>

You should use such an approach to sort your images and throw out the once with the worst score (depending on the subject and other factors, it seems the cut-off threshold will be different for different photo sets).

3D web viewers
--------------

Many sites, include [AliceVision](https://alicevision.org/) use an embeddable viewer from Sketchfab, however their restriction on their free tier (one model upload per month) and the [pricing](https://sketchfab.com/plans/individuals) for paid tiers (cheapest is EUR 84 per year) don't make it very attractive for individuals with no commercial intent.

See [`photogrammetry.md`](photogrammetry.md) for model of me on Sketchfab.

The two main open source solutions seem to be:

* babylon.js - see their [viewer](https://doc.babylonjs.com/extensions/babylonViewer) documentation. They also have a [sandbox](https://sandbox.babylonjs.com/) where you can try out models.
* tree.js - see their [loading 3D models](https://threejs.org/docs/#manual/en/introduction/Loading-3D-models) documentation. This documentation specifically mentions Don McCurdy's [glTF Viewer](https://github.com/donmccurdy/three-gltf-viewer) as essentially a good reference implementation of a viewer. For another walk thru of creating a viewer see [here](https://manu.ninja/webgl-3d-model-viewer-using-three-js/) on manu.ninja.

Both the official babylon.js [sandbox](https://sandbox.babylonjs.com/) and semi-official tree.js [sandbox](https://gltf-viewer.donmccurdy.com/) work well with the `.glb` model that I created of myself (see [`pifuhd`](pifuhd) subdirectory).

Lip restrainers and wig caps
----------------------------

For a good 3D model of yourself, you need good photographs of your teeth.

You can do this with spoons as described [here](https://www.worldofsmiles.com/at-home-how-to-take-dental-photos/) and in this [YouTube video](https://www.youtube.com/watch?v=glP78Bp-rdE).

Probably overkill but one can also easily lip restrainers:

* EUR 7 from [Amazon](https://www.amazon.de/Vicloon-Wangenhalter-Mundwinkelhalter-Mund%C3%B6ffner-Zahnaufhellung/dp/B01N0EKDD7/) - pack of 12.
* Fr. 14 from [M+W Dental](https://www.mwdental.ch/spandex-295327---wangenhalter-20527-d-pg-shop.html) (a proper dental supplier) - pack of 2.

### Wig cap

You also need to get your hair out of the way (and then recreate it later for the model) with something like a wig cap, e.g. this [one](https://www.lightinthebox.com/en/p/5pcs-lot-new-fishnet-wig-cap-stretchable-hair-net-snood-wig-cap-net-weaving-cap-open-end-hair-tools_p5767983.html). After looking at WikiHow and videos like [this](https://www.youtube.com/watch?v=CQdOYJyHaBg), I'm fairly convinced the tube style ones must be a lot easier to use than the more cap-like ones.

ArUco
-----

I wonder if [ArUco markers](https://docs.opencv.org/3.4/d5/dae/tutorial_aruco_detection.html) printed on a white t-shirt (e.g. by [Din Schrift](https://www.dinschrift.ch/en/technical)) would make generating a full body model easier for Meshroom.

Note: ArUco markers are a form of [fiducial marker](https://en.wikipedia.org/wiki/Fiducial_marker).

Entry level DSLR
----------------

At the time of writing (June 2021) something like the Canon EOS 2000D (called the Rebel T7 in some markets) with an 18-55mm lens seems to be cheapest of the commonly recommended entry level DSLRs (though at Fr. 390, it's hardly inexpensive). The [Nikon D5100](https://en.wikipedia.org/wiki/Nikon_D5100) comes up in various places as the go-to second-hand entry-level DSLR (introduced in 2011, it's specs still sound respectable).

Note: on some stores the Canon EOS 2000D seems to be sold in ridiculous bundles - various sites say to stay away from bundles and just buy the body and a lens.

Black velvet adhesive sheets
----------------------------

On eBay you can find:

* $8 - 30x20cm - <https://www.ebay.co.uk/itm/183721781687>
* $10 - 100x45cm - <https://www.ebay.co.uk/itm/184796653721>
* $2 - 20x14cm - <https://www.ebay.co.uk/itm/224067639684>
* $4 - 30x20cm - <https://www.ebay.co.uk/itm/224067635839>

The first two are from seller monarchsgarden and the second two from chenting2018. Both are located in China.

chenting2018 has much higher sales than monarchsgarden but unfortunately doesn't seem to do larger sizes.

Photogrammetry scale
--------------------

This looks like an interesting contrast to the void approach of Erik Christensen's void - sitting your target on a pattern designed to help the photogrammetry software.

The scale developed by Samantha Thi Porter (a digital archeologist) is mentioned in a few places, including the Meshroom docs, and can be found [here](http://www.stporter.com/resources/) (see the "Updated Scale for Small-Object Photogrammetry" section).

Miscellaneous
-------------

Mentioned on Corridor Crew, [Polycam](https://poly.cam/) looks fascinating but requires an iPhone 12 Pro, iPhone 12 Pro Max or the 2020 iPad Pro.

For face-capture, [Live Link](https://www.unrealengine.com/en-US/blog/new-live-link-face-ios-app-now-available-for-real-time-facial-capture-with-unreal-engine) for Unreal Engine looks really interesting. It requires an iPhone with a depth camera (the iPhone X or later except SE models).

For a non-iPhone solution using Intel's RealSense cameras, the only commonly mentioned product is the seriously expensive [Dot3D Pro](https://www.dotproduct3d.com/dot3dpro.html) which in tutorials from Intel and others _seems_ to produce very so-so results.
