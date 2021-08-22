Non-AliExpress lighting
=======================

The LEDs on AliExpress may well have the stated electrical characteristics but most of the other characteristics (lm/W, CCT, viewing angle) are less certain. In particular the [CRI](https://insights.regencylighting.com/how-to-choose-color-rendering-index-cri-a-practical-guide) is unlikely to be particularly high. Ideally, for photography you want a CRI of at least 80 but this is a value that's never listed for LEDs on AliExpress.

Here are the items, I'd buy if trying to reproduce a similar setup using parts from Digikey and other Western suppliers.

---

LEDs - Cree - XPLBWT-00-0000-000HV30E1

1050mA / 6500K

These have clearly defined characteristics unlike AliExpress LEDs - e.g. CRI is 80, i.e more than acceptable.

* <https://www.digikey.ch/product-detail/en/creeled-inc/XPLBWT-00-0000-000HV30E1/XPLBWT-00-0000-000HV30E1-ND/7349388>
* <https://cree-led.com/media/documents/dsxpl2.pdf>

Unfortunately, neither Mouser nor Digikey stock them - you have to order a minimum of 500.

4000K seems to be the highest color temperature that's commonly stocked, e.g.:

* <https://www.digikey.ch/product-detail/en/creeled-inc/XPLBWT-00-0000-000HV30E5/XPLBWT-00-0000-000HV30E5CT-ND/6198658>

Mouser have 6200K ones with a lower CRI of 70 available singly:

* <https://www.mouser.ch/ProductDetail/Cree-LED/XPLAWT-00-0000-000BV6051>

The LEDiL lenses are also compatible with these 1050mA / 5700K / 82CRI LEDs from Osram:

* <https://www.mouser.ch/ProductDetail/OSRAM-Opto-Semiconductors/GW-PUSTA1EM-NBND-XX52-1>

These have to be ordered in reels of 600.

Only the lower wattage variants of these are available from Digikey.

Lenses - LEDiL - TINA-SC-M

* <https://www.digikey.ch/product-detail/en/ledil/CP17595-TINA-SC-M/711-CP17595-TINA-SC-M-ND/14123663>
* <https://www.ledil.com/data/prod/Tina/17595/17595-ds.pdf>

Driver - MeanWell - LDH-65-1050W

Can handle about 19 1050mA LEDs with an input voltage of 24V.

* <https://www.digikey.ch/products/en?keywords=LDH-65-1050W>
* <https://www.meanwell-web.com/content/files/pdfs/productPdfs/MW/LDH-65/LDH-65-spec.pdf>

AliExpress style LEDs on Digikey
--------------------------------

The style of LED used in all the 3W LEDs plus heatsink combos seen on AliExpress is called "2-SMD, Gull Wing Exposed Pad" and seems to be no longer generally produced for Western markets.

The only such item still listed as active, on Digikey, is the Lumix [SML-LXL8047UWCTR/3](https://www.digikey.ch/product-detail/en/lumex-opto-components-inc/SML-LXL8047UWCTR-3/67-2113-2-ND/2346571) but it is a non-stock item. They do still have availablity on this form factor for 350mA LEDs like the Seoul Semiconductor [N42180-06-S2](https://www.digikey.ch/product-detail/en/seoul-semiconductor-inc/N42180-06-S2/N42180-06-S2TR-ND/2504440) but Seoul Semiconductor's range of LEDs in this form factor are all listed as obsolete.

While the gull-wing form factor isn't commonly available, 700mA LEDs are - use this one for forum posts if looking for something that has a datasheet while having similar characteristics to those claimed for the LEDs on AliExpress:

* <https://www.digikey.ch/product-detail/en/broadcom-limited/ASM6-SWD1-NQTHH/516-ASM6-SWD1-NQTHHCT-ND/13693579>
