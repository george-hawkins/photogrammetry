Videos:

* [Scanning in the void](https://www.youtube.com/watch?v=Il6LVXqSlRg) by Erik Christensen (the Witstro AR400 that he uses shows up all the time in photogrammetry videos).
* [Scanning featureless objects](https://www.youtube.com/watch?v=krm9vDlTaxU) also by Erik Christensen.
* [Cross polarization explained](https://www.youtube.com/watch?v=yhjKO1a99OQ) - he buys his _linear_ polarization film from [Polarization.com](http://polarization.com/polarshop/product_info.php?cPath=21&products_id=28) - 43cm x 61cm for $30 and then uses a _circular_ polarization filter on his camera and discuss the effect seen when rotating one relative to the other.

Erik Christensen rotates his subject on an amazingly expensive [Syrp Genie Mini II panning motion control system](https://www.bhphotovideo.com/c/product/1483069-REG/syrp_sy0033_0001_genie_mini_ii_panning.html). You can get much cheaper devices like the [Movo Photo MTP-11](https://www.bhphotovideo.com/c/product/1624190-REG/movo_photo_mtp_11_motorized_panoramic_time.html) but why not just use an electric turntable from AliExpress (see section below).

Erik Christensen doesn't discuss how he made the polarizing film mount he uses so, Exitaph created one himself and released the 3D model and details [here](https://cults3d.com/en/3d-model/gadget/flashpoint-rf-400-godox-ar400-90-degree-magnetic-polarizing-film-mount).

For an amazing automated scanning-in-the-void system in action see [here](https://www.youtube.com/watch?v=dyPn5lmq9B4&t=329s) (link starts 5m 29s in to the video - the first 5 minutes show building the system).

The guy who made this system also has a [5 part series](https://www.youtube.com/watch?v=010lAKpr7JE) on photogrammetry where he answers all the questions others barely mention, e.g. how mnay photos do you _really_ need, what kind of lens do you need. He compares all different kinds of equipment so at the end you have a much clearer idea of what impacts you results and what price point you want to go for.

There are many similar builds including this [one](https://www.youtube.com/watch?v=Fj7wGGXPM0A) that he's since scaled down into something far smaller that's open source and available as a kit [here](https://en.openscan.eu/shop).

Ben Kreimer has a nice [page](http://www.immersiveshooter.com/2020/05/11/photogrammetry-photography-guide-ring-flash-photography/) on choosing a ring flash for photogrammetry - as with everyone else he goes with the Witstro AR400. He specifically doesn't recommend the much cheaper ring _lights_ available from many sources. He mentions that "I consistently shoot at 200 ISO, f/16, 1/200th of a second".

---

* $500 - [Witstro AR400](https://www.bhphotovideo.com/c/product/1341907-REG/godox_ar400_witstro_ring_flash.html).
* $70 - [Bolt VM-160](https://www.bhphotovideo.com/c/product/750878-REG/bolt_vm_160_led_macro_ring.html).

There are no end of people building there own ring flashes:

* https://www.youtube.com/watch?v=xsd5b9p19nM
* https://www.youtube.com/watch?v=bcIdqdecKDI

You can find the designs to go with the second video [here](https://www.facebook.com/photo?fbid=645114522288869).

But as covered elsewhere, I've come to the conclusion that this looks cooler than it works out in practice.

You could use a large Li-Po like [this](https://www.gensace.de/gens-ace-5000mah-11-1v-3s1p-50c-lipo-battery-pack-with-xt-90-plug-bashing-series.html) to properly power such a project.

---

The brightest cold white / neutral white LED E27 bulbs that I've found that are easily available are the 1521lm CorePro bulbs from Philips.

See [here](https://www.lighting.philips.com/main/prof/led-lamps-and-tubes/led-bulbs/corepro-ledbulbs). However, the 4000K variants seem much more readily available than the 6000K variants (but 4000K is still better than the common 2700K warm white).

E.g. here are the 4000K variants from [Brack](https://www.brack.ch/philips-professional-lampe-corepro-ledbulb-12-5-100w-a60-e27-840-700751) and [Microspot](https://www.microspot.ch/de/wohnen-licht/leuchtmittel/leuchtmittel-pro--c489400/philips-corepro-ledbulb-lampe-led-e27-12-5-w--p0001863627).

---

Services that that offer online laser cutting for aluminum:

* [Ponoko](https://www.ponoko.com/designs)
* [Oshcut](https://app.oshcut.com/cart)
* [LaserBoost](https://www.laserboost.com/en/create)
* [Xometry](https://xometry.eu/en/laser-cutting/) (its web service failed to load, last time I tried).

Sculpteo only offer woods, plastics and cardboard.

---

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

---

If controlling the 5V shutter port of a Nikon with a 3.3V MCU board then you need a level shifter such as the [TI 74AHCT125](https://www.adafruit.com/product/1787). All interaction with the camera is unidirectional (even for GPS) so you do not need a more expensive bi-directional level shifter.

While such a level shifter is an annoying additional component (vs using a 5V capable MCU board) it does have the nice characteristic of providing a degree of electrical separation between camera and board.

Wiring up the 74AHCT125 is very simple and described [here](https://learn.adafruit.com/neopixels-on-raspberry-pi/raspberry-pi-wiring#raspberry-pi-wiring-with-level-shifting-chip-3006459-3) by Adafruit for the Raspberry Pi and a Neopixel strip.

---

The MC-DC2 is available for $35 from Nikon - <https://www.nikonusa.com/en/nikon-products/product/remote-cords/mc-dc2-remote-release-cord-%281-meter%29.html>

The basic MC-DC2 PDF manual is available from the amazingly dated looking Nikon [product manuals](https://www.nikonimgsupport.com/ni/NI_article?articleNo=000002351&lang=en_US) support page.

Companies like B&H sell the MC-DC2 for around $27 - see [here](https://www.bhphotovideo.com/c/product/580879-REG/Nikon_25395_MC_DC2_Remote_Release_Cord.html/overview).

Companies of AliExpress sell similar devices for around $2 - e.g. see [here](https://www.aliexpress.com/item/4001115307637.html).

If you just want the connector, you unfortunately have to buy something like this and cut the connector off it as the connector is proprietary and not easily available on its own.

Note: the connector used on the MC-DC2 is often referred to as an N3 connector.

An alternative to the MC-DC2 style shutter release is a simple N3 connector to 2.5mm jack - e.g. see [here](https://www.aliexpress.com/item/32962277670.html). Surprisingly, this isn't particularly cheaper than an MC-DC2 knock-off but maybe there's less waste involved if all you want is the connector (though the MC-DC2 knock-offs come with a straight cable while the N3 to 2.5mm cables are usually spiral - which may be relevant if you want to keep the cable connected to the N3 connector).

Note: you can get shutter control systems that can be connected to many different camera types via a 2.5mm socket - hence the market for 2.5mm to various connector types.

If you're genuinely interested in a shutter release you can also get wireless ones (an option not offered by Nikon). There seem to be two main brands:

* The YouPro MC-292 N3 - e.g. [here](https://www.aliexpress.com/item/32915209731.html).
* The Pixel TW-283 N3 - e.g. [here](https://www.aliexpress.com/item/1005001677529230.html).

---

Turntables for photogrammetry:

* Fr. 20 - [Hama 25cm turntable](https://www.galaxus.ch/en/s14/product/hama-turntable-255-x-2-cm-tv-furniture-9811823) (also available in 32cm and 40cm variants).
* Fr. 13 - [Ikean 39cm Lazy Susan](https://www.ikea.com/ch/en/p/snudda-lazy-susan-solid-wood-90074483/).
* $26 - [25cm electric turntable](https://www.aliexpress.com/item/32996372258.html).
* $14 - [14cm electric turntable](https://www.aliexpress.com/item/4001352037979.html).
