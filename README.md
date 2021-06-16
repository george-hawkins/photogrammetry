Upgrade Nikon firmware
----------------------

Press _MENU_ on your camera and go to the _SETUP MENU_ (the one with the spanner icon). Then scroll to _Firmware version_ (it's the very last item in this menu) and select it.

You'll see a list of firmware versions for the various components of your camera:

* A - camera operation.
* B - image processing.
* L - lens distortion control data.
* S - flash unit.

On mirrorless cameras you may see C for camera and LF for the lens data.

Note that for both L and LF, the firmware involved is actually the camera's DB of lenses which includes lens correction information etc. It is not firmare for the lens itself.

For more on distortion control, see [here](https://www.nikonimgsupport.com/eu/BV_article?articleNo=000006158&lang=en_GB).

You can find the latest firmware for your camera at the [Nikon Download Center](https://downloadcenter.nikonimglib.com/en/index.html).

From here, navigate to the page for the [camera body](https://downloadcenter.nikonimglib.com/en/products/19/D3100.html) (in my case, a D3100) and then go to _Firmware_.

There I found two firmware files:

* D3100 Firmware
* Distortion control data

The first will update the A and B firmware (if there are newer versions of both) while the second will update the L firmware.

Depending on your camera, there may be different sets of firmware that will update different components.

Bizarrey, Nikon bundle the firmware updates into `.exe` files (for Windows) and `.dmg` files (for Mac) - even though there's nothing OS specific about the files involved. The `.exe` and `.dmg` files both just unpack to reveal a firmware file that you'll copy to your camera's memory card.

---

On Linux systems, you can download the Mac `.dmg` and unpack it with [7-Zip](https://www.7-zip.org/), e.g. like so:

```
$ sudo apt install p7zip-full
$ cd ~/Downloads
$ 7z x F-D3100-V102M.dmg
$ ls F-D3100-V102M/D3100Update
D3100_0102.bin
```

The file names involved, e.g. `F-D3100-V102M.dmg` and `D3100_0102.bin`, will of course vary depending on your camera and the firmware release.

---

Once you have the `.bin` file, just copy it to the root directory of your camera's memory card, then put it back in the camera and go back to the _Firmware version_ menu item mentioned above.

Now, the camera will present you with an _Update_ option which will upgrade the camera's firmware (this takes several minutes).

Remember to delete the `.bin` file on the memory card each time you complete a successful upgrade.

If you've got further firmware to upgrade (e.g. in my case the Distortion control data) then just go through the same steps for it.

Update
------

It turned out that the distortion control data for Mac actually, did involve having to run an application. And the packaged application was so old (it was built for PowerPC and i386) that it wouldn't run on an x86_64 Mac.

I eventually had to use a Windows machine. All the downloaded `.exe` does is extract a `.bin` file into `C:\Users\Public\Desktop`. A ridiculous layer of complexity that adds nothing - why they couldn't allow you to download the tiny `.bin` file directly, I've no idea.


