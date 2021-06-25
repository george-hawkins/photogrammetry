Complete Photogrammetry course
==============================

Notes from the 5 part video course [Complete Photogrammetry](https://www.youtube.com/watch?v=010lAKpr7JE).

You can use a phone but the more mega-pixels really do matter in this context so ideally you want a reasonable semi-pro camera.

Don't worry about the lens - any will do - but it does affect the depth of field (DoF).

You want as high DoF as possible - so the higher the supported apperture number the better, e.g. some go as high as 22.

Note: high apperture _number_ actually means as small apperture as possible.

You don't want any part of your subject to be out of focus in any given photo - this is what you achieve with a high DoF.

He says he gets really sharp images with a 85mm f1,8 lens but can't get close and he says he can get close with 50mm f1,8 macro but will have DoF issues.

He actually uses a 28-75mm f2,9 zoom which gives him flexibility and good DoF at the cost of some sharpness.

He uses a [lazy susan](https://en.wikipedia.org/wiki/Lazy_Susan) (available from Ikea etc.) to rotate his object in front of his camera.

For the camera settings, he:

* Cranks up the aperture from 2.8 to the max (shown as f22 on his camera).
* He dramatically raises the exposure time from the usual near instantaneous to 2.5s
* He keeps the ISO low (ISO 100 is shown) as higher ISO results in noise.

But this setup still results in shadows and the 2.5s exposure time obviously makes the process extremely slow - so the AR400 ring flash (seen in every photogrammetry video, it seems) comes out at this point.

He recommends combining it with a quick release (what looks like a [Manfrotto 323](https://www.bhphotovideo.com/c/product/554141-REG/)) - see 10m 16s mark in the video.

This flash allows him to reduce the shutter speed to 1/125 of a second and resolves the shadows issue.

We still have the serious problem that with the lazy susan, the photogrammetry will notice the background isn't moving and completely throw it off.

You _could_ manually mask out the background afterwards in each image or with certain software you can photograph the scene without the subject first and then have the software drop out the parts of the image that are unchanging relative to this initial image (if the s/w supports that). But he says he doesn't trust this approach (but doesn't go into why).

So he bought a photo tent initially but doesn't recommend it - he says the flash light actually bounces off the sides of the tent. But he uses the tent for the moment with a black velvet like background over the bottom and back of the tent (leaving the sides and top as they are).

He notes at this point - always shoot in RAW.

He then introduces an electric turntable so speed up the process - and points out that if you can control the turntable to stop as you take the photos then you can set up a fully automatic process where it's up to you how fast you want the process to be - it you can accept a slower process then you can use a much cheaper ring _light_ rather than a ring _flash_.

With a real ring flash you can leave the turntable on continuous slow rotation (in his case one rotation every 30s) without needing to start and stop and just use the cameras standard timelapse or interval shooting feature for taking the photos.

Actually, his turntable takes 32 seconds to rotate fully and he sets his interval timer to shoot 32 photos.

Note: he's using what looks suspiciously like one of those cheap electric jewellery turntables with a white top (similar to one of [these](https://www.aliexpress.com/item/1005001923447660.html)).

He puts down a pattern - actually a cow pattern (like this CC BY tileable [pattern](https://www.flickr.com/photos/anniekate/644895289)) with added lines, circles and letters (see 20m mark in video) to give the photogrammetry sotware something to track (especially important when the subject itself has little to track).

He discusses that it's really important to remove reflections and you can do this with cross polarization - he explains cross polarization at the 21m 30s mark. He uses a 3D printed mount (see main [`README`](README.md) for links to models) to hold the polarization file in front of the ring flash. But he says you can also just tape it in place.

For the camera lens itself, he uses an amazingly expensive Kase polarization filter (the cheapest Kase polarization filters start at $80 on B+H) but notes you can use whatever you want but just avoid the very cheapest as they introduce image artifacts.

He uses a mirrored ball as his subject, places the flash in light mode, i.e. on continuously, and rotates the film over the flash until you can no longer see the flash's light in the image shown on the camera's LCD - you still see all other reflections, it's just the flash light that's gone. So I'm not quite sure how the s/w gets substantially less confused but maybe this is just establishing the ideal lighting but you still need to eliminate reflective and transparent surfaces (e.g. with 3D scanning spray - see main `README`).

This polarization setup also means that the background is now completely black - all odd little reflections off it have been eliminated - though he notes you may still need to postprocess the images to get the background down to pure black (I suspect you can also configure this in the camera).

Polarization kills about 3/4 of the light so he has to increase the ISO to 200.

Interestingly, he's using the AS400 at a 1/4 of power - because otherwise it can't recharge quickly enough between photos. So he's limited in how much of this expensive flashes strength he can really use and is constrained from upping its output rather than increasing the ISO value. I assume the flash also constrains him from simply decreasing the shutter speed to compensate, e.g. making it 4 times longer - with a ring _light_ rather than a _flash_ presumably you have this option.
