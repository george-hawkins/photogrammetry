Initially, it's quite hard to work out what lens to use with Raspberry Pi camera module.

But in reality there isn't as much choice as there seems if you want a DoF greater than F1.4 and a focal length greater than 6mm.

Basically, everyone is selling the same thing - a 16mm lens with F1.4 to F16:

* <https://www.adafruit.com/product/4562>
* <https://www.arducam.com/product/c-mount-lens-for-raspberry-pi-high-quality-camera-16mm-focal-length-with-manual-focus-and-aperture-adjustment/>
* <https://www.seeedstudio.com/16mm-telephoto-lens-p-4452.html>
* <https://www.waveshare.com/16mm-Telephoto-Lens-for-Pi.htm>

Fitting and adjusting this style of lens is covered here:

* <https://static.raspberrypi.org/files/product-guides/Typical_C-Mount_Lens_Guide.pdf>

You can find out more about how sensor size and lens size interact here:

* <https://www.1stvision.com/machine-vision-solutions/2017/08/how-does-a-lens-optical-format-relate-to-machine-vision-cameras.html>

However, there's only so-much value in this knowledge given that you don't really have too much choice when it comes to lenses in the cheaper segment.

For a practical overview of lenses and the the Raspberry Pi HQ Camera Module, see:

* <https://learn.adafruit.com/raspberry-pi-hq-camera-lenses?view=all>

Seeed and WaveShare also have nice guides:

* <https://www.seeedstudio.com/blog/2020/06/18/a-complete-guide-to-help-you-choose-lenses-for-your-raspberry-pi-high-quality-camera-m/>
* <https://www.waveshare.com/wiki/Raspberry_Pi_HQ_Camera>

Lens adapter and polarizing filter
----------------------------------

The 16mm lens above _appears_ to be 39mm wide so it _should_ take this lens adapter:

* <https://www.bhphotovideo.com/c/product/809744-REG/Sensei_sur3952_39_52mm_Step_Up_Ring.html>

And then you can use polarizing filters like this:

* Basic - <https://www.bhphotovideo.com/c/product/56631-REG/Tiffen_52CP_52mm_Circular_Polarizing.html>
* Next-step-up - <https://www.bhphotovideo.com/c/product/533172-REG/Tiffen_52HTCP_52mm_Digital_HT_High.html>

Note: you can step up to many lens sizes from 39mm, 52mm is simply the most popular size in terms of available filters etc.

Notes
-----

WaveShare have even higher mega-pixel sensors but they're only compatible with the Raspberry Pi Compute Module (and the Jetson Nano):

* <https://www.waveshare.com/product/raspberry-pi/cameras/12m-pixels/imx477-12.3mp-camera.htm>

ArduCam's model naming convention isn't easy to decipher, here's the convention they use:

* <https://www.arducam.com/docs/lens/arducam-lens-part-number-naming-convention/>
