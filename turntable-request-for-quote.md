Design for stepper-based turntable using GoBilda parts
======================================================

Turtables usually involve continuous motion - I want a turntable that will stop and start every fixed number of degrees of rotation, e.g. 50 steps of 7.2 degrees to do a full 360 degree rotation. The turntable is only required to move in a single direction, e.g. clockwise.

I'm only interested in the structural and mechanical elements of the design (the stepper will be controlled by electronics and software that are outside the design scope).

All structural parts must come from GoBilda and the stepper motor from Pololu - this is a hard requirement.

* GoBilda - <https://www.gobilda.com/>
* Pololu - <https://www.pololu.com/category/87/stepper-motors>

I appreciate that some people may find it awkward working with the metric sized components of GoBilda.

No additional modification (drilling, bending etc.) should be required.

The only exception to this rule is the plate for the turntable itself - this can be e.g. an aluminium plate (from any source) that's drilled to accommodate the holes for some kind of hub.

The aim should be to keep the overall cost of parts low, e.g. Pololu sell several steppers costing more than $150 but ideally something _substantially_ cheaper would be used.

A naive design would involve e.g.:

* A $18 [42x38mm, 2.8V, 1.7 A/Phase, 200 Steps/Rev bibolar stepper](https://www.pololu.com/product/2267)
* A $6 [5mm bore set screw hub](https://www.gobilda.com/1308-series-lightweight-set-screw-hub-5mm-bore/)
* A 250mm x 1mm aluminium disc

Holes would then be drilled in the disc, the hub attached to the disc and then to the motor - job done.

However, with no structure suppoting it, such a design will not be stable and it's unclear what sort of weight it could handle on the disc or whether it will deal smoothly with repeated stopping and starting.

So some requirements:

* The disc/motor combination should be able to handle an item of at least 500g placed on the turntable.
* The starting/stopping should involve very little judder - any item placed on the turntable shouldn't move around as a consequence.
* The turntable structure itself should be stable, i.e. it shouldn't topple over or move around when in action.

All that is required is the design and bill-of-materials - an actual implementation of the design is not required or desired. However, notes should be included to make clear how the design is better than the naive design outlined above - i.e. making clear that it is stable, involves little judder and can be reasonably expected to handle an object of at least 500g sitting on the turntable.

This design is for a small open source project so set your expectations accordingly as to what can be accommodated when quoting for this project.

Your design will be made freely available to anyone who wishes to use it and will be licensed under Creative Commons Attribution 4.0 (CC BY 4.0) meaning that you must be credited.

See <https://creativecommons.org/licenses/by/4.0/>

For alternative possible licenses, see <https://en.wikipedia.org/wiki/Open-source_hardware#Licenses>

## Additional details on the disc

The disc, ideally, should be no smaller that 250mm and no bigger than 300mm - you can propose a material, thickness and diameter.

I tried sourcing 300mm x 1mm aluminum discs in the belief that such disks would be strong enough and easy to drill.

However, they weren't as easily available as I expected. I found some on eBay, e.g.:

* [200mm x 1.6mm aluminum disc](https://www.ebay.com/itm/202636098751).
* [12" x 1/16" aluminum disc](https://www.ebay.com/itm/201988333587).
* [300mm x 1mm aluminum disc](https://www.ebay.com/itm/322556775607) (details in German).

Steel disks were much more common, e.g. these ones (again from eBay):

* [12" x 1/16" steel disc](https://www.ebay.com/itm/192248841896).
* [200mm x 1.5mm steel disc](https://www.ebay.com/itm/184585897628) (details in German).

But what I perceive as the increased difficulty of drilling them makes them a less popular choice for me.

The surface of the disc will be covered in adhesive velvet. This adhesive velvet will be sourced separately and should not be included in the BOM. However, it should be considered if suggesting an alternative material for the disc, e.g. POM would be problematic for any adhesive (quite apart from POM never being quite flat).

Your input would be welcome - perhaps something completely different, e.g. a laser cut disc from Ponoko made from wood or some plastic would work as well or better. Or even a 3D printed disc. The disc needs to be something that can be ordered fairly easily and require no more finishing than some basic drilling (to attach a hub or whatever).

* Ponoko - https://www.ponoko.com/materials
* Sculpteo - https://www.sculpteo.com/en/lasercutting/laser-cutting-materials/
