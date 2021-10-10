If you want to use a battery or a 12V or 24V DC supply then you need a step-up DC LED driver.

The two main options seem to be:

* the 700mA variant from the MeanWell 65W LDH series - handles up to 24 LEDs with 24V input.
* the 500mA variant from the MeanWell 45W LDH series - handles up to 26 LEDs with 24V input.
* the 700mA variant from the MeanWell 45W LDH series - handles up to 19 LEDs with 24V input.

* <https://www.digikey.ch/products/en?keywords=LDH-65-700W>
* <https://www.digikey.ch/product-detail/en/mean-well-usa-inc/LDH-45A-500W/1866-5298-ND/7704778>

Note that these are PWM dimmable (unlike the AliExpress AC drivers).

Mouser and Conrad also carry these items:

* <https://www.mouser.ch/ProductDetail/MEAN-WELL/LDH-45A-500W>
* <https://www.conrad.ch/de/p/mean-well-ldh-45a-500w-dc-dc-wandler-print-43-w-anzahl-ausgaenge-1-x-1292797.html>

A suitable battery for these drivers would need to be something like this 6S (i.e. 22.2V) Lipo:

* <https://www.brack.ch/gens-ace-rc-akku-lipo-1250-mah-22-2-v-60c-636447>

It's more than capable of providing the current needed to power even two LED drivers.

For a Lipo calculator see:

* <https://www.radiocontrolinfo.com/information/rc-calculators/rc-lipo-battery-power-configuration-calculator/>

A 3S battery could do the job too but the efficiency fall-off when powering the maximum number of LEDs is higher:

* <https://www.brack.ch/tattu-rc-akku-lipo-650-mah-11-1-v-75c-967771>

Suitable 3S batteries start at far cheaper prices than suitable 6S batteries.

Note: a 3S battery starts at 12.6V when fully charged and you should stop using it once it hits 11.12V, i.e. 15% capacity.

The 700mA 65W MeanWell LED driver requires 3.1A@24V or 6.2A@12V.

Power supplies
--------------

12V 5A:

* <https://www.adafruit.com/product/352>
* <https://www.sparkfun.com/products/14934>

12V 10A:

* <https://www.reichelt.com/ch/en/desktop-power-supply-unit-120-w-12-v-10-a-ea11011h1246-p293289.html>
* <https://www.reichelt.com/ch/de/netzteil-itx-120w-extern-it88882103-p210800.html>

24V 5A:

* <https://www.reichelt.com/ch/en/desktop-power-supply-120-w-24-v-5-a-mw-gst120a24-p171066.html>
* <https://www.digikey.ch/product-detail/de/mean-well-usa-inc/GST120A24-P1M/1866-2040-ND/7703595>

Note: you can also get relatively cheap 120W laptop power supplied but they're often odd voltages for specific laptop models.

Dimming via Arduino
-------------------

This thread covers dimming via PWM using an Arduino:

* <https://forum.arduino.cc/t/controlling-led-brightness-with-a-pwm-signal-to-led-driver/117328>
